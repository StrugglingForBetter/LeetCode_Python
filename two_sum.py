class Solution:
	def twoSum(self, num, target):
		"""
	        :type nums: List[int]
        	:type target:int
        	:rtype: List[int]
        	"""
		d={}
		r=[]
		for i,e in enumerate(num):
			if target - e in d:
				r.append(d[target-e])
				r.append(i)
				return r
			d[e]=i
if __name__=="__main__":
	print Solution().twoSum([3,2,4],6)
	
