class Solution(object):

	def threeSumClosest(self, nums, target):

	        """
        	:type nums: List[int]
        	:type target: int
        	:rtype: int
        	"""
        	nums.sort()
        	temp=2**31-1
        	res=0
        	for i in range(len(nums)-2):
            		left,right = i+1,len(nums)-1
            		while left<right:
                		sum=nums[i]+nums[left]+nums[right]
                		diff=abs(sum-target)
                		if diff<temp:
                    			temp=diff
                    			res=sum
                		if diff==0:
                    			return sum
                		elif sum-target<0:
                    			left+=1
                		else:
                    			right-=1
        	return res
if __name__=="__main__":
    print Solution().threeSumClosest([0,2,1,-3],1) 
