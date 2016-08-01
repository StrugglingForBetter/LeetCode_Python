class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None
	def __repr__(self):
		if self is None:
			return " Nil"
		else:
			return "{} -> {}".format(self.val, self.next)
class Solution(object):
	def mergeTwoLists(self,l1,l2):
	        cur=dummy=ListNode(0)
		if not l1:
			return l2
		if not l2:
			return l1
	  	while l1 and l2:
			if l1.val<l2.val:
				cur.next=l1
				l1=l1.next

			else:
				cur.next=l2
				l2=l2.next
			cur=cur.next
		cur.next=l1 or l2
		return dummy.next
if __name__=="__main__":
	l1=ListNode(1)
	l1.next=ListNode(2)
	l1.next.next=ListNode(3)
	l1.next.next.next=ListNode(6)
	l2=ListNode(2)
	l2.next=ListNode(4)
	l2.next.next=ListNode(6)
	l2.next.next.next=ListNode(8)
	l2.next.next.next.next=ListNode(10)
	print Solution().mergeTwoLists(l1,l2)
