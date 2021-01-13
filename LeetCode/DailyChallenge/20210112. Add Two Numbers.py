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
