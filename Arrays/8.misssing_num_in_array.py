"""
Missing number in an array
"""


def missing_number(a):
    for i in range(10):
        if i not in a:
            print(i)


if __name__ == '__main__':
    array_num = [1, 4, 5, 6, 7, 3, 9]
    missing_number(array_num)
