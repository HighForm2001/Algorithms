"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).

The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).

The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take

to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for j in range(m)] for i in range(n)]
    for x in range(n):
        dp[x][0] = 1
    for y in range(m):
        dp[0][y] = 1
    for x in range(1,n):
        for y in range(1, m):
            dp[x][y] = dp[x-1][y] + dp[x][y-1]
    return dp[n-1][m-1]


if __name__ == "__main__":
    print(uniquePaths(3, 7))