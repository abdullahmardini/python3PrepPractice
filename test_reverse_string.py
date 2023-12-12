#!/usr/bin/env python3

from reverse_string import StringReverser

def test_reverse_word():
    word = ['a', 'p', 'p', 'e', 'n', 'd']
    revword = ['d', 'n', 'e', 'p', 'p', 'a']
    reverser = StringReverser()
    reverser.reverse_word(word, 0, 5)
    assert word == revword

def test_reverse_string():
    string = ['i', ' ', 'a', 'm']
    revstring = ['a', 'm', ' ', 'i']
    reverser = StringReverser()
    reverser.reverse_string(string)
    assert string == revstring
