class Solution:
	
	def removeDuplicates(self, A):
		if len(A)==0:
			return 0
		j=0
		for i in range(len(A)):
			if A[i]!=A[j]:
				A[i],A[j+1]=A[j+1],A[i]
				j+=1
		return A[0:j+1]
		
if __name__=="__main__":
	print Solution().removeDuplicates([1,2,3,3,4,4,5,5])
	print Solution().removeDuplicates([1,1,2])
