class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution_dict = {}
        for i, value in enumerate(nums):
            if (target - value) in solution_dict:
                return [i, solution_dict[target - value]]
            else:
                solution_dict[value] = i
