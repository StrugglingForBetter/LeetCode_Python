class Solution:
	def plusOne(self,digits):
		flag=1
		for i in range(len(digits)-1,-1,-1):
			if digits[i]+flag==10:
				digits[i]=0
				flag=1
			else:
				digits[i]+=flag
		if flag==1:
			digits.insert(0,1)
		return digits
if __name__=="__main__":
	print Solution().plusOne([9,9,9,9])
