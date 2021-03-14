class Solution(object):
	def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy 
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next   

class Solution(object):
	def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1 
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2 

        
