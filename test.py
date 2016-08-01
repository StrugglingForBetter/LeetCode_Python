class Solution:
	def show(self):
		res=[]
		i=10
		while i>0:
			if i==10:s=str(i)
			else:
				s+=' '+str(i)
			i-=1
		s+=' '*2
		return s

if __name__=="__main__":
	print Solution().show()
