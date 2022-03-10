def naive_search(pattern, text):
    m = len(pattern)
    n = len(text)

    # this operation takes O(n) linear running time complexity
    for i in range(n - m + 1):

        # track the letters in the pattern (start 0) from left to right
        j = 0

        # all the letters of the pattern o(m) - in worst -case
        # this approach take o(n*m)
        while j < m:

            # we have to compare the characters
            if text[i + j] != pattern[j]:
                break

            # consider the next character
            j = j + 1
        if j == m:
            print("Found the match at index %s " % i)


if __name__ == '__main__':
    naive_search("text", "this is a text")
    naive_search("abc", "abcdfgdhkjfgdiuabc;labc")
