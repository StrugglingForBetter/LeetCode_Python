class Solution:
	def ReverseInteger(self, x):
		if x>=0:
			sgn=1
		else:
			sgn=-1
		x=abs(x)
		ans=0
		while x>0:
			ans=ans*10+x%10
			x=x/10
		return sgn*ans


if __name__=="__main__":
	print Solution().ReverseInteger(123)
