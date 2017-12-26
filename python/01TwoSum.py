class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i ,j = 0, 0
        dictionary = dict()
        
        for k in range(len(nums)):
            if not target - nums[k] in dictionary:
                dictionary[nums[k]] = k
            else:
                return [dictionary[target-nums[k]], k]
            
        return []