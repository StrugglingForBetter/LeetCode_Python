class Solution:
	def solveNQueens(self, n):
		def isValid(k,j):
			for i in range(k):
				if board[i]==j or abs(i-k)==abs(board[i]-j):
					return False
			return True
		
		def dfs(depth,valuelist):
			if depth==n:
				res.append(valuelist)
				return
			for i in range(n):
				if isValid(depth,i):
					board[depth]=i
					s='.'*n
					dfs(depth+1,valuelist+[s[:i]+'Q'+s[i+1:]])
		board=[-1 for i in range(n)]
		res=[]
		dfs(0,[])
		return res	
if __name__=="__main__":
	for item in Solution().solveNQueens(4):
		for str in item:
			print str
		print '-'*20
