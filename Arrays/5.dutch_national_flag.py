"""
Dutch national flag problem overview
The problem is that we want to sort a T[] one-dimensional array of integers in
O(N) running time - and without any extra memory.
The array can contain values: 0, 1 and 2.

Here to achieve this we can use sorting methods - but since it is dealing with
data structiures and memory

This should be solved using linear complexity
"""


def dutch_flag_problem(A, pivot=1):
    i = 0
    j = 0
    k = len(A) - 1

    while j <= k:
        # Current element is 0
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
            j += 1
        # Current element is 2
        elif A[j] > pivot:
            swap(A, j,k)
            k -= 1
        # Current element is 1
        else:
            j += 1

    return A


def swap(num, index1, index2):
    num[index1], num[index2] = num[index2], num[index1]


if __name__ == '__main__':
    print(dutch_flag_problem([1, 0, 2, 2, 2, 1, 1, 1, 0, 1]))

    print(dutch_flag_problem([0, 1, 0,  1, 2, 0, 2]))