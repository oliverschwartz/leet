# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        
        self.global_max = 0
        def longest_path_right_or_left(v):
            if not v: return 0

            # calculate left and right, then only include them if they're
            # the same value as this root
            l, r = longest_path_right_or_left(v.left), longest_path_right_or_left(v.right)
            l = 1 + l if v.left and v.left.val == v.val else 0
            r = 1 + r if v.right and v.right.val == v.val else 0
            
            # global longest_path max is set with current node as root
            self.global_max = max(self.global_max, l + r)
            
            # but the max we return, will be either right or left
            return max(l, r)
            
            
        longest_path_right_or_left(root)
        return self.global_max
        