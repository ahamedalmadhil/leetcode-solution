# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1 or head is None:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. Find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next

            # 2. Reverse nodes in [group_prev.next .. kth]
            prev = group_next
            curr = group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 3. Connect previous part to new head, and advance group_prev
            new_group_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_group_tail