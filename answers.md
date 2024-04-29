# CMPS 2200 Assignment 3
## Answers

**Name:** Jaimie Morris


Place all written answers from `assignment-03.md` here for easier grading.

1a) To produce as few coins as possible that sum to $N$:
1. Initialize an empty list `coins` to store the coins used.
2. Iterate through coin denominations in decreasing order (starting from the highest denomination).
3. While the remaining amount $N$ is greater than 0:
   a. If the current denomination is less than or equal to $N$, subtract it from $N$ and add it to `coins`.
   b. Otherwise, move to the next smaller denomination.
4. Return the list of coins.

1b) At each step, selecting the largest possible coin, $2^k$, denomination ensures the minimum total coins used. Optimal solutions to subproblems (smaller remaining amounts) contribute to the optimal solution for the overall problem.

1c) work and span are both O(logn)

2a) a counterexample would be to let the denominations be [4, 3, 1] and the amount be $6.
The greedy algorithm would choose [4, 1, 1] (3 coins),
but the optimal solution is [3, 3] (2 coins)

2b) The optimal solution would be to find the minimum number of coins to get $N$ dollars. For any amount $N$ and denomination list [D0, D1, ..., Dk], the optimal solution can be recursively determined by considering all choices of using or not using each denomination.

2c)  By using a bottom-up approach, it would start by initializing a table to store minimum coins for subproblems, ensuring optimal solutions to smaller subproblems are calculated first. Then, we iteratively fill in the table by considering all possible choices of using or not using each denomination for each amount, leading to the calculation of the minimum coins needed for the target amount N in DP[N][k]
Work = O(N*k), where N is the amount and k is the number of denominations and Span = O(k), as each subproblem computation depends on previous subproblems within the denomination loop.







