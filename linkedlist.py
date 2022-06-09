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