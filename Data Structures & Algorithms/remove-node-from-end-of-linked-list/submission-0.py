# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        currNode = head
        dummyHead = dummyNode = ListNode
        dummyNode.next = head

        count = 0

    # move currNode to

        while currNode:
            if count < n: 
                count += 1
                currNode = currNode.next
                continue
            else:
                currNode = currNode.next
                dummyNode = dummyNode.next

        newNode = dummyNode.next.next
        dummyNode.next = newNode

        return dummyHead.next



# intutive 
# n = 2
#         head
# dummy -> 1 -> 2 -> 3 -> 4  
# ^                  ^
# dummy -> 1 -> 2 -> 3 -> 4  
#          ^              ^ 
# dummy -> 1 -> 2 -> 3 -> 4 -> null  
#               ^               ^ 
#
# &1, &2, &3, &

# iterate through and store node references in a stack, pop n + 1 times and relink n + 1 node to n - 1 node.