class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        matches = []

        if len(nums) < 3:
            return matches

        nums.sort()

        for i in range(len(nums) - 2):
            fixed = nums[i]
            if i > 0 and fixed == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_result = nums[i] + nums[left] + nums[right]

                if sum_result == 0:
                    matches.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif sum_result > 0:
                    right -= 1

                else:
                    left += 1

        return matches