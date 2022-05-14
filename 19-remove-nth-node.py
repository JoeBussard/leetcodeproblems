totalLength = 1
        curr = head
        while curr.next:
            curr = curr.next
            totalLength += 1
            
        targetIndex = totalLength - n
        
        if totalLength == 1:
            head = None
            return
        elif targetIndex == 0:
            temp = head.next
            head = None
            return temp

        
        
        
            
