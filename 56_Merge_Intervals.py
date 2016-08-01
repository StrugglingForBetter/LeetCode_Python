class Intervals(object):
	def __init__(self,s,e):
		self.start=s
		self.end=e
	def __repr__(self):
		return "[{},{}]".format(self.start,self.end)

class Solution(object):
	def merge(self, intervals):
		intervals.sort(key=lambda x:x.start)
		length=len(intervals)
		res=[]
		for i in range(length):
			if res==[]:
				res.append(intervals[i])
			else:
				if res[len(res)-1].start<=intervals[i].start<=res[len(res)-1].end:
					res[len(res)-1].end=max(res[len(res)-1].end,intervals[i].end)
				else:
					res.append(intervals[i])
		return res
if __name__=="__main__":
	print Solution().merge([Intervals(1,3),Intervals(2,6),Intervals(8,10),Intervals(15,18)])
