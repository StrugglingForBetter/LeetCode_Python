class Solution:
	def SortColors(self,nums):
		i=0
		p=0
		q=len(nums)-1
		while i<=q:
			if nums[i]==2:
				nums[i],nums[q]=nums[q],nums[i]
				q-=1
			elif nums[i]==0:
				nums[i],nums[p]=nums[p],nums[i]
				p+=1
				i+=1
			else:
				i+=1
		return nums

if __name__=="__main__":
	print Solution().SortColors([1,0,1,2,0,0,0,1,1,2,1,2])

