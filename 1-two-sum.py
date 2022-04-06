class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    bruteForce = False
    if bruteForce:
      for a in range(0, len(nums)):
        for b in range(a+1, len(nums)):
          if nums[a] + nums[b] == target:
            return [a,b]
    hashmap = False
    if hashmap:
      pairs = {}
      for i in range(0, len(nums)):
        pairs[nums[i]] = i
      for i in range(0, len(nums)):
        compliment = target - nums[i]
        if compliment in pairs:
          return [i, nums[compliment]]

    oNHashmap = True
    if oNHashmap:
      pairs = {}
      for i in range(0, len(nums)):
        pairs[nums[i]] = i
        compliment = target - nums[i]
        if compliment in pairs:
          if i == pairs[compliment]: continue
          return [i, pairs[compliment]]






    listMap = True
    if listMap:
      for x in nums:
          compliment = target - x
