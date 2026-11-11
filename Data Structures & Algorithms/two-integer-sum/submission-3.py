class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            numToIndex[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]
            if x in numToIndex and numToIndex[x] != i:
                return [i, numToIndex[x]]
        