class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None
	def __repr__(self):
		if self is None:
			return 'Nil'
		else:		
			return '{} -> {}'.format(self.val, self.next)
class Solution(object):
	def rotateRight(self, head, k):
		dummy=ListNode(-1)
		dummy.next=head
		#to be continued
		return dummy.next
if __name__=="__main__":
	head=ListNode(1)
	head.next=ListNode(2)
	head.next.next=ListNode(3)
	head.next.next.next=ListNode(4)
	head.next.next.next.next=ListNode(5)
	print Solution().rotateRight(head,2)
