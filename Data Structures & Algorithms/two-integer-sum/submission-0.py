class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = defaultdict(int)
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in ans:
                return([ans[compliment], i])
            ans[nums[i]] = i
        