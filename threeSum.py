class Solution:
	def threeSum(self, num):
		num.sort()
		res=[]
		for i in range(len(num)-2):
			if i==0 or num[i]>num[i-1]: # to exclude the situation num[i]=num[i-1]
						    # duplicates are not allowed
				left,right=i+1,len(num)-1
				while left<right:
					if num[left]+num[right]==-num[i]:
						res.append([num[i],num[left],num[right]])
						left+=1;right-=1
						while left<right and num[left]==num[left-1]:left+=1
						while left<right and num[right]==num[right+1]:right-=1
					elif num[left]+num[right]<-num[i]:
						while left<right:
							left+=1
							if num[left]>num[left-1]:break
					else:
						while left<right:
							right-=1
							if num[right]<num[right+1]:break
		return res
if __name__=="__main__":
	print Solution().threeSum([-1,0,1,2,-1,-4])
