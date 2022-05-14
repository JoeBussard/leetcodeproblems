# find all positive integer solutions under 1,000 to a^3 * b^3 = c^3 * d^3

# brute brute brute force
from collections import defaultdict
a,b,c,d = 1,1,1,1
solutions = set()
solutions.add((1,1,1,1))
#solutions = defaultdict(set)
num_solutions = 1

for i in range(1,1):
  a = i
  for j in range(1,10):
    b = j
    for k in range(1,10):# 1,000,000,000,000
      c = k
      for l in range(1,10):
        d = l
        if a**3 + b**3 == c**3 + d**3:
          solutions.add((a,b,c,d))

#print(sorted(solutions))

# 1, 2, 1, 2
# 2, 1, 2, 1

a = [x for x in range(1,1000)]
b = [x for x in range(1,1000)]

solutions2 = set()

for i in range(1,1000):
  for j in range(1,1000):
    solutions2.add((i,j,i,j))
    solutions2.add((j,i,j,i))
    solutions2.add((i,j,j,i))
    solutions2.add((j,i,i,j))

    

print(solutions2)
