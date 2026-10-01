class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = 0
        for i in range(len(nums)):
            num1 = i
            for j in range(len(nums)):
                num2 = j
                if (num1 != num2 and (nums[num1] + nums[num2] == target)):
                    return [num1, num2]
        