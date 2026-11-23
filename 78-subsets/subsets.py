class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        current: list[int] = []

        def backtrack(index: int) -> None:
            if index == len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            backtrack(index + 1)
            current.pop()
            backtrack(index + 1)

        backtrack(0)
        return result