"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
"""
class Solution:
    def generate(self, numRows: int):
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
    print(Solution().generate(5))