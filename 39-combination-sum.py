class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import heapq
        combos = set()
        working_area = []
        heapq.heapify(working_area)
        candidates = candidates[::-1]
        
        def backtrack(c, t):
            nonlocal working_area
            print("Backtrack. C", c, "T", t)
            
            if t % c[0] == 0:
                print("Found a solution")
                n = t // c[0]
                print("Appending", n, "c[0]'s")
                for i in range(n):
                    heapq.heappush(working_area, c[0])
                
                print("Adding", working_area, "to combo list")
                combos.add(tuple(working_area))
                for i in range(n):
                    heapq.heappop(working_area)
            else:
                print("Solution not found yet")
            if len(c) <= 1:
                return
            else:
                print("Fixing", c[0])
                heapq.heappush(working_area, c[0])
                if t - c[0] > 0:
                    print("Trying again with w_a", working_area, "t=", t - c[0], "c=", c[1:])
                    backtrack(c[1:], t - c[0])
                heapq.heappop(working_area)
                
        for i in range(len(candidates)):
            backtrack(candidates[i:], target)
        print(working_area)
        print(combos)
                


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import heapq
        combos = set()
        working_area = []
        
        def backtrack(c, t):
            nonlocal working_area
            print("Backtrack. C", c, "T", t)
            if t % c[0] == 0:
                print("Found a solution")
                n = t // c[0]
                print("Appending", n, "c[0]'s")
                for i in range(n):
                    working_area.append(c[0])
                
                print("Adding", working_area, "to combo list")
                combos.add(tuple(sorted(working_area)))
                for i in range(n):
                    working_area.pop(-1)
            else:
                print("Solution not found yet")
            
            for i in range(len(c)-1):
                print("Fixing", c[i])
                working_area.append(c[i])
                if t - c[i] > 0:
                    print("Trying again with w_a", working_area, "t=", t - c[i], "c=", c[i+1:])
                    backtrack(c[i+1:], t - c[i])
                working_area.pop(-1)
                print("Trying again with just", working_area, "t=", t, "c=", c[i+1:])
                backtrack(c[i+1:], t)                
        backtrack(candidates, target)              
#        for i in range(len(candidates)):
 #           backtrack(candidates[i:], target)
        print(working_area)
        print(combos)



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import heapq
        combos = set()
        working_area = []
        
        def backtrack(c, t):
            nonlocal working_area
        #    print("Backtrack. C", c, "T", t)
            if len(c) < 1: return
            for x in range(len(c)):
                if t % c[x] == 0:
               #     print("Found a solution")
                    n = t // c[x]
               #     print("Appending", n, "c[x]'s")
                    for i in range(n):
                        working_area.append(c[x])

              #      print("Adding", working_area, "to combo list")
                    combos.add(tuple(sorted(working_area)))
                    for i in range(n):
                        working_area.pop(-1)
                else:
                    pass #rint("Solution not found yet")
            
            for i in range(len(c)):
                #print("Pinning", c[i])
                for j in range(1,t // c[i]):
                    #working_area.append(c[i])
                    working_area += [c[i]] * j
                    if t - c[i] > 0:
                 #       print("Pin", c[i], "look at combos to the right...", working_area, "t=", t - c[i] * j, "c=", c[i+1:])
                        backtrack(c[i+1:], t - c[i] * j)
                #        print("Pin", c[i], "look at combos to the left", working_area, "t=", t - c[i] * j, "c=", c[:i])
                        backtrack(c[:i], t - c[i] * j)                    
                    
                    #working_area.pop(-1)
                    working_area = working_area[:-j]
                    
                #    print("Start with", working_area, "Combos to the right." "t=", t, "c=", c[i+1:])
                    backtrack(c[i+1:], t)   
                
                #working_area.append(c[i])
                #print("Start with", working_area, "Combos to the left.", "t=", t, "c=", c[:i])
                #backtrack(c[:i], t - c[i])      
                #working_area.pop(-1)
                
                
        backtrack(candidates, target)              
#        for i in range(len(candidates)):
 #           backtrack(candidates[i:], target)
       # print(working_area)
       # print(combos)
        finished_list = []
        return list(combos)
    
                class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import heapq
        combos = set()
        working_area = []
        candidates = sorted(candidates)
        def backtrack(c, t):
            nonlocal working_area
        #    print("Backtrack. C", c, "T", t)
            if len(c) < 1: return
            for x in range(len(c)):
                if t < c[x]: break
                if t % c[x] == 0:
               #     print("Found a solution")
                    n = t // c[x]
               #     print("Appending", n, "c[x]'s")
                    for i in range(n):
                        working_area.append(c[x])

              #      print("Adding", working_area, "to combo list")
                    combos.add(tuple(sorted(working_area)))
                    for i in range(n):
                        working_area.pop(-1)
                else:
                    pass #rint("Solution not found yet")
            
            for i in range(len(c)):
                #print("Pinning", c[i])
                for j in range(1,t // c[i]):
                    #working_area.append(c[i])
                    working_area += [c[i]] * j
                   # if sum(working_area) > t:
                    #    working_area = working_area[:-j]
                        #continue
                    if t - c[i]*j > 0:
                 #       print("Pin", c[i], "look at combos to the right...", working_area, "t=", t - c[i] * j, "c=", c[i+1:])
                     #   backtrack(c, t-c[i] * j)
                        backtrack(c[i+1:], t - c[i] * j)
                #        print("Pin", c[i], "look at combos to the left", working_area, "t=", t - c[i] * j, "c=", c[:i])
                #        backtrack(c[:i], t - c[i] * j)                    
                    
                    #working_area.pop(-1)
                    working_area = working_area[:-j]
                    if sum(working_area) >= t: continue
                #    print("Start with", working_area, "Combos to the right." "t=", t, "c=", c[i+1:])
                #    backtrack(c[i+1:], t)   
                
                #working_area.append(c[i])
                #print("Start with", working_area, "Combos to the left.", "t=", t, "c=", c[:i])
                #backtrack(c[:i], t - c[i])      
                #working_area.pop(-1)
                
                
        backtrack(candidates, target)              
#        for i in range(len(candidates)):
 #           backtrack(candidates[i:], target)
       # print(working_area)
       # print(combos)
        finished_list = []
        return list(combos)
    
                

      class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combos = set()
        working_area = []
        #candidates = sorted(candidates)
        def backtrack(c, t):
            nonlocal working_area
            if len(c) < 1: return
            for x in range(len(c)):
                #if t < c[x]: break
                if t % c[x] == 0:
                    n = t // c[x]
                    for i in range(n):
                        working_area.append(c[x])
                    combos.add(tuple(sorted(working_area)))
                    for i in range(n):
                        working_area.pop(-1)
            
            for i in range(len(c)):
                for j in range(1, t // c[i]):
                    working_area += [c[i]] * j
                    backtrack(c[i+1:], t - c[i] * j)
                    backtrack(c[:i], t - c[i] * j) # remove this if you are using a sorted list
                    working_area = working_area[:-j]
                    #if sum(working_area) >= t: continue
    
        backtrack(candidates, target)              
        return list(combos)
    
                
