class Solution:
	def myPow(self, x, n):
		if n==0:
			return 1.0
		elif n<0:
			return 1/self.myPow(x,-n)
		elif n%2:
			return self.myPow(x*x,n/2)*x
		else:
			return self.myPow(x*x,n/2)

if __name__=="__main__":
	print Solution().myPow(2,-2)
	print Solution().myPow(2,0)
	print Solution().myPow(2,10)
