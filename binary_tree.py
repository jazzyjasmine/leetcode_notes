# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 106. Construct Binary Tree from Inorder and Postorder Traversal
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        
        root_pos = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[0: root_pos], postorder[0: root_pos])
        root.right = self.buildTree(inorder[root_pos + 1: len(inorder)], postorder[root_pos: -1])
        
        return root

    # 450. Delete Node in a BST
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
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
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
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


    # 285. Inorder Successor in BST
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
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
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        
        return successor