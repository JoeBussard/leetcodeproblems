class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numStrMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) < 1:
            return []
        answer = []  
        numMap = numStrMap
        #print(numMap[digits[0]])
        firstMap = [a for a in numMap[digits[0]]]
        newMap = firstMap
        currMap = []
        prevMap = newMap[:]
        for x in range(1, len(digits)):
            old_nums = len(currMap)
            for element in prevMap:
                currMap += [element + char for char in numMap[digits[x]]]
            #currMap = currMap[old_nums:]
            prevMap = currMap[old_nums:]
        #print(prevMap)
        return prevMap
