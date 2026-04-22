class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
            
            res = []
            
            for root in range(start, end + 1):
                left = build(start, root - 1)
                right = build(root + 1, end)
                
                for l in left:
                    for r in right:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        res.append(node)
            
            return res
        
        return build(1, n)