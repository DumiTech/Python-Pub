'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = [1,2,4]
l2 = [1,3,4]


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		dummy = ListNode()
		tail = dummy

		while l1 and l2:
			if l1.val < l2.val:
				tail.next = l1
				l1 = l1.next
			else:
				tail.next = l2
				l2 = l2.next
			tail = tail.next

		tail.next = l1 or l2
		
		return dummy.next