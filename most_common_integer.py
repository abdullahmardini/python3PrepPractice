"""
I'm just trying to solve the most common integer problem
"""
import random
from operator import itemgetter

class CountInteger:
    """
    Given a list of ints, it will put them in a hash map,
    and return the most common seen integer.
    Actually this be generic enough to work on anything
    """
    def __init__(self):
        self.sorted_map = {}

    def build_map(self, input_list: list) -> dict:
        '''
        input: list
        return: dict
        Given a list of some stuff, will return a dict containing
        each item, and how frequently it appears
        '''
        counted_map = {}
        for i in input_list:
            print(type(input_list))
            print(type(i))
            print(i)
            if i in counted_map:
                counted_map[i] += 1
            else:
                counted_map[i] = 1
        self.sorted_map = dict(sorted(counted_map.items(), key=itemgetter(1), reverse=True))
        return self.sorted_map

    def give_unsorted_list(self, length: int) -> list:
        '''
        input: int
        return: list
        If you don't want to provide a list, I can do that for you.
        '''
        return [random.randint(0,9) for i in range(length)]

if __name__ == '__main__':
    counter_thing = CountInteger()
    mylist = counter_thing.give_unsorted_list(20)
    mymap = counter_thing.build_map(mylist)
    print(mymap)