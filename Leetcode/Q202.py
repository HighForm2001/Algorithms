"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay),

or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        appeared = set()
        while n > 1:
            p = 0
            while n > 0:
                p += ((n % 10) * (n % 10))
                n = int(n / 10)
            if p in appeared:
                return False
            appeared.add(p)
            n = p
        return n == 1


if __name__ == "__main__":
    print(Solution().isHappy(6))