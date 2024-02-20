def longest_palindrome(s: str) -> str:
    '''
    So palindromes have two funny properties:
    1. They are symmetrical
    2. If len(palindrome) % 2 >= 1, then fundamentally, the
    palindrome contains another palindrome. (yo dawg I heard...)
    So for example: aba. 3%1 == 1, so true. And it contains b, which is a palindrome.
    So it has b, and a on either side.

    What we want to do is crawl through the string, and look for palindromes, storing the radius and center along the way. Finally, when the radius reaches the end of the string, we have effectively parsed through the entire string, and are done.

    This is not Manacher's algorithm. But if you understand the gist of it, you're about 75% of the way there.
    '''
    # Add '|' to every string, to make them all odd.
    # 'aba' becomes 'a|b|a' (3->5), 'abba' becomes 'a|b|b|a' (4->7)
    if s == '':
        return ''

    mod_s = '#'.join(s)

    center = 0
    pal_rad = [0 for _ in enumerate(mod_s)]

    while center < len(mod_s):
        radius = 0
        while center - (radius + 1) >= 0 and \
            center + (radius + 1) < len(mod_s) and \
            mod_s[center - (radius + 1)] == mod_s[center + (radius + 1)]:
                radius +=1
        pal_rad[center] = radius
        center +=1

    max_r = max(pal_rad)
    max_c = [x for x, r in enumerate(pal_rad) if r == max_r]
    strings = []


    for x in max_c:
        strings.append(mod_s[x-max_r:x+max_r+1].replace('#', ''))

    print(mod_s)
    print(pal_rad)
    print(strings)
    return(max(strings, key=len))


def is_palindrome_test(s: str) -> bool:
    '''
    Simple palindrome test. Take advantage of symmetry, and
    strings indexes in python3. Work outside to the center.
    This will not be used in the solution, but knowing this
    property will make the actual solution easier to follow.
    Fun fact: in the case 'abba', this will test if b==b, but
    in 'abcba', this does not test if c==c, because who cares?
    '''
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


def is_palindrome(s:str) -> bool:
    '''
    Same idea, but this time we're going to from inside out.
    '''
    mid = len(s)//2
    left = mid - 1
    right = mid
    # Skip right a character if the length is odd. We won't compare
    # a character to itself.
    if len(s) % 2:
        right = mid + 1

    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            return False
        left -= 1
        right += 1
    return True

if __name__ == '__main__':
    print(longest_palindrome('aacdefcaa'))
