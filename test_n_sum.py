from n_sum import two_sum, three_sum

def test_case_1():
    nums = [2,7,11,15]
    target = 9
    solution = [0,1]
    assert two_sum(nums, target) == solution

def test_case_2():
    nums = [3,2,4]
    target = 6
    solution = [1,2]
    assert two_sum(nums, target) == solution

def test_case_3():
    nums = [3,3]
    target = 6
    solution = [0,1]
    assert two_sum(nums, target) == solution

def test_three_sum_1():
    nums = [-1,0,1,2,-1,-4]
    solution = [[-1,-1,2],[-1,0,1]]
    assert three_sum(nums) == solution

def test_three_sum_2():
    nums = [0,1,1]
    solution = []
    assert three_sum(nums) == solution

def test_three_sum_3():
    nums = [0,0,0]
    solution = [0,0,0]
    assert three_sum(nums) == solution