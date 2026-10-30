# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slowPtr = fastPtr = headNode = head
        
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        currNode = midPointPtr = slowPtr

        # reverse back half
        prevNode = None
        while currNode:
            tempNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tempNode
        
        dummyHead = dummyNode = ListNode()

        flip = False
        while headNode is not prevNode:
            if not flip:
                dummyNode.next = headNode
                headNode = headNode.next
            else:
                dummyNode.next = prevNode
                prevNode = prevNode.next
            
            dummyNode = dummyNode.next
            flip = not flip

        dummyNode.next = midPointPtr

        