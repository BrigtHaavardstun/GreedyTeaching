# This file will binary search for the Minimum Saturating Number
import random
import can_we_find_a_full_matching

RADNOM_INT = random.randint(0, 100)
print(RADNOM_INT)


def value_high_enough(x):
    """
    Evaluate the function at a given point
    """

    return can_we_find_a_full_matching.check(x)


def binary_search():
    """
    arr: Sorted list of eligable indexes to evaluate
    """
    left = 0
    right = 1
    # find right
    while not value_high_enough(right):
        right *= 2

    while left <= right:
        mid = left + (right - left) // 2
        print(mid)

        if mid == left:
            break
        # If target is smaller, ignore the right half
        elif value_high_enough(mid):
            right = mid

        # If target is greater, ignore the left half
        else:
            left = mid+1

    return left


binary_search()
