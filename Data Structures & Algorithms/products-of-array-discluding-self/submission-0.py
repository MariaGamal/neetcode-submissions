class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 1)
        right = [1] * (len(nums) + 1)
        res = []
        for i in range(len(nums)):
            left[i+1] = left[i] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right[i+1] * nums[i]
        for i in range(len(nums)):
            res.append(left[i] * right[i+1])
        return res

        