# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #print(lists)
        big_list = []
        
        for linked_list in lists:
            curr = linked_list
            while curr != None:
                big_list.append(curr.val)
                curr = curr.next
        
       # print(big_list)
        big_list.sort()
      #  print(big_list)
        if len(big_list) == 0:
            return None
        head = ListNode()
        head.val = big_list[0]
        
        curr = head
        
        for element in big_list[1:]:
            node = ListNode(val = element)
            curr.next = node
            curr = curr.next
        
        
        return head
        
