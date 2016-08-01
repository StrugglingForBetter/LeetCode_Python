class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
	def __repr__(self):
		if self is None:
			return "Nil"
		else:
			return "{} -> {}".format(self.val,repr(self.next))
class Solution:
	def removeNthFromEnd(self, head, n):
		dummy=ListNode(0)
		dummy.next=head
		p1=p2=dummy
		for i in range(n):p1=p1.next
		while p1.next:
			p1=p1.next;p2=p2.next
		p2.next=p2.next.next
		return dummy.next

if __name__=="__main__":
	head=ListNode(1)
	head.next=ListNode(2)
	head.next.next=ListNode(3)
	head.next.next.next=ListNode(4)
	head.next.next.next.next=ListNode(5)
	res=Solution().removeNthFromEnd(head,2)
	print res
	print '-'*20
	while res:
		print res
		res=res.next	
