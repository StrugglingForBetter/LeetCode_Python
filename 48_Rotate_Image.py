class Solution:
	def rotate(self, matrix):
		n=len(matrix)
		for i in range(n):
			for j in range(i+1,n):
				matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
		for i in range(n):
			matrix[i].reverse()
		return matrix

if __name__=="__main__":
	matrix=[[1,2,3,4],[5,6,7,8],[9,1,2,5],[3,7,6,4]]
	print matrix
	print '-'*20
	print Solution().rotate(matrix)