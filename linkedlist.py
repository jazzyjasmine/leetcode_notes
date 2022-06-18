from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    # 2. Add Two Numbers
    # Add two numbers in linked list and return result in linked list
    # Use dummyhead and carry
    # https://leetcode.com/problems/add-two-numbers/
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        dummyHead = result  # let dummyHead point to the result, instead of dummyHead.next = result
        
        carry = 0  # initialize carry
        
        while l1 or l2:
            l1_val = l1.val if l1 else 0  # no need to write "while l1 and l2" then "while l1" then "while l2"
            l2_val = l2.val if l2 else 0
            
            curr_digit = l1_val + l2_val + carry
            carry = curr_digit // 10  # !!!

            result.next = ListNode(curr_digit % 10)  # !!!
            result = result.next
            
            if l1:
                l1 = l1.next
                
            if l2:
                l2 = l2.next
        
        if carry > 0:
            result.next = ListNode(carry)
            
        return dummyHead.next


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution708:
    # 708. Insert into a Sorted Circular Linked List
    # Time O(n), Space O(1)
    # https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
    def insert_optimized_sol(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # Case 1: head is null, return the new node
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        prev, curr = head, head.next
        
        while True:
            # Case 2: min <= insertVal <= max
            if prev.val <= insertVal <= curr.val:
                prev.next = Node(insertVal, curr)
                return head
            
            # Case 3: The loop is not uniform, and the insertVal is either lower than min or higher than max
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next
            
            if prev == head:
                break
        
        # Case 4: The loop is uniform, all values are the same
        prev.next = Node(insertVal, curr)
        return head
    

    def insert_original_sol(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        if not head.next:
            head.next = Node(insertVal, head)
            return head.next
        
        given_node = head
        last_max_node, first_min_node = self.get_extremes(head)
        
        if insertVal < first_min_node.val or insertVal > last_max_node.val:
            last_max_node.next = Node(insertVal, first_min_node)
            return given_node
        
        while head.val > insertVal or head.next.val < insertVal:
            head = head.next
        
        post_node = head.next
        head.next = Node(insertVal, post_node)
        return given_node
        
        
    def get_extremes(self, head):
        max_val = head.val
        max_node = head
        node = head.next
        while node and node != head:
            if node.val >= max_val:
                max_val = node.val
                max_node = node
            node = node.next

        return max_node, max_node.next