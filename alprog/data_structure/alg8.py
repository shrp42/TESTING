# < 8. Динамическое программирование >

# -------------------------
# Алгоритмы и DP
# -------------------------
class Algorithms:


# ----------------------------------------------------------------------


# -------------------------
# Fibonacci Numbers
# -------------------------
    # Recursive
    def fibonacci_recursive(self, n):
        if n <= 1:
            return n
        return self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)

    # Iterative
    def fibonacci_iterative(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

    # Memoization
    def fibonacci_memo(self, n, memo=None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = self.fibonacci_memo(n-1, memo) + self.fibonacci_memo(n-2, memo)
        return memo[n]


# ----------------------------------------------------------------------


# -------------------------
# Climbing Stairs (DP)
# -------------------------
    # Количество способов подняться на n ступеней (1 или 2 за раз)
    def climbing_stairs(self, n):
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# ----------------------------------------------------------------------


# -------------------------
# 0/1 Knapsack Problem
# -------------------------
    # weights = [w1, w2, ...], values = [v1, v2, ...], W = max weight
    def knapsack_01(self, W, weights, values):
        n = len(weights)
        dp = [[0]*(W+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for w in range(W+1):
                if weights[i-1] <= w:
                    dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][W]


# ----------------------------------------------------------------------


# -------------------------
# Maximum Sum Subarray (Kadane’s Algorithm)
# -------------------------
    def max_sum_subarray(self, nums):
        max_so_far = nums[0]
        max_ending_here = nums[0]

        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


# ----------------------------------------------------------------------


# -------------------------
# Coin Change Problem
# -------------------------
    # coins = [c1, c2, ...], amount = total
    def coin_change(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1


# ----------------------------------------------------------------------


# -------------------------
# Пример использования
# -------------------------
if __name__ == "__main__":
    algo = Algorithms()

    # Fibonacci
    n = 10
    print("Fibonacci recursive:", algo.fibonacci_recursive(n))
    print("Fibonacci iterative:", algo.fibonacci_iterative(n))
    print("Fibonacci memo     :", algo.fibonacci_memo(n))

    # Climbing Stairs
    print("Climbing stairs (10 steps):", algo.climbing_stairs(10))

    # 0/1 Knapsack
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    print("0/1 Knapsack max value:", algo.knapsack_01(W, weights, values))

    # Maximum Sum Subarray
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("Max sum subarray (Kadane):", algo.max_sum_subarray(nums))

    # Coin Change
    coins = [1,2,5]
    amount = 11
    print("Coin change min coins:", algo.coin_change(coins, amount))
