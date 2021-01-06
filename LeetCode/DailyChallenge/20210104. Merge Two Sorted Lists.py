'''
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Input: l1 = [], l2 = []
Output: []
Input: l1 = [], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check if one of two lists is empty. (or all of them)
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        
        return head

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
result = solution.mergeTwoLists(l1, l2)

while True:
    if result == None:
        break
    print(result.val)
    result = result.next