"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase.

Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor."""


def minCostClimbingStairs(cost) -> int:
    first = cost[0]
    second = cost[1]
    if len(cost) == 2:
        return min(first,second)
    for i in range(2, len(cost)):
        curr = cost[i] + min(first, second)
        first = second
        second = curr
    return min(first,second)



if __name__ == "__main__":
    test_case = [1, 2, 2, 2]
    print(test_case)
    print(minCostClimbingStairs(test_case))
