from longestsubstrworepeat import lengthOfLongestSubstring

def test_case_1():
    s = "abcabcbb"
    assert lengthOfLongestSubstring(s) == 3

def test_case_2():
    s = "bbbbb"
    assert lengthOfLongestSubstring(s) == 1

def test_case_3():
    s = "pwwkew"
    assert lengthOfLongestSubstring(s) == 3

def test_case_4():
    s = "dvdf"
    assert lengthOfLongestSubstring(s) == 3
