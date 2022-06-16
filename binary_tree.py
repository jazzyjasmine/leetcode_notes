from typing import List, Optional, Tuple, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution366_1_NonOptimal:
    # 366. Find Leaves of Binary Tree
    # DFS + Hashmap
    # Non-optimal solution with sorting. Time: O(nlogn); Space: O(n)
    # https://leetcode.com/problems/find-leaves-of-binary-tree/
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        height_to_nodes = {}
        self.get_heights(height_to_nodes, root)
        return [pair[1] for pair in sorted(height_to_nodes.items())]
    
    
    def get_heights(self, height_to_nodes, root):
        if not root:
            return -1
        
        left_height = self.get_heights(height_to_nodes, root.left)
        right_height = self.get_heights(height_to_nodes, root.right)
        curr_height = max(left_height, right_height) + 1
        
        if curr_height in height_to_nodes:
            height_to_nodes[curr_height].append(root.val)
        else:
            height_to_nodes[curr_height] = [root.val]
        
        return curr_height


class Solution366_2_Optimal:
    # 366. Find Leaves of Binary Tree
    # DFS
    # Optimal solution without sorting. Time: O(n); Space: O(n)
    # https://leetcode.com/problems/find-leaves-of-binary-tree/
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        self.get_heights(root, results)
        return results
    
    
    def get_heights(self, root, results):
        if not root:
            return -1
        
        left_height = self.get_heights(root.left, results)
        right_height = self.get_heights(root.right, results)
        curr_height = max(left_height, right_height) + 1
        
        # the node's height is exactly the index of the list in the results
        # insert into results instead of sorting
        if curr_height == len(results):
            results.append([root.val])
        else:
            results[curr_height].append(root.val)
        
        return curr_height


class Solution1650:
    # 1650. Lowest Common Ancestor of a Binary Tree III
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.parent = None

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_dup, q_dup = p, q
        while p_dup != q_dup:
            p_dup = p_dup.parent if p_dup.parent else q
            q_dup = q_dup.parent if q_dup.parent else p
        return p_dup

class Solution2196:
    # 2196. Create Binary Tree From Descriptions
    # https://leetcode.com/problems/create-binary-tree-from-descriptions/
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val_to_node = {}
        for parent, child, isLeft in descriptions:
            parent_node = self.get_node(val_to_node, parent)
            child_node = self.get_node(val_to_node, child)
            val_to_node[child][1] = True
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
        for val, (node, isChild) in val_to_node.items():
            if not isChild:
                return node
        
        return None
    
    
    def get_node(self, val_to_node, val):
        if val in val_to_node:
            return val_to_node[val][0]
        node = TreeNode(val)
        val_to_node[val] = [node, False] # note that this cannot be a tuple because tuple is immutable
        return node


class Solution1315:
    """Divide and Conquer"""
    # 1315. Sum of Nodes with Even-Valued Grandparent
    # https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans, _ = self.helper(root)
        return ans
    
    def helper(self, root):
        if not root:
            return 0, 0
        
        left, left_snd_sum = self.helper(root.left)
        right, right_snd_sum = self.helper(root.right)
        
        curr_snd_sum = 0
        
        if root.left:
            curr_snd_sum += root.left.val
        if root.right:
            curr_snd_sum += root.right.val
        
        if root.val % 2 != 0:
            return left + right, curr_snd_sum
        
        return left + right + left_snd_sum + right_snd_sum, curr_snd_sum


class Solution106:
    # 106. Construct Binary Tree from Inorder and Postorder Traversal
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        
        root_pos = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[0: root_pos], postorder[0: root_pos])
        root.right = self.buildTree(inorder[root_pos + 1: len(inorder)], postorder[root_pos: -1])
        
        return root
