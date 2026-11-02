# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 1. Find the k-th node from the current groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # 2. Reverse the k group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # 3. Connect the reversed group with the rest of the list
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr