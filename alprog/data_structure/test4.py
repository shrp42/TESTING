# LESSON 8
# print("final")

# class Algorithms:
#
#     def fin_recursive(self, n):
#         if n <= 1:
#             return n
#
#         return self.fin_recursive(n-1) + self.fin_recursive(n-2)
#
#     def fin_iterative(self, n):
#         if n <= 1:
#             return n
#
#         a, b = 0, 1
#
#         for _ in range(2, n+1):
#             a, b = b, a + b
#         return b
#
#     def fin_memo(self, n, memo=None):
#         if memo is None:
#             memo = {}
#
#         if n in memo:
#             return memo[n]
#
#         if n <= 1:
#             memo[n] = n
#
#         else:
#             memo[n] = self.fin_memo(n-1, memo) + self.fin_memo(n-2, memo)
#         return memo[n]
#
#     def fib_fast(self, n):
#         def helper(n):
#             if n == 0:
#                 return (0, 1)
#
#             a, b = helper(n // 2)
#             c = a * (2 * b - a)
#             d = a * a + b * b
#
#             if n % 2 == 0:
#                 return (c, d)
#             else:
#                 return (d, c + d)
#
#         return helper(n)[0]
#
# if __name__ == "__main__":
#     algo = Algorithms()

    # Fibonacci
    # n = 9999
    # print("Fibonacci recursive:", algo.fib_fast(n))
    # print("Fibonacci iterative:", algo.fin_iterative(n))
    # print("Fibonacci memo     :", algo.fin_memo(n))
    # 0 1 1 2 3 5 8 13 21 34 55 89 144



class Algorithms:

    def fin_recursive(self, n):
        if n <= 1:
            return n

        return self.fin_recursive(n-1) + self.fin_recursive(n-2)


    def fin_iterative(self, n):
        if n <= 1:
            return n

        a, b = 1, 2

        for _ in range(2, n+1):
            a, b = b, a+b

        return b


    def fin_memo(self, n, memo=None):
        if memo is None:
            memo = {}

        if n in memo:
            return memp[n]

        if n <= 1:
            memo[n] = n

        else:
            memo[n] = self.fin_memo(n-1, memo) + self.fin_memo(n-2, memo)

        return memo[n]



    def climbing_stairs(self, n):
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]



# def backpack(self, W, weights, values):
#     n = len(weights)
#         dp = [[0] * (W+1) for _ in range(n+1)]
#
#         for i in range(1, n+1):
#             for w in range(W+1):
#                 if weights[i-1] <= w:
#                     dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
#                 else:
#                     dp[i][w] = dp[i-1][w]
#
#         print("DP Table:")
#         for row in dp:
#             print(row)
#
#         return dp[n][W]
#
#
# algo = Algorithms()
# weights = [1, 2, 3]
# values = [6, 10, 12]
# W = 5
#
# max_value = algo.backpack(W, weights, values)
# print("\nМаксимальная ценность рюкзака:", max_value)



    def backpack(self, W, weights, values):
        n = len(weights)
        dp = [[0] * (W+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for w in range(W+1):
                if weights[i-1] <= w:
                    dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]

        return dp[n][W]



    def max_subarray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        current_nums = nums[0]
        max_nums = nums[0]

        for num in nums[1:]:
            current_nums = max(num, current_nums + num)
            max_nums = max(max_nums, current_nums)

        return max_nums

# lag = Algorithms()
# nums = [1,2,33,4,-45,64,6,6,-34623,25,1]
# print(lag.max_subarray(nums))



    def coin(self, coins, amount):
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float("inf") else -1

algo = Algorithms()
coins = [1, 2, 5]
amount = 1136
print(algo.coin(coins, amount))