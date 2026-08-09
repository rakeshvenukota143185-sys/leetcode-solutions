class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root
        left_root = preorder[1]
        index = postorder.index(left_root)
        left_size = index + 1

        root.left = self.constructFromPrePost(
            preorder[1:left_size + 1],
            postorder[:left_size]
        )

        root.right = self.constructFromPrePost(
            preorder[left_size + 1:],
            postorder[left_size:-1]
        )

        return root
        
