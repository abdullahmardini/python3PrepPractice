from longest_palindrome import longest_palindrome, is_palindrome, is_palindrome_test

def test_case_1():
    s = 'abad'
    assert longest_palindrome(s) == 'aba'

def test_case_2():
    s = 'banana'
    assert longest_palindrome(s) == 'anana'

def test_case_3():
    s = 'cbbd'
    assert longest_palindrome(s) == 'bb'

def test_case_4():
    s = 'babad'
    outputs = ['bab', 'aba']
    assert longest_palindrome(s) in outputs

def test_case_5():
    s = 'ccd'
    assert longest_palindrome(s) == 'cc'

def test_case_6():
    s = 'bcc'
    assert longest_palindrome(s) == 'cc'

def test_case_7():
    s = ''
    assert longest_palindrome(s) == ''

def test_case_8():
    s = 'aacdefcaa'
    assert longest_palindrome(s) == 'aa'

def test_palindrome_1():
    s = 'abad'
    assert is_palindrome(s) is False
    assert is_palindrome_test(s) is False

def test_palindrome_2():
    s = 'abba'
    assert is_palindrome(s) is True
    assert is_palindrome_test(s) is True

def test_palindrome_3():
    s = 'abbac'
    assert is_palindrome(s) is False
    assert is_palindrome_test(s) is False

def test_palindrome_4():
    s = 'abcba'
    assert is_palindrome(s) is True
    assert is_palindrome_test(s) is True

def test_palindrome_5():
    s = 'dbcba'
    assert is_palindrome(s) is False
    assert is_palindrome_test(s) is False
