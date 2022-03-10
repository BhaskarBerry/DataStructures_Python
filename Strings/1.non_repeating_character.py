"""
Non repeating character
ip:  aabcb --> c
ip: xxyz --> y

"""


# --------------------------------------------------------------------------------------
# 1st approach
# --------------------------------------------------------------------------------------
def non_repeating(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    # print(d)
    for key, value in d.items():
        # print(key, value)
        if value == 1:
            return key

    return None


# --------------------------------------------------------------------------------------
# -2nd approach
# --------------------------------------------------------------------------------------
def non_repeating2(given_string):
    char_count = {}
    for c in given_string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in given_string:
        if char_count[c] == 1:
            return c
    return None


#
# a = input("Enter the inpt string : ")
# print(non_repeating(a))

print(non_repeating("abcab"))  # should return 'c'
print(non_repeating("abab"))  # should return None
print(non_repeating("aabbbc"))  # should return 'c'
print(non_repeating("aabbdbc"))  # should return 'd'
