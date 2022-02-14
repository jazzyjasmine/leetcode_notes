# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 333. Largest BST Subtree
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        ans, _, _, _ = self.helper(root)
        return ans
    
    
    def helper(self, root):
        if not root:
            return 0, True, float("-inf"), float("inf")
        
        l_num, l_include, l_max, l_min = self.helper(root.left)
        r_num, r_include, r_max, r_min = self.helper(root.right)
        
        curr_max = max(l_max, root.val, r_max)
        curr_min = min(l_min, root.val, r_min)
        
        curr_num, curr_include = None, False
        
        if l_include and r_include and l_max < root.val and r_min > root.val:
            curr_num = l_num + r_num + 1
            curr_include = True
        else:
            if l_num > r_num:
                curr_num = l_num
            else:
                curr_num = r_num
        
        return curr_num, curr_include, curr_max, curr_min

    # 1008. Construct Binary Search Tree from Preorder Traversal
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        i = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[1: i + 1], inorder[0: i])
        root.right = self.buildTree(preorder[i + 1: len(preorder)], inorder[i + 1: len(preorder)])
        
        return root

    # 99. Recover Binary Search Tree
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x, y = None, None
        stack = []
        self.findLeftMost(root, stack)
        
        while stack:
            curr = stack.pop()
            self.findLeftMost(curr.right, stack)
            if stack:
                successor = stack[-1]
                if successor.val < curr.val:
                    y = successor
                    if not x:
                        x = curr
                    else:
                        break
        
        x.val, y.val = y.val, x.val
          
    
    def findLeftMost(self, root, stack):
        while root:
            stack.append(root)
            root = root.left
            
        