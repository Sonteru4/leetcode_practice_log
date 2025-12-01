class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next
