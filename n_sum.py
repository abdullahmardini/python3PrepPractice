'''
2sum, 3sum, etc
leetcode problem
you know, it's probably possible to make a real nsum function that just keeps calling itself
chatgpt hlp plz
'''

def two_sum(nums: list, target: int) -> list:
    '''
    The idea is to create a map, where I use the number
    as the key, and the index of the list as value. Then
    I check if the difference is already stored in my map.
    returns: list of indexes
    '''
    num_map = {}
    for i, num in enumerate(nums):
        remainder = target - num
        pair = num_map.get(remainder,None)
        if pair is not None:
            return [pair,i]

        num_map[num] = i
    return []


def three_sum(nums: list) -> list:
    '''
    Going to try to reduce the problem to a 2sum problem.
    also lol
    returns: list of list of values
    '''
    target = 0
    pairs = []
    for i, num in enumerate(nums):
        remainder = target - num
        tmp_list = nums[:i]+nums[i+1:]
        pair_idx = two_sum(nums[:i]+nums[i+1:], target-remainder)
        pair = [tmp_list[x] for x in pair_idx]

        if pair:
            pairs += [[num] + pair]
    return pairs

if __name__=='__main__':
    numbs = [0,0,0]
    print(three_sum(numbs))