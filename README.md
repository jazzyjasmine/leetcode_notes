# Leetcode Notes
## Topics
- [Binary Tree](#binary-tree)
- [Binary Search Tree (BST)](#binary-search-tree)
- [Graph: General](#graph-general)
- [Graph: DFS](#graph-dfs)
- [Graph: Topological Sorting](#graph-topological-sorting)
- [Single-source Shortest Path](#single-source-shortest-path)
- [Dynamic Programming](#dynamic-programming)
- [String](#string)
- [Linked List](#linked-list)

&nbsp;

## 🦀 Binary Tree <a id="binary-tree"></a>

### 1. Divide & Conquer
[1315. Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)  
[333. Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/)  
[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)


### 2. Construct Tree by Two Different Traversals
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


### 3. LCA (Lowest Common Ancestor)
- Given parent node: Use math. Let $a$ denote the distance between node p and lca, $b$ denote the distance between node q and lca, $c$ denote the distance between lca and the root. We have $a + c + b = b + c + a$. So they will meet at the lca eventually.   
  [1650. Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)


### 4. Height of binary tree
height(node) = 1 + max(height(node.left) + height(node.right))  
Example:    
  [366. Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/) (Topological sorting also works for this one. Simply treat leaves as nodes with indegree of 0.)


&nbsp;

## 🦀 Binary Search Tree (BST) <a id="binary-search-tree"></a>

### 1. BST Validation
The max value in left subtree is smaller than the root value and the min value in right subtree is larger than the root value.  
[333. Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/)

### 2. Predecessor & Successor
Predecessor: The prev node, i.e. the largest node before (smaller than) the current one.  

Find predecessor:  
1. If node has left child: One step left and then always right.
2. If node has no left child: The first node that is not having a "left" relationship with its parent.

Successor: The next node, i.e. the smallest node after (larger than) the current node.

Find successor:  
1. If node has right child: One step right and then always left.
2. If node has no right child: The first node that is not having a "right" relationship with its parent.

![bst_successor](/diagrams/bst_successor.png)

Typical BST predecessor/successor problem:  
📎 [426. Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)  
📎 [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)  
📎 [99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

Other BST problems:  
[285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)  
[450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)  


BST problems using recursion:
[https://leetcode.com/problems/trim-a-binary-search-tree/](https://leetcode.com/problems/trim-a-binary-search-tree/)  


&nbsp;

## 🦀 Graph: General<a id="graph-general"></a>

### Detect Cycle
Key: If there is a neighbor that has been visited, then there is a cycle.  
Can be solved by DFS, BFS, UnionFind.  
- For undirected graph, what's more complicated is that, each edge has two directions, so when a neighbor of the current node is the parent of current node, even though this neighbor is in the "visited" set, we should not say there is a cycle. We should exclude this scenario after checking whether a neighbor is in "visited".  
- For the DFS solution, we do not use backtracking (e.g. visited.add(neighbor), dfs(neighbor), visited.remove(neighbor)) because we need to get all visited sub nodes when we are to mark the current node as black (finish probing). Backtracking is used for getting all paths from a start to an end. After finish probing all sub nodes, backtracking keeps the "visited" set only the previous nodes till the current node, no sub nodes.  
[261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

&nbsp;

## 🦀 Graph: BFS <a id="graph-bfs"></a>
[1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)

&nbsp;

## 🦀 Graph: DFS <a id="graph-dfs"></a>
- White: Not visited; Gray: Visited, probing; Black: Visited, finish probing.   
- Make deep copy whenever append a list to the result sets  
  [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)
- Build graph and find recursion  
    [851. Loud and Rich](https://leetcode.com/problems/loud-and-rich/)


&nbsp;

## 🦀 Graph: Topological Sorting<a id="graph-topological-sorting"></a>
- DAG &harr; At least one topological sorting.  
  If DAG(directed acyclic graph), it must have at least one topological sorting.  
  If the graph has topological sorting, it must be a DAG.
- Build graph and identify topological sorting (identify DEPENDENCIES/PREREQUISITES)
- Use "visited" set to check if topological sorting exists   
[802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)  
[2115. Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)  
[1136. Parallel Courses](https://leetcode.com/problems/parallel-courses/) 

&nbsp;

## 🦀 Single-source Shortest Path <a id="single-source-shortest-path"></a>
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
  [1786. Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/)

&nbsp;

### UnionFind
[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

&nbsp;

## 🦀 Dynamic Programming <a id="dynamic-programming"></a>
Categories by problem types:
### Memoization Search
To avoid repeated calculation. Substitute divide and conquer for memoization search is the subproblems have overlaps.  
[120. Triangle](https://leetcode.com/problems/triangle/)

### Extreme Values
[198. House Robber](https://leetcode.com/problems/house-robber/)  
[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
```python
if text2[i - 1] == text1[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```  

### Total number of paths/strategies
[62. Unique Paths](https://leetcode.com/problems/unique-paths/)  
[63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

### Feasibility

&nbsp;

Categories by solution types:
### Prefix: Segmentation
[139. Word Break](https://leetcode.com/problems/word-break/)  
[140. Word Break II](https://leetcode.com/problems/word-break-ii/)

&nbsp;

## 🦀 String <a id="string"></a>

[408. Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/)  
Brute force. Use two pointers. Be careful about corner cases.  
[791. Custom Sort String](https://leetcode.com/problems/custom-sort-string/)  
Use Counter to get the show times of each character, sort those in "order" first (pop while sorting).

&nbsp;

## 🦀 Linked List <a id="linked-list"></a>
- DummyHead (same with result initially)  
  [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/submissions/)
- Others  
  [708. Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/)


&nbsp;

## 🦀 Data Structure <a id="data-structure"></a>
- Data structure combination  
  [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
- Direct data structure (non-combination)  
  [1396. Design Underground System](https://leetcode.com/problems/design-underground-system/)  
  [244. Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/)


&nbsp;

## 🦀 Modular Arithmetic <a id="modular-arithmetic"></a>
- Subtraction  
  [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)
- Addition  
  [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)  

&nbsp;

## 🦀 Binary Search <a id="binary-search"></a>
Advanced (binary search not at a glance, need detection):  
- [1060. Missing Element in Sorted Array](https://leetcode.com/problems/missing-element-in-sorted-array/)

&nbsp;

## 🦀 Monotonic Stack <a id="monotonic-stack"></a>
Monotonic stacks are a good option when a problem involves comparing the size of numeric elements, with their order being relevant.  
Tricky part: The time complexity is O(n) though there is nested loop.  
[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

&nbsp;

## 🦀 Python Tricks <a id="python-tricks"></a>
### Sort dictionary(hashmap) by key
```python
>> a = {2: [3,4], 1: [5,6]}
>> sorted(a.items())
[(1, [5, 6]), (2, [3, 4])]
```
### Append into nested list
```python
>> a = [[1], [1], [1]]
>> a[1].append(2)
>> a
[[1], [1, 2], [1]]
```
