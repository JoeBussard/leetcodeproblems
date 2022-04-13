
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        best = len(wordsDict)
        i1 = -1
        i2 = -1

        for i in range(len(wordsDict)):
            print(i1, i2)
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            if i1 > -1 and i2 > -1 :
                print("Found word 1 and word2 at", i1, i2)
                distance = abs(i1-i2)
                if distance < best:
                    best = distance

        print(best)
        return best
              



       
