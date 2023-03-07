"""
You are given an m x n integer matrix 'matrix' with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


class Solution:

    # general solution
    def searchMatrix(self, matrix, target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        cur_m = 0
        while cur_m < M:
            if matrix[cur_m][N - 1] < target:
                cur_m += 1
                continue
            elif matrix[cur_m][N - 1] == target:
                return True
            else:
                left, right = 0, N - 1
                while left < right:
                    print(f"cur_m:{cur_m}")
                    print(f"left:{left}")
                    print(f"right:{right}")

                    mid = left + int((right - left) / 2)
                    print(f"mid:{mid}")
                    print(f"matrix[cur_m][mid]:{matrix[cur_m][mid]}")
                    input()
                    if matrix[cur_m][mid] < target:
                        left = mid+1
                        continue
                    elif matrix[cur_m][mid] > target:
                        right = mid
                        print(f"assigned mid to right: {right}")
                        continue
                    else:
                        return True
                if left >= right:
                    break

        return False

    # solution for python only
    def pythonSolution(self, matrix, target):
        for x in range(len(matrix)):
            if target in matrix[x]:
                return True
        return False

if __name__ == "__main__":
    matrix = [[1,3,5]]
    target = 1
    print(Solution().searchMatrix(matrix, target))