'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        answer = result # head of result
        remainder = 0
        sum = 0
        while True:
            if l1 == None and l2 == None:
                if remainder == 1:
                    sum = 1
                    remainder = 0
                else:
                    break
            elif l1 == None and l2 != None:
                sum = l2.val + remainder
                l2 = l2.next
            elif l1 != None and l2 == None:
                sum = l1.val + remainder
                l1 = l1.next
            else:
                sum = l1.val + l2.val + remainder
                l1 = l1.next
                l2 = l2.next
            
            if (sum < 10):
                remainder = 0
            else:
                sum = sum - 10
                remainder = 1

            result.next = ListNode(sum)
            result = result.next
        return answer.next

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

while True:
    if result == None:
        break
    print(result.val)
    result = result.next
