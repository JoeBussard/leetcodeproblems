
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        wordsDict = ['x', 'y', 'z', 'x', 'y', 'a']
        
        L = -1
        R = len(wordsDict) - 1
        best = len(wordsDict)

        word_locations = [ [],[] ]

        while L < len(wordsDict) and word1 in wordsDict[L+1:]:
            L = wordsDict[L+1:].index(word1)
            word_locations[0].append(L)
        L = -1
        while L < len(wordsDict) and word2 in wordsDict[L+1:]:
            L = wordsDict[L+1:].index(word2)
            word_locations[1].append(L)

        for x in word_locations[0]:
          for y in word_locations[1]:
            if abs(x-y) < best:
              best = abs(x-y)

        print(best)
        return best


