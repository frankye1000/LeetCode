# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next

#############################################################################
l1 = [1,2,4,4,4]
l2 = [1,3,3,4,5,5,5,5]

sort_list=[]
for i in range(min(len(l1),len(l2))):
    sort_list.append(min([l1[i],l2[i]]))
    sort_list.append(max([l1[i], l2[i]]))

if len(l1)>len(l2):
    for i in range(min(len(l1),len(l2)),max(len(l1),len(l2))):
        sort_list.append(l1[i])
else:
    for i in range(min(len(l1),len(l2)),max(len(l1),len(l2))):
        sort_list.append(l2[i])

print(sort_list)