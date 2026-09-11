# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = temp = head
        
        xset = set()
        while temp:
            if temp not in xset:
                xset.add(temp)
                temp = temp.next
            else : return True
        return False   
            