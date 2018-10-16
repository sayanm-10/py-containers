#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest

def anagram(str1, str2):
    ''' returns True if str1 and str2 are anagrams using only lists '''

    return sorted(list(str1)) == sorted(list(str2))


class AllTest(unittest.TestCase):
    ''' Test cases for all functions '''

    def test_anagram(self):
        ''' test anagram check based on lists '''

        self.assertTrue(anagram('dormitory', 'dirtyroom'))
        self.assertTrue(anagram('racecar', 'carrace'))
        self.assertTrue(anagram('', ''))
        self.assertFalse(anagram('class', 'blast'))

if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    unittest.main(exit=False, verbosity=2)