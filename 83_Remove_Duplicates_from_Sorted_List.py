'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pointer = head         
        while True:
            if head == None or pointer.next == None:
                return head
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:                           
                pointer = pointer.next  
