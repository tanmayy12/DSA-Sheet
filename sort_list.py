class Solution:
    
    def sortList(self, head):
        # Base case
        if not head or not head.next:
            return head
        
        # Step 1: split list into halves
        mid = self.getMid(head)
        right = mid.next
        mid.next = None
        
        # Step 2: sort both halves
        left = self.sortList(head)
        right = self.sortList(right)
        
        # Step 3: merge
        return self.merge(left, right)
    
    
    def getMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next