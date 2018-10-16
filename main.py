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

def covers_alphabet(sentence):
    ''' returns True if sentence includes at least one instance of every 
        character in the alphabet or False using only Python sets '''

    for letter in set('abcdefghijklmnopqrstuvwxyz'):
        if letter not in set(sentence.lower()):
            return False

    return True

def book_index(words):
    ''' takes a list of tuples (word, index) and returns a sorted list
        of each word and all its occurrences '''

    dd = defaultdict(list)

    # sort the index of words so that the indices are inserted in ascending order
    for item in sorted(words, key= lambda k: k[1]):
        dd[item[0]].append(item[1])

    # sort default dict (by keys)
    return [[item[0], item[1]] for item in sorted(dd.items())]

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

    def test_covers_alphabet(self):
        ''' test covers_alphabet '''

        self.assertTrue(covers_alphabet('abcdefghijklmnopqrstuvwxyz'))
        self.assertTrue(covers_alphabet('aabbcdefghijklmnopqrstuvwxyzzabc'.upper()))
        self.assertTrue(covers_alphabet("The quick, brown, fox; jumps over the lazy dog!"))
        self.assertTrue(covers_alphabet('We promptly judged antique ivory buckles for the next prize'))
        self.assertFalse(covers_alphabet(''))
        self.assertFalse(covers_alphabet('abc'))
        self.assertFalse(covers_alphabet('We promptly judged antique ivory buckles for the next...'))

    def test_book_index(self):
        ''' test book_index '''

        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), \
                ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), \
                ('could', 2), ('chuck', 1), ('wood', 1)]
        
        expected_result = [['a', [1, 1]], ['chuck', [1, 3]], ['could', [2]], \
                    ['how', [3]], ['if', [1]], ['much', [3]], \
                    ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]

        unexpected_result = [['a', [1, 1]], ['woodchuck', [1, 2]], ['if', [1]], \
                            ['chuck', [1, 3]], ['wood', [1, 3]], ['would', [2]], \
                            ['could', [2]], ['how', [3]], ['much', [3]]]

        self.assertTrue(book_index(woodchucks) == expected_result)
        self.assertFalse(book_index(woodchucks) == unexpected_result)


if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    unittest.main(exit=False, verbosity=2)
