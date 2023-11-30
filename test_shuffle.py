"""
test_shuffle.py
Testing module for shuffle
"""
import shuffle

def test_shuffle_recursive():
    '''
    input: none
    return: none
    test the recursive varient
    Just a bunch of basic tests to make sure my code has a sembelence of sanity
    '''
    string = 'abcd'
    shuffled = shuffle.shuffle_string_recursive(string)
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
    shuffled = shuffle.shuffle_string_loop(string)
    assert shuffled != string
    assert len(shuffled) == len(string)
    assert sorted(shuffled) == sorted(string)
