class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        node1 = l1
        node2 = l2
        remainder = 0
        curr = ListNode() #burner
        head = curr

        while True:
            if (node1 is None and node2 is None): break
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0

            val3 = val1 + val2 + remainder
            if val3 > 9:
                remainder = 1
                val3 -= 10
            else:
                remainder = 0
            next = ListNode(val3, None)
            curr.next = next
            curr = next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        if remainder:
            next = ListNode(remainder, None)
            curr.next = next
            curr = next
        head = head.next #burn the burner
        curr = head

        return head
