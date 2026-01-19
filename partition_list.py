class Solution:
    def partition(self, head, x):
        less_head = less = ListNode(0)
        greater_head = greater = ListNode(0)
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        greater.next = None
        less.next = greater_head.next
        
        return less_head.next
