"""
ONe array roatation of another
[1,2,3,4,5,6,7] is roatation of [4,5,6,7,1,2,3]
"""
# 1st approach
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_loc = -1
    for i in range(len(list2)):
        if list2[i] == key:
            key_loc = i
            break
    if key_loc == -1:
        return False
    for i in range(len(list1)):
        j = (key_loc + i) % len(list1)
        if list1[i] != list2[j]:
            return False
    return True




if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    print(is_rotation(list1, list2a)) # is_rotation(list1, list2a) should return False.
    list2b = [4, 5, 6, 7, 1, 2, 3]
    print(is_rotation(list1, list2b))    # is_rotation(list1, list2b) should return True.
    list2c = [4, 5, 6, 9, 1, 2, 3]
    print(is_rotation(list1, list2c)) # is_rotation(list1, list2c) should return False.
    list2d = [4, 6, 5, 7, 1, 2, 3]
    print(is_rotation(list1, list2d)) # is_rotation(list1, list2d) should return False.
    list2e = [4, 5, 6, 7, 0, 2, 3]
    print(is_rotation(list1, list2e)) # is_rotation(list1, list2e) should return False.
    list2f = [1, 2, 3, 4, 5, 6, 7]
    print(is_rotation(list1, list2f)) # is_rotation(list1, list2f) should return True.
    list2g = [7, 1, 2, 3, 4, 5, 6]
    print(is_rotation(list1, list2g)) # is_rotation(list1, list2g) should return True.