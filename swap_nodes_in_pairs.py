class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap
            prev.next = second
            first.next = second.next
            second.next = first

            # move prev
            prev = first

        return dummy.next