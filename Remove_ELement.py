class Solution:
	def RemoveElem(self, nums,elem):
		j=len(nums)-1
		for i in range (len(nums)-1,-1,-1):
			if nums[i]==elem:
				nums[i],nums[j]=nums[j],nums[i]
				j-=1
		return nums

if __name__=="__main__":
	print Solution().RemoveElem([1,2,2,1,3,2,1],1)

