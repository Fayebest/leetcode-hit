# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        firNode = head
        for i in range(n-1):
            firNode = firNode.next
        secNode = head
        tempNode = None
        while firNode.next != None:
            if firNode.next.next == None:
                tempNode = secNode
            firNode = firNode.next
            secNode = secNode.next
        if secNode == head:
            return head.next
        if tempNode != None:
            tempNode.next = secNode.next   
        else:
            return None
    
        return head