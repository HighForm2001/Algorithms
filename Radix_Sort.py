import math

import tester


def radixSort(arr):
    if not arr or len(arr) < 2:
        return
    process(arr, 0, len(arr) - 1, maxBits(arr))


def maxBits(arr):
    max_ = float('-inf')
    for i in range(0, len(arr)):
        max_ = max(max_, arr[i])
    res = 0
    while max_ > 0:
        res += 1
        max_ /= 10
        max_ = int(max_)
    return res


# def process(arr, L, R, digit):
#     radix = 10
#     bucket = [0] * (R - L + 1)
#     for d in range(1, digit+1):
#         count = [0] * radix
#         i = L
#         while i <= R:
#             j = getDigit(arr[i], d)
#             count[j] += 1
#             i += 1
#         i = 1
#         while i < radix:
#             count[i] = count[i] + count[i - 1]
#             i += 1
#         i = R
#         while i >= L:
#             j = getDigit(arr[i], d)
#             bucket[count[j] - 1] = arr[i]
#             count[j] -= 1
#             i -= 1
#         i = L
#         j = 0
#         while i <= R:
#             arr[i] = bucket[j]
#             i += 1
#             j += 1

def process(arr, L, R, digit):
    radix = 10
    bucket = [0] * (R-L + 1)
    for d in range(1, digit + 1):
        count = [0] * radix
        i = L
        while i <= R:
            j = getDigit(arr[i],d)
            count[j] += 1
            i += 1
        i = 1
        while i < radix:
            count[i] = count[i] + count[i-1]
            i += 1
        i = R
        while i >= L:
            j = getDigit(arr[i],d)
            bucket[count[j]-1] = arr[i]
            count[j] -= 1
            i -= 1
        i,j = L,0
        while i <= R:
            arr[i] = bucket[j]
            i += 1
            j += 1

def getDigit(x, d):
    return int(x / int(math.pow(10, d - 1)) % 10)

if __name__ == "__main__":
    test = tester.random_number_generator(20,1000)
    test_2 = test.copy()
    print(test)
    radixSort(test)
    test_2.sort()
    print(test)
    print(test_2)