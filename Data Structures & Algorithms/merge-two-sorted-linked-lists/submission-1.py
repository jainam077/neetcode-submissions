# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
    #creating a dummy node, and a tail/node that wil trraverse D -> 1 -> etc etc

        dummy = ListNode() #has any random value
        tail = dummy # both are on the same node right now

        while list1 and list2:
            if list1.val<list2.val: 

                # basically we compare values and take the sorted one and assign it to 
                # the tail/node we created and then move the list1 to the next  element   

                tail.next = list1
                list1 = list1.next
            
            else:
                tail.next = list2
                list2 = list2.next
        # Now here our first pass has finished so we need to forward the tail to the next element value
            tail = tail.next
        if list1 == None:
            tail.next = list2
        else: tail.next = list1
        return dummy.next

