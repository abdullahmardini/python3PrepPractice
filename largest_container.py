def largest_container(container: list) -> list:
    '''
    start with a window of the entire container. move inward until you meet in
    the middle.

    we want to exploit the fact that the largest will essentially cut the box in
    half. then it's a question of figuring out how to increment inwards to cut
    out that box
    '''
    max_area = 0

    left = 0
    right = len(container) - 1

    while right > left:
        left_height = container[left]
        right_height = container[right]
        width = right - left
        height = min(left_height, right_height)
        volume = width * height
        if volume > max_area:
            print(f"{left}->{left_height} {right}->{right_height}")
            max_area = volume
        if left_height < right_height:
            left += 1
        else:  # right_height {<,==} left_height
            right -= 1

    return max_area

def largest_container_naive(container: list) -> list:
    '''
    simple brute force solution
    '''
    max_area = 0

    for left, left_height in enumerate(container):
        for right, right_height in enumerate(container):
            width = right - left
            height = min(left_height, right_height)
            volume = width * height
            if volume > max_area:
                print(f"{left}->{left_height} {right}->{right_height}")
                max_area = volume

    return max_area