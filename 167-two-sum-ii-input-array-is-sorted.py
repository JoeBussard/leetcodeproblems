class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(numbers) - 1
        
        while True:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1, right+1]
            if current < target:
                left += 1
            if current > target:
                right -= 1
