"""
one way strings

they  are oen away from each other if a single operation
> chnaging a characer
> Adding a character
> deleteing a character

will chnage one of the string to another

Ex:
"abcde" and "abcd  --> deleting a character
"abc" and "abd" --> chaninging a character
"abc" and  "abcd" - ->  adding  character
"abc" and "bcc"  are not one way we need two operation

"""


# --------------------------------------------------------------------------------------
# 1 way

# --------------------------------------------------------------------------------------
def is_one_away(s1, s2):
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_lengths(s1, s2)
    else:
        return is_one_away_diff_lengths(s2, s1)


def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


# Assumption: len(s1) == len(s2) + 1
def is_one_away_diff_lengths(s1, s2):
    i = 0
    count_diff = 0
    while i < len(s2):
        if s1[i + count_diff] == s2[i]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


# --------------------------------------------------------------------------------------
# 2-way approch
# --------------------------------------------------------------------------------------
def is_one_away1(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    count = 0

    if l1 == l2:
        for i in range(l1):
            if s1[i] != s2[i]:
                count += 1
        if count <= 1:
            return True
    elif l1 > l2:
        count = 0
        for i in s1:
            if i not in s2:
                count += 1
        if count == 1:
            return True
    else:
        count = 0
        for i in s2:
            if i not in s1:
                count += 1
        if count == 1:
            return True

    return False


# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
