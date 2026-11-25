import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based index
        result: list[str] = []

        for remaining in range(n, 0, -1):
            fact = math.factorial(remaining - 1)
            idx = k // fact
            result.append(numbers.pop(idx))
            k %= fact

        return "".join(result)