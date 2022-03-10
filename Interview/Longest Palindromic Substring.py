"""
Brute Force.
Approach: The simple approach is to check each substring whether the substring
 is a palindrome or not.
 To do this first, run three nested loops, the outer two  loops pick all substrings
 one by one by fixing the corner characters,
 the inner loop checks whether the picked substring is palindrome or not.

"""


# Function to print subString str[low..high]
def print_sub_str(st, low, high):
    for i in range(low, high + 1):
        print(st[i], end="")


# This function prints the longest palindrome subString
# It also returns the length of the longest palindrome
def longest_palindrome_substr(str):
    # Get length of input String
    n = len(str)

    # All subStrings of length 1
    # are palindromes
    max_length = 1
    start = 0

    # Nested loop to mark start
    # and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1

            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if str[i + k] != str[j - k]:
                    flag = 0

            # Palindrome
            if flag != 0 and (j - i + 1) > max_length:
                start = i
                max_length = j - i + 1

    print("Longest palindrome subString is: ", end="")
    print_sub_str(str, start, start + max_length - 1)

    # Return length of LPS
    return max_length


# Driver Code
if __name__ == '__main__':
    str = "forgeeksskeegfor"

    print("\nLength is: ", longest_palindrome_substr(str))
