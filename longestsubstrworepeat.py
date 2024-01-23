def lengthOfLongestSubstring(s: str) -> int:
    '''
    longest substring without repeating characters problem from leet
    The idea to create a sliding window, and track the length of the longest
    substring so far. If I see a repeating character, I chop the substr at that
    character, only keep the rest. We do the comparison at the beginning to
    ensure the length is only recorded after a character is added.
    I could probably use a map or something, or keep track of the longest
    substring and return that.
    input: string
    return: int
    '''
    substr = ''
    length = 0
    for _, letter in enumerate(s):
        if letter in substr:
            temp = substr.split(letter)[1]
            substr = ''.join(temp)
        substr += letter
        length = len(substr) if len(substr) > length else length
    return length