class Solution:
	def permutationUnique(self, nums):
		if len(nums)==0: return []
		if len(nums)==1: return [nums]
		res=[]
		nums.sort()
		previousNum=None
		for i in range(len(nums)):
			if nums[i]==previousNum:
				continue
			previousNum=nums[i]
			for j in self.permutationUnique(nums[:i]+nums[i+1:]):
				res.append([nums[i]]+j)
		return res

if __name__=="__main__":
	print Solution().permutationUnique([1,1,2])
