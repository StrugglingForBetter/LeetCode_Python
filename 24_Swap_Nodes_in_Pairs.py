class ListNode:
	def __init__(self, x):
		self.val=x
		self.next=None
	def __repr__(self):
		if self.val==None:
			return "Nil"
		else:
			return "{} -> {}".format(self.val,self.next)
class Solution:
	def swapPairs(self,head):
		p=dummy=ListNode(-1)
		dummy.next=head
		while p.next and p.next.next:
			temp=p.next.next
			p.next.next=temp.next
			temp.next=p.next
			p.next=temp
			p=p.next.next
		return dummy.next
if __name__=="__main__":
	head=ListNode(1)
	head.next=ListNode(2)
	head.next.next=ListNode(3)
	head.next.next.next=ListNode(4)
	head.next.next.next.next=ListNode(5)
	print Solution().swapPairs(head)
