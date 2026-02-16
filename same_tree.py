class Solution:
    def isSameTree(self, p, q):
        # If both nodes are None
        if not p and not q:
            return True
        
        # If one is None or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Check left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
