class Solution:
    cache: list[int] = [-1] * 45

    def climbStairs(self, n: int) -> int:
        # See if answer for n is already in cache
        if self.cache[n - 1] != -1:
            return self.cache[n - 1]

        # Base cases
        if n == 1 or n == 2:
            self.cache[n - 1] = n
            return n

        # Inductive step
        self.cache[n - 1] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n - 1]
