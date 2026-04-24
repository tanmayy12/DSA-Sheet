class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        queue = [(root, 1)]
        i = 0
        
        while i < len(queue):
            node, depth = queue[i]
            i += 1
            
            # check leaf
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))