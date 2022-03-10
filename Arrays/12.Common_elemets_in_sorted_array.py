"""
Common elements in two sorted array

ip :
A = [1,3,4,5,6,7,9]
B = [1,2,4,5,9,12]
common_ele(A,B) -> [1,4,5,9]
O(max(n,m))
"""


# 1st approach
def common_elements(list1, list2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


# 2nd approach
def common_ele(A, B):
    l = []
    for i in A:
        if i in B:
            l.append(i)
    return l


# 3rd approach
def c_e(l1, l2):
    res = []
    for item in l1:
        for item1 in l2:
            if item == item1:
                res.append(item1)
    return res


if __name__ == '__main__':
    A = [1, 3, 4, 6, 7, 9]
    B = [1, 2, 4, 5, 9, 8]
    print(common_ele(A, B))

    # NOTE: The following input values will be used for testing your solution.
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    print(common_elements(list_a1, list_a2))  # should return [1, 4, 9] (a list).
    print(c_e(list_a1, list_a2))
    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    # common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    # common_elements(list_b1, list_b2) should return [] (an empty list).
