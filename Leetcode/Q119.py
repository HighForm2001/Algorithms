"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
"""


class Solution:
    def getRow(self, rowIndex: int):
        dp = [[1], [1, 1]]
        for height in range(2, rowIndex + 1):
            length = height
            to_append = [1] * (length + 1)
            for y in range(1, length):
                to_append[y] = dp[height - 1][y] + dp[height - 1][y - 1]
            dp.append(to_append)
        return dp[rowIndex]


if __name__ == "__main__":
    print(Solution().getRow(5))
