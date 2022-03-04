# Leetcode Notes
## Topics
- [Binary Tree](#binary-tree)
- [Binary Search Tree (BST)](#binary-search-tree)

&nbsp;

## Binary Tree <a id="binary-tree"></a>

### <span style="color:yellow">Divide & Conquer</span>
[333. Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/)  

&nbsp;

### <span style="color:yellow">Construct Tree by Two Different Traversals</span>
Use recursion, find root and the span of left subtree (start and end) and the span of right subtree (start and end) on the array.  
[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)  
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        i = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[1: i + 1], inorder[0: i])
        root.right = self.buildTree(preorder[i + 1: len(preorder)], inorder[i + 1: len(preorder)])
        
        return root
```
[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)  
[1008. Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)



&nbsp;

## Binary Search Tree (BST) <a id="binary-search-tree"></a>

### <span style="color:yellow">BST Validation</span>
The max value in left subtree is smaller than the root value and the min value in right subtree is larger than the root value.  
[333. Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/)

### <span style="color:yellow">Predecessor & Successor</span>
Predecessor: The prev node, i.e. the largest node before (smaller than) the current one.  

Find predecessor:  
1. If node has left child: One step left and then always right.
2. If node has no left child: The first node that is not having a "left" relationship with its parent.

Successor: The next node, i.e. the smallest node after (larger than) the current node.

Find successor:  
1. If node has right child: One step right and then always left.
2. If node has no right child: The first node that is not having a "right" relationship with its parent.

[285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)  
[450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

&nbsp;

## Dynamic Programming <a id="dynamic-programming"></a>
[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
```python
if text2[i - 1] == text1[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

## Graph DFS <a id="graph-dfs"></a>
- Make deep copy whenever append a list to the result sets  
  [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)
- Build graph and find recursion  
    [851. Loud and Rich](https://leetcode.com/problems/loud-and-rich/)

## Single-source Shortest Path <a id="single-source-shortest-path"></a>
### Dijkstra
Points:
- Remember the "visited" set, i.e. S, after the vertices popped out from the heap, they were added to the S, meaning that their shortest distance from the source vertex is found and fixed, i.e. d[u] = $\delta$(u, s). 
    
  There are two places to use the "visited":
  1. (Must) After a vertex is popped out from the heap, we need to check whether it is in the visited, if so, skip to the next iteration. If we don't do so, the heap will never become empty and thus endless loop.
  2. (Optional but recommended) For each neighbor of the popped-out-vertex, check if it is in the visited set, if so, skip. Not doing so will not cause error, but it keeps the unneccessary calculation.


Types of problems:
- Straightforward Dijkstra with extra work in the results set  
  [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- Add: count number of shortest path  
  [1976. Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)



## UnionFind
[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)