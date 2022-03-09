
s = 'PAYPALISHIRING'
numRows = 3

hashMap = {}
for x in len(s):
    hashMap[x] = ''

row = 0
advance = 0
while s:
    hashMap[row] += s.pop()
    if advance:
        row -= 1
    else:
        row += 1
    if row > numRows:
        advance = 1
        row -= 2
    elif row < 0:
        advance = 0
        row += 2

output = ""
for i in hashMap:
    output += hashMap[i]

    # O(n)
output = ""



for i in range(numRows):
    j = 2 * (numRows - 1)
    k = j
    output += s[i + j]
    output += s[i + j]
    j = j -2
    k = 2
    output += s[i +j]

        for i in range(numRows):
            print(output)
            n = 1
            if i == 0 or i == numRows - 1:
                j = (numRows - 1) * 2
                k = j
            else:
                j = (numRows - 1) * 2 - (2 * i)
                k = 2 * i
            while True:
                try:
                    output += s[i + j*n]
                    output += s[i + k*n]
                    n+=1
                except:
                    break


    # method 2

      output = ''
        if numRows == 1: return s
        for i in range(numRows):
            #print("outer", output)
            n = 0
            if i == 0 or i == numRows - 1:
                j = (numRows - 1) * 2 or 1
                k = j
            else:
                j = (numRows - 1) * 2 - (2 * i)
                k = 2 * i
            #print("numRows | row | offset | offset 2")
           # print(numRows , "i=", i, "j=", j, "k=", k)
            while True:
                #print("inner", output)
                try:
                    output += s[i]
                    output += s[i + j]
                    #output += s[i + k] if j is not k else ""
                    i = i + j + k

                    #
                   # output += s[i + j*n]
                 #   if j is not k:
                 #       output += s[i + k*n]
               #         i += k
                 #   n = 1
               #     i += j

                except:
                    break
        return output
