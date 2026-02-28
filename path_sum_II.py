class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return
            
            # Choose
            path.append(node.val)
            remaining -= node.val
            
            # Check leaf
            if not node.left and not node.right and remaining == 0:
                result.append(path[:])  # copy
            
            # Explore
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)
            
            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result