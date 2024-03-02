def twoSum(nums: list, target: int) -> list:
    '''
    The idea is to create a map, where I use the number
    as the key, and the index of the list as value. Then
    I check if the difference is already stored in my map.
    '''
    num_map = {}
    for i, num in enumerate(nums):
        remainder = target - num
        pair = num_map.get(remainder,None)
        if pair is not None:
            return [pair,i]

        num_map[num] = i
    return []


def threeSum(nums: list) -> list:
    target = 0
    pairs = []
    for i, num in enumerate(nums):
        remainder = target - num
        pair = twoSum(nums[:i]+nums[i+1:], target-remainder)

        if pair:
            pairs += [[num] + pair]
    return pairs