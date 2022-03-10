"""
Trapping rain water:
Given n non-negative integers representing an elevation map where the width
of each bar is 1. Compute how much water it can trap after raining!

Here the elevation map (the input for the algorithm) is [4,1,3,1,5] and the
output is the total units of trapped rain water - which is 7.
"""


def trapping_water_problem(height):
    if len(height) < 3:
        return 0

    left_max = [0 for _ in range(len(height))]
    right_max = [0 for _ in range(len(height))]

    # dealing with left max values
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i - 1], height[i - 1])

    # dealing with right max values
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i + 1])

    # consider all the items in O(N) and sum up the trapped rain water units
    trapped = 0
    for i in range(1, len(height) - 1):
        if min(left_max[i], right_max[i]) > height[i]:
            trapped += min(left_max[i], right_max[i]) - height[i]

    return trapped


if __name__ == '__main__':
    print(trapping_water_problem([1,0,2,1,3,1,2,0,3]))
