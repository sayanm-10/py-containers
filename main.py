#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from collections import defaultdict, Counter

def anagram(str1, str2):
    ''' returns True if str1 and str2 are anagrams using only lists '''

    return sorted(list(str1)) == sorted(list(str2))

def anagram_dd(str1, str2):
    ''' returns True if str1 and str2 are anagrams using default dict '''

    dd = defaultdict(int)

    # add chars to dd
    for c in str1:
        dd[c] += 1

    for c in str2:
        # check if all chars in str2 are in dd
        if c not in dd.keys():
            return False
        else:
            # reduce char frequency by 1
            dd[c] -= 1

    # if any char has remaining freq > 0, return false
    return not any(dd.values())

def anagram_counter(str1, str2):
    ''' returns True if str1 and str2 are anagrams using counter '''

    return Counter(str1) == Counter(str2)


class AllTest(unittest.TestCase):
    ''' Test cases for all functions '''

    def test_anagram(self):
        ''' test anagram check based on lists '''

        self.assertTrue(anagram('dormitory', 'dirtyroom'))
        self.assertTrue(anagram('racecar', 'carrace'))
        self.assertTrue(anagram('', ''))
        self.assertFalse(anagram('class', 'blast'))

    def test_anagram_dd(self):
        ''' test anagram check based on default dict '''

        self.assertTrue(anagram_dd('dormitory', 'dirtyroom'))
        self.assertTrue(anagram_dd('racecar', 'carrace'))
        self.assertTrue(anagram_dd('', ''))
        self.assertFalse(anagram_dd('class', 'blast'))

    def test_anagram_counter(self):
        ''' test anagram check based on counter '''

        self.assertTrue(anagram_counter('dormitory', 'dirtyroom'))
        self.assertTrue(anagram_counter('racecar', 'carrace'))
        self.assertTrue(anagram_counter('', ''))
        self.assertFalse(anagram_counter('class', 'blast'))

if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    unittest.main(exit=False, verbosity=2)