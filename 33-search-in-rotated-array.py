#!/bin/python
import time

arr = []

for x in range(1, 100):
  arr += [x]

temp = arr[:30]
arr = arr[30:]
arr += temp
print(arr)

target = 32
print('cheating', target, 'is at', arr.index(target))
print(arr[49:51])

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        source = nums
        R = len(source) - 1
        while L <= R:
          #time.sleep(0.5)

            M = (R + L) // 2
            print('L', L, 'R', R, 'aM', source[M])
            if target == source[M]: # target is M!
                return M
                                 #elif target == source[M+1]:
                                #return M + 1
            elif target > source[M]: # target is to the right of M 
                L = M + 1
            else: # target is to the left of M.
                if source[M] < source[R]:
                    R = M
                else:
                    print("Something fishy!")
                    if target > source[L]:
                        print("Something very fishy...")
                        R = M
                    else:
                        L = M + 1
        return -1






def binarySearch(source, target):
  L = 0
  R = len(source) - 1
  while L <= R:
    time.sleep(0.5)

    M = (R + L) // 2
    print('L', L, 'R', R, 'aM', source[M])
    if target == source[M]: # target is M!
      return M
                                 #elif target == source[M+1]:
                                #return M + 1
    elif target > source[M]: # target is to the right of M 
        L = M + 1
    else: # target is to the left of M.
      if source[M] < source[R]:
        R = M
      else:
        print("Something fishy!")
        if target > source[L]:
          print("Something very fishy...")
          R = M
        else:
          L = M + 1

#print(arr[binarySearch(arr, target)])


