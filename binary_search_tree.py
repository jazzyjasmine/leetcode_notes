# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution450:
    # 450. Delete Node in a BST
    # Solution 1
    def deleteNodeSol1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right and not root.left:
                root = None
            elif root.right:
                root.val = self.getSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.getPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root 
    
    def getPredecessor(self, node):
        predecessor = node.left
        while predecessor.right:
            predecessor = predecessor.right
        return predecessor.val
    
    def getSuccessor(self, node):
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor.val

    # 450. Delete Node in a BST
    # Solution 2
    def deleteNodeNoChild(self, parent, target):
        if parent.right == target:
            parent.right = None
        else:
            parent.left = None
    
    def deleteNodeOneChild(self, parent, target):
        if not target.left:
            if parent.right == target:
                parent.right = target.right
            else:
                parent.left = target.right
                
        if not target.right:
            if parent.right == target:
                parent.right = target.left
            else:
                parent.left = target.left       
    
    def deleteNodeSol2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        dummy = TreeNode()
        dummy.right = root
        
        stack = self.findKey(dummy, key)
        if stack[-1].val != key:
            return root
        
        target = stack.pop()
        
        if not target.left and not target.right:
            self.deleteNodeNoChild(stack[-1], target)
            return dummy.right
        
        if not target.left or not target.right:
            self.deleteNodeOneChild(stack[-1], target)
            return dummy.right
                
        node = target.right
        parent = target
        while node.left:
            parent = node
            node = node.left
        
        target.val = node.val
        node.val = target.val
        
        if not node.right:
            self.deleteNodeNoChild(parent, node)
            return dummy.right
        
        self.deleteNodeOneChild(parent, node)
        return dummy.right
        
    
    def findKey(self, dummy, key):
        stack = [dummy]
        node = dummy.right
        while node and node.val != key:
            stack.append(node)
            if node.val < key:
                node = node.right
            else:
                node = node.left
        
        if node:
            stack.append(node)
                
        return stack

class Solution285:
    # 285. Inorder Successor in BST
    def inorderSuccessorSol1(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        
        stack = []
        node = root
        while node and node != p:
            stack.append(node)
            if node.val < p.val:
                node = node.right
            else:
                node = node.left
        
        node = p
        while stack and stack[-1].right == node:
            node = stack.pop()
        
        return stack[-1] if stack else None

    # 285. Inorder Successor in BST
    def inorderSuccessorSol2(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        
        return successor


class Solution333:
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


class Solution1008:
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


class Solution99:
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
            
        