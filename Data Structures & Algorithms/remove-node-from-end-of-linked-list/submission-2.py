# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cur = head
        # N=0
        # while cur:
        #     N+=1
        #     cur=cur.next
        # removeIndex=N-n
        # if removeIndex==0:
        #     return head.next
        
        # cur = head
        # for i in range(N-1):
        #     if (i+1)==removeIndex:
        #         cur.next=cur.next.next
        #         break
        #     cur=cur.next
        # return head

        dummy = ListNode(0,head)
        left = dummy
        right= head 

        while n>0:
            right = right.next
            n-=1

        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next
        return dummy.next