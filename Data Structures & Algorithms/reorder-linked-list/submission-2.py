# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None

        node = None

        while middle:
            temp = middle.next
            cur = middle
            cur.next = node
            node = cur
            middle = temp
        
        dummy = head
        
        while dummy and node:
            temp1 = dummy.next
            temp2 = node.next
            dummy.next = node
            node.next = temp1

            dummy = temp1
            node = temp2
            


        


# 1.Find the middle of the linked list using slow and fast pointers.
# This splits the list into two halves.
# 2.Reverse the second half of the list.
# Doing this makes it easy to merge nodes from the front and back alternately.
# 3.Merge the two halves one-by-one:
# Take one node from the first half (first), then one from the reversed second half (second), and repeat.