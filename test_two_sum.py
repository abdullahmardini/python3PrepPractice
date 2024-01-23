from two_sum import twoSum

def test_case_1():
    nums = [2,7,11,15]
    target = 9
    solution = [0,1]
    assert twoSum(nums, target) == solution

def test_case_2():
    nums = [3,2,4]
    target = 6
    solution = [1,2]
    assert twoSum(nums, target) == solution

def test_case_3():
    nums = [3,3]
    target = 6
    solution = [0,1]
    assert twoSum(nums, target) == solution

