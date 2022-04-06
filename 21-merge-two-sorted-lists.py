# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.



#   O > O > O
#   O > O > O

#   O   O   O
#   V   ^ \ ^
#   O > O   O


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


        L = list1
        R = list2
        # check for null lists
        if not list1:
            return list2
        if not list2:
            return list1

        # initial condition
        # determine which is head, and which is temp
        head = None
       if list1.val <= list2.val:
            curr = list1
            temp = list2
        else:
            curr = list2
            temp = list1
        head = curr

        # compare if next is already in place or is the other list
        while curr.next and temp:
            if curr.next.val <= temp.val:
                curr = curr.next
            else:
                temp2 = curr.next
                curr.next = temp
                temp = temp2
                curr = curr.next

        print('curr', curr, curr.next, 'temp', temp, temp.next)

        # add on stragglers

        while temp:
            temp2 = curr.next
            curr.next = temp
            curr = curr.next
            temp = temp2
        return head
