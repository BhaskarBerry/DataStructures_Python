"""
Reversing an array in-place

The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be
in-place as well - so no additional memory can be used!
For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
"""
print("Reverse an array")

# One way using a built in function reverse()
a = [1, 2, 3, 4, 5]
print("Original Array:", a)
a.reverse()
print("Reversed Array:", a)


# Second way using while loop
def reverse(nums):
    # Starting position
    start_index = 0
    # index pointing to the last item
    end_index = len(nums) - 1

    while end_index > start_index:
        # Keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1


if __name__ == "__main__":
    n = [56, 2, -3, 0, 3]
    reverse(n)
    print(n)
