import heapq
class ListNode:
	def __init__(self, x):
		self.val=x
		self.next=None
	def __repr__(self):
		if not self:
			return "Nil"
		else:
			return "{} -> {}".format(self.val,self.next)
class Solution:
	def mergeKSortedLists(self,lists):
		heap=[]
		dummy=ListNode(-1)
		cur=dummy
		for node in lists:
			if node:
				heap.append((node.val,node))
		heapq.heapify(heap)
		while heap:
			pop=heapq.heappop(heap)
			cur.next=ListNode(pop[0])
			cur=cur.next
			if pop[1].next:
				heapq.heappush(heap,(pop[1].next.val,pop[1].next))
		return dummy.next
	
if __name__=="__main__":
	list1=ListNode(1)
	list1.next=ListNode(3)
	list2=ListNode(2)
	list2.next=ListNode(4)
	list3=ListNode(2)
	list3.next=ListNode(3)
	list3.next.next=ListNode(5)
	
	print Solution().mergeKSortedLists([list1,list2,list3])		
