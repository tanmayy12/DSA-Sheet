class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: make circular
        tail.next = head
        
        # Step 3: reduce k
        k = k % length
        
        # Step 4: find new tail
        steps_to_new_tail = length - k - 1
        new_tail = head
        
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 5: new head
        new_head = new_tail.next
        
        # Step 6: break circle
        new_tail.next = None
        
        return new_head