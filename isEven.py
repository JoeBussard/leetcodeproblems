nums = [10, 23, 1233, 12, 4, 1231]

def isEven(num):
    return not (num & 1)

for x in nums:
    print(x, "is", ("even" if isEven(x) else "odd"))
