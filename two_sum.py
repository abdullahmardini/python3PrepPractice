def twoSum(nums: list, target: int) -> list:
    '''
    The idea is to create a map, where I use the number
    as the key, and the index of the list as value. Then
    I check if the differnce is already stored in my map.
    '''
    num_map = {}
    for i, num in enumerate(nums):
        remainder = target - num
        pair = num_map.get(remainder,None)
        if pair is not None:
            return [pair,i]

        num_map[num] = i
    return []