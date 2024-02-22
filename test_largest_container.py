from largest_container import largest_container_naive, largest_container

def test_1():
    assert largest_container_naive([1,1]) == 1
    assert largest_container([1,1]) == 1

def test_2():
    container = [1,8,6,2,5,4,8,3,7]
    assert largest_container_naive(container) == 49
    assert largest_container(container) == 49

def test_3():
    container = [1000000,1000002,1,8,6,2,5,4,8,3,7]
    assert largest_container_naive(container) == 1000000
    assert largest_container(container) == 1000000