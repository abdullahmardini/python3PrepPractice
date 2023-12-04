"""
test_most_common_integer.py
"""

from most_common_integer import CountInteger

def test_empty():
    '''
    what happens when i give it an empty list
    '''
    mci = CountInteger()
    empty_list = []
    assert mci.build_map(empty_list) == {}


def test_single():
    '''
    single item?
    '''
    mci = CountInteger()
    single_list = [1]
    assert mci.build_map(single_list) == {1: 1}

def test_tie():
    '''
    let's give it a tie
    '''
    mci = CountInteger()
    tie_list = [1, 2]
    assert mci.build_map(tie_list) == {1: 1, 2: 1}

def test_obvious():
    '''
    make sure that it even works
    '''
    mci = CountInteger()
    my_list = [1, 1, 1, 1, 1, 2, 3]
    assert mci.build_map(my_list) == {1: 5, 2: 1, 3: 1}

def test_strings():
    '''
    Hey I should be able to pass strings into this, right?
    '''
    mci = CountInteger()
    str_list = ['a', 'a', 'b']
    assert mci.build_map(str_list) == {'a': 2, 'b': 1}

def test_list_function():
    '''
    make sure that list actually does the thing
    '''
    mci = CountInteger()
    mylist = mci.give_unsorted_list(10)
    assert len(mylist) == 10
