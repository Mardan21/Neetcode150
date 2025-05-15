class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []

        def dfs(curr, depth):
            if not curr:
                return

            if depth == len(rightView):
                rightView.append(curr.val)
            
            dfs(curr.right, depth + 1)
            dfs(curr.left, depth + 1)

        dfs(root, 0)

        return rightView
