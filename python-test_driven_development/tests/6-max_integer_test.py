#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 10, 5]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 99]), 99)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_list_of_same_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.4, 2.5]), 3.4)

    def test_mixed_ints_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_string_input(self):
        self.assertEqual(max_integer("abcxyz"), "z")

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])

    def test_list_with_string_and_int(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])
