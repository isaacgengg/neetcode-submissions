# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = dummyNode = ListNode()
        list1Curr = list1
        list2Curr = list2

        while list1Curr and list2Curr:
            if list2Curr.val >= list1Curr.val:
                dummyNode.next = list1Curr
                list1Curr = list1Curr.next
            elif list1Curr.val > list2Curr.val:
                dummyNode.next = list2Curr
                list2Curr = list2Curr.next
            
            dummyNode = dummyNode.next

        dummyNode.next = list1Curr or list2Curr
    

        return dummyHead.next
  
