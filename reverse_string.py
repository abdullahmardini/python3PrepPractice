#!/usr/bin/env python3
"""
https://interviewing.io/mocks/linked-in-java-reverse-word-in-string

Problem type
Reverse word in string

Interview question
Given a string with multiple words and spaces represented as a character array. Write an in-place algorithm to reverse the order of words in the string. Example: convert ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'] to ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']
"""

class StringReverser:
    '''
    Reverse the words of a string, but in place.
    Idea is to reverse words and then string
    '''

    def reverse_word(self, input_word: list, start: int, end: int) -> None:
        '''
        input: list
        output: None
        reverses a word
        '''
        while start < end:
            input_word[start], input_word[end] = input_word[end], input_word[start]
            start += 1
            end -= 1

    def reverse_string(self, input_string: list) -> None:
        '''
        input: list
        output: None
        reverses an entire string, finds words, and reverses them individually
        '''
        previous_space = 0
        for i, char in enumerate(input_string):
            if char == ' ':
                self.reverse_word(input_string, previous_space, i-1)
                previous_space = i+1
            elif i == len(input_string)-1:
                self.reverse_word(input_string, previous_space, i)
        input_string.reverse()


def main():
    '''
    just for some input and playing around
    '''
    str_input=input("Enter some string: ")
    if not str_input:
        return
    my_list = list(str_input)
    reverser = StringReverser()
    reverser.reverse_string(my_list)
    print(''.join(my_list))

if __name__ == "__main__":
    main()
