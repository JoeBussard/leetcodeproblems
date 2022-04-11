class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        winners = []
        for target in range(0, len(nums)):
            pairs = {}
            for i in range(0, len(nums)):
                pairs[nums[i]] = i
            for i in range(0, len(nums)):
                compliment = 0 - nums[target] - nums[i]
                if compliment in pairs:
                    if i == pairs[compliment]: 
                        continue
                    if target == i:
                        continue
                    if pairs[compliment] == target:
                        continue
                    winners.append([nums[target], nums[i], nums[pairs[compliment]]])
        for x in winners:
            x.sort()
        trumales = []
        for x in winners:
            if x not in trumales:
                trumales.append(x)
        return trumales

class Solution2(object):
    def threeSum(self, nums):
      if len(nums) < 3:
        return []
      for i in range(0, len(nums)):
        pairs[nums[i]] = i
      triplets = {}
      for i in range(0, len(nums)):
        compliment = 0 - nums[i]
        if compliment in pairs:
          triplets[
              for i in range(0, len(nums)):
        triplement = nums[i] - triplets[i]
        if triplement = 0:
          if triplement[
