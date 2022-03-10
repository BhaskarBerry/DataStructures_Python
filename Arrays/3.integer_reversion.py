"""
Our task is to design an efficient algorithm to reverse a given integer.
For example if the input of the algorithm is 1234 then the output should be 4321.
"""


# Converting number to string and reversing
def reverse_integer(data):
    a = list(str(data))
    print(a)
    # starting index
    start_index = 0
    # ending index
    end_index = len(a) - 1

    while end_index > start_index:
        a[end_index], a[start_index] = a[start_index], a[end_index]
        start_index += 1
        end_index -= 1

    return ''.join(a)


# Second and correct way to reverse numbers
def revese_numbers(data):
    reversed_integer = 0

    while data > 0:
        remainder = data % 10
        reversed_integer = reversed_integer * 10 + remainder
        data = data // 10

    return reversed_integer


if __name__ == '__main__':
    print(int(reverse_integer(102)))
    print(revese_numbers(103))
