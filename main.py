import heapq
import time
def topKFrequent(nums, k):
    freq = dict()
    for num in nums:
        a = freq.get(num,0)
        print(a)
        freq[num] = a + 1
    return heapq.nlargest(k, freq.keys(), key=freq.get)

memory = {}

def climbStairs(n):
    if n < 1:
        return 0
    if n ==1:
        return 1
    if n == 2:
        return 2
    if n in memory:
        return memory[n]
    else:
        memory[n] = climbStairs(n-1) + climbStairs(n-2)
        return memory[n]

def climbstair1(n):
    if n < 1:
        return 0
    if n ==1:
        return 1
    if n == 2:
        return 2
    return climbstair1(n-1) + climbstair1(n-2)


def minimumTotal(triangle) -> int:
    if len(triangle) == 1:
        return triangle[0][0]
    i = 0
    sum = triangle[0][0]
    print(sum)
    for x in range(1, len(triangle)):
        first_ = triangle[x - 1][i] + triangle[x][i]
        second_ = triangle[x - 1][i] + triangle[x][i + 1]
        minimum = min(first_, second_)
        sum += minimum - triangle[x - 1][i]
        print(sum)
        i = i if minimum == first_ else i + 1
    print(sum)
    return sum

def longestValidParentheses(s: str) -> int:
    if len(s) == 0:
        return 0
    dp = [0] * (len(s) + 1)
    for i in range(1, len(s)):
        if s[i] == ")":
            pre = i - dp[i-1] - 1
            if pre > 0 and s[pre] == "(":
                pre = dp[pre-1] if pre > 0 else 0
                dp[i] = dp[i-1] + 2 + pre
    return max(dp)

def answer118(numRows: int):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    dp = [[1], [1, 1]]
    for height in range(2,numRows):
        length = height
        to_append = [1] * (length+1)
        for y in range(1,length):
            to_append[y] = dp[height-1][y] + dp[height-1][y-1]
        dp.append(to_append)
    return dp
if __name__ == "__main__":
    print(answer118(5))
