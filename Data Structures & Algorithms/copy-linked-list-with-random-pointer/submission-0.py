"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = collections.defaultdict(lambda: Node(0))
        nodeDict[None] = None

        currNode = head

        while currNode:
            nodeDict[currNode].val = currNode.val
            nodeDict[currNode].next = nodeDict[currNode.next]
            nodeDict[currNode].random = nodeDict[currNode.random]
            currNode = currNode.next
        
        return nodeDict[head]
        