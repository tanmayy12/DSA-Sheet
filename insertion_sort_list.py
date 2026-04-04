class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)  # sorted list
        
        curr = head
        
        while curr:
            prev = dummy
            next_node = curr.next  # save next
            
            # find position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            # move to next node
            curr = next_node
        
        return dummy.next