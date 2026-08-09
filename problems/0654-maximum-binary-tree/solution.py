class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        max_value = max(nums)
        index = nums.index(max_value)

        root = TreeNode(max_value)

        root.left = self.constructMaximumBinaryTree(
            nums[:index]
        )

        root.right = self.constructMaximumBinaryTree(
            nums[index + 1:]
        )

        return root
        
