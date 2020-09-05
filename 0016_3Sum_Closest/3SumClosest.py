class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest_sum = nums[0] + nums[1] + nums[2]
        closest_dist = abs(closest_sum - target)

        nums.sort()

        for i in range(len(nums) - 2):
            fixed = nums[i]

            if i > 0 and fixed == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_dist = abs(current_sum - target)

                if current_dist < closest_dist:
                    closest_sum = current_sum
                    closest_dist = current_dist
                    if closest_dist == 0:
                        return closest_sum

                if current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest_sum