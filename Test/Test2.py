def smallest_divisor(n):
    # if divisible by 2
    if n % 2 == 0:
        return 2;

    # iterate from 3 to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2

    return n


def solution(data):
    count = 0
    for i in range(1, len(data) - 1):
        # print("S, ", smallest_divisor(data[i]), smallest_divisor(data[i + 1]))
        if smallest_divisor(data[i]) == smallest_divisor(data[i + 1]):
            data[i], data[i + 1] = data[i + 1], data[i]
            count = count + 1

    return count


if __name__ == '__main__':
    a = [4, 1, 2, 4, 3]
    print(solution(a))
