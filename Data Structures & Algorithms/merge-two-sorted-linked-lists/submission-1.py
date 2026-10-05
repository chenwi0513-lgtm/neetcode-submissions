# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        iterator = dummyHead
        while list1 and list2:
            iterator.next = list1 if list1.val < list2.val else list2
            iterator = iterator.next
            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next
        iterator.next = list1 if list1 else list2
        return dummyHead.next