class Solution:
    def combine(self, n: int, k: int):  #-> List[List[int]]:
        self.mainList = []
        self.backtrack(n,k,1,0)
        return self.mainList

    def backtrack(self, n,k,i,j, newList=[]):
        if len(newList) == k:
            self.mainList.append(newList[:])
            return
        for i_c in range(i, n + 1):
            newList.append(i_c)
            self.backtrack(n,k,i_c+1,j+1,newList)
            newList.pop()
        return None
