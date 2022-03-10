"""
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once"

For example: restful and fluster
"""


# ---One way---
def anagram_check(s1, s2):
    first_string = list(s1)
    second_string = list(s2)

    if len(first_string) == len(second_string):
        for i in range(len(first_string)):
            if first_string[i] in second_string:
                pass
            else:
                return "Not Anagram"
        return "Anagram"
    else:
        return "Not Anagram"


# -- Second way --
def is_anagram(s1, s2):
    # if the length of strings differ - they are not anagram
    if len(s1) != len(s2):
        return False

    # we have to sort the letters in each strings & compare the letters with the same indexes
    # This is the bottleneck becasue it has O(NLogN)
    s1 = sorted(s1)
    s2 = sorted(s2)
    print(s1)
    # O(N) Running time
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    # over all running time O(NLogN) + O(N) = O(NlogN)
    return True


if __name__ == '__main__':
    print(anagram_check("Mom", "moM"))
    print("Second Way : ", is_anagram("Red", "deR"))
