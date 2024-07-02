#!/usr/bin/env python3
'''test for client'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    '''Tests github client'''
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''test the organization'''
        mock_response = Mock()
        mock_response.json.return_value = {"org": org_name}
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )
        self.assertEqual(result, {"org": org_name})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        '''tests the public repo urls'''
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        mock_org.return_value = {"repos_url": expected_repos_url}
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, expected_repos_url)

    @patch('client.get_json')
    @patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
            )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        '''tests the public repos'''
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = expected_repos_url
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mock_payload
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2", "repo3"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(expected_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        '''tests if a github client has license'''
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
        (
            'org_payload',
            'repos_payload',
            'expected_repos',
            'apache2_repos'
            ),
        [
            (
                fixtures.org_payload,
                fixtures.repos_payload,
                fixtures.expected_repos,
                fixtures.apache2_repos
                ),
            ]
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Github client integration class'''
    @classmethod
    def setUpClass(cls):
        """Set up the class for integration tests"""
        cls.get_patcher = patch(
                'requests.get',
                side_effect=cls.mocked_requests_get
                )
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after integration tests"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mock requests.get to return the appropriate fixture"""
        if url == "https://api.github.com/orgs/google":
            return Mock(**{'json.return_value': fixtures.org_payload})
        elif url == "https://api.github.com/orgs/google/repos":
            return Mock(**{'json.return_value': fixtures.repos_payload})
        return Mock(**{'json.return_value': {}})

    def test_public_repos(self):
        """Test the public_repos method with integration test"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license filtering"""
        client = GithubOrgClient('google')
        self.assertEqual(
                client.public_repos(license="apache-2.0"),
                self.apache2_repos
                )
