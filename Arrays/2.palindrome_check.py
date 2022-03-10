"""
"A palindrome is a string that reads the same forward and backward"
For example: radar or madam

Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!
"""


# =========One way=========
def palindrome_check(value):
    a = value
    b = value[::-1]
    print("the original string ", a)
    print("the reversed  string ", b)
    if a == b:
        return "Palindrome"
    else:
        return "Not Palindrome"


# =========Second way=========
def palindrome(value):
    stringlength = len(value) - 1
    for i in range(stringlength):
        if value[i] != value[stringlength - i]:
            return "Not Palindrome"
        else:
            return "Palindrome"


# =========Third Way=========
def is_palindrome(s):
    original_string = s
    reverse_string = reverse(s)
    # print("the original string ", original_string)
    # print("the reversed  string ", reverse_string)
    if original_string == reverse_string:
        return "Plaindrome"
    else:
        return "Not Palindrome"


# O(N) Linear running time where N is the number  of letters in a string s N= len(s)
def reverse(data):
    # String into list of  characters
    data = list(data)
    # Starting position
    start_index = 0
    # index pointing to the last item
    end_index = len(data) - 1

    while end_index > start_index:
        # Keep swapping the items
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    return ''.join(data)


if __name__ == '__main__':
    a = "MaMa"
    result = palindrome_check(a)
    resu1t1 = palindrome(a)
    print(is_palindrome(a))
    print(result)
    print(resu1t1)
