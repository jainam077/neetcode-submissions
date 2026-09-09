# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        elements = []
        while curr != None:
            elements.append(curr.val)
            curr = curr.next


        if elements:
            Head = ListNode(elements[-1])
            curr = Head
        
            for value in elements[-2::-1]:
                curr.next = ListNode(value)
                curr = curr.next
            return Head
