#
# def minimum_swaps(arr):
#     count = 0
#     i = 0
#     while i < len(arr):
#         print(arr[i], i+1)
#         if arr[i] != i + 1:
#             print("Inner")
#             print(arr[i], i + 1)
#             while arr[i] != i + 1:
#                 temp = 0
#
#                 # Swap current element with correct position of that element
#                 temp = arr[arr[i] - 1]
#                 arr[arr[i] - 1] = arr[i]
#                 arr[i] = temp
#                 count += 1
#         print(count)
#         # Increment for next index, current element is at  correct position
#         i += 1
#
#     return count
#
#
# if __name__ == '__main__':
#     arr = [4, 1, 2, 3, 4];
#     # Function to find minimum swaps
#     print(minimum_swaps(arr))

def end_sort_steps(lst):
    steps = 0
    right_min = max(lst)

    for n in reversed(lst):
        if n >= right_min:
            # Then the number must be moved
            steps += 1
        else:
            # Otherwise it is the smallest number seen yet
            right_min = n

    return steps

print(end_sort_steps([4,1,2,4,3])) # [3, 4, 5]