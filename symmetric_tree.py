class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(t1, t2):
            # If both are None
            if not t1 and not t2:
                return True
            
            # If one is None or values differ
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # Check mirror condition
            return (isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        
        return isMirror(root, root)
