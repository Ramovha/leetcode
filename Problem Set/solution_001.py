class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        
        num = {}        
        for index, val in enumerate(nums):
            if target - val in num:
                return num[target - val], index
            num[val] = index