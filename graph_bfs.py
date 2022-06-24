from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1302:
    # 1302. Deepest Leaves Sum
    # https://leetcode.com/problems/deepest-leaves-sum/
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        next_level = deque([root])
        
        while next_level:
            curr_level = next_level
            next_level = deque([])
            
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
        return sum([node.val for node in curr_level])
