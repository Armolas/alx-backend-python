#!/usr/bin/env python3
'''tests the utils module'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''The access nested map test class'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''tests the access nested map'''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested_map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in {'a': 1}"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_msg):
        '''tests nested ma exception'''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        actual_exception_msg = str(context.exception)
        self.assertIn(expected_exception_msg, actual_exception_msg)

class TestGetJson(unittest.TestCase):
    '''The get json test class'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''tests get_json'''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    '''Memoize test class'''
    class TestClass:
        '''test class'''
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        '''tests momoize'''
        with patch.object(self.TestClass, 'a_method', return_value=42) as mock_a_method:
            obj = self.TestClass()

            # Call a_property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Assert that a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
