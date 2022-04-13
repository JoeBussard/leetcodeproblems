class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        wordsDict = ['x', 'y', 'z', 'x', 'y', 'a']
        
        L = 0
        R = len(wordsDict) - 1
        best = len(wordsDict)
        
        word1 = 'x'
        word2 = 'a'
        
        while L < R:  
            if wordsDict[L] == word1 and wordsDict[R] == word2:
                distance = R - L
                if distance < best:
                    best = distance
            elif wordsDict[L] == word2 and wordsDict[R] == word1:
                distance = R - L
                if distance < best:
                    best = distance
            if wordsDict[L] == word1 and word1 in wordsDict[L:]:
                L += 1
                continue
            if wordsDict[L] == word2 and word2 in wordsDict[L:]:
                L += 1
                continue
            if wordsDict[R] == word1 and word1 in wordsDict[:R]:
                R -= 1
                continue
            if wordsDict[R] == word2 and word2 in wordsDict[:R]:
                R -= 1
                continue
            vkkkk
        
        return best
    
    
     
            
    
