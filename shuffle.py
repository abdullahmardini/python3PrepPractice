"""
Contained practice script for interviewing.io
https://interviewing.io/mocks/interviewing.io-python-string-shuffle-and-analysis

Interview question
1) Write a function that takes a string as an input and returns a shuffled version of that string (i.e. a version where each character is just as likely to be in any given position)
2) Write a function that analyzes how well your previous function randomly shuffles the string
"""
#!/usr/bin/python3
import random
import sys
from typing import Callable

def shuffle_string_recursive(string: str) -> str:
    '''
    input: string
    return: string
    Recursive implementation to shuffle a string.
    Takes a string, returns a string.
    Note: not ideal in python. Just for practice.
    '''
    if len(string) == 1:
        return string
    i = random.randrange(0, len(string))
    new_string = string_cut(string, i)
    return string[i] + shuffle_string_recursive(new_string)

def shuffle_string_loop(string: str) -> str:
    '''
    input: string
    return: string
    Iterative implementation to shuffle a string.
    Takes a string, returns a string.
    '''
    shuffled = ''
    for i in range(len(string)):
        j = random.randrange(0, len(string))
        shuffled = shuffled + string[j]
        string = string_cut(string, j)
    return shuffled

def string_to_list(string: str) -> list:
    '''
    input: string
    return: list
    Really simple function to turn a string into a list, because
    Python strings are immutable. Note, this isn't used anywhere.
    It's here as a reminder that since strings are not immutable,
    the cost of any function goes up * (n)
    '''
    return list(string)

def string_cut(string: str, i: int) -> str:
    '''
    input: string
    returns: string
    Make strings mutable.
    '''
    return string[:i] + string[i+1:]

def assess_shuffle(og_string: str) -> None:
    '''
    input: string
    return: None
    Calls both type of functions, and has a shitty comparison
    to see how well they shuffled the given strings.
    '''
    recu_string = shuffle_string_recursive(og_string)
    loop_string = shuffle_string_loop(og_string)
    x = y =0
    for i in enumerate(og_string):
        if og_string[i] == recu_string[i]:
            x += 1
        if og_string[i] == loop_string[i]:
            y += 1
    print(f'The original string is {og_string}')
    print(f'The recursive shuffled string is {recu_string}')
    print(f'The loop shuffled string is {loop_string}')
    print(f'{x} and {y} characters did not move')

def test_shuffle_recursive():
    '''
    input: none
    return: none
    test the recursive varient
    Just a bunch of basic tests to make sure my code has a sembelence of sanity
    '''
    string = 'abcd'
    shuffled = shuffle_string_recursive(string)
    assert shuffled != string
    assert len(shuffled) == len(string)
    assert sorted(shuffled) == sorted(string)

def test_shuffle_loop():
    '''
    input: none
    return: none
    test the iterative varient
    Just a bunch of basic tests to make sure my code has a sembelence of sanity
    '''
    string = 'abcd'
    shuffled = shuffle_string_loop(string)
    assert shuffled != string
    assert len(shuffled) == len(string)
    assert sorted(shuffled) == sorted(string)

if __name__=="__main__":
    '''Simple program to shuffle a string.''' # pylint: disable=W0105
    ogString = input("input a string: ")
    if len(ogString) == 0:
        sys.exit()
    assess_shuffle(ogString)
