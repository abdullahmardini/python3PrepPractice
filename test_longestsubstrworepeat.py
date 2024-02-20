from longestsubstrworepeat import length_of_longest_substring

def test_case_1():
    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3

def test_case_2():
    s = "bbbbb"
    assert length_of_longest_substring(s) == 1

def test_case_3():
    s = "pwwkew"
    assert length_of_longest_substring(s) == 3

def test_case_4():
    s = "dvdf"
    assert length_of_longest_substring(s) == 3
