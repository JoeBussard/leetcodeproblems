#!/bin/python
import time

arr = []

for x in range(1, 1000):
  arr += [x]

target = 999

def binarySearch(source, target):
  L = 0
  R = len(source) - 1
  while L <= R:
    print('L', L, 'R', R)
    #time.sleep(0.01#)

    M = (R + L) // 2
    if target == source[M]: # target is M!
      return M
    #elif target == source[M+1]:
      #return M + 1
    elif target > source[M]: # target is to the right of M 
      L = M + 1
    else: # target is to the left of M.
      R = M

print(arr[binarySearch(arr, target)])


