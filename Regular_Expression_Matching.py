class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
	m,n=len(s),len(p)
	
	#init dp dp[i][j] represents the matching status between s[i:] and p[j:]
	dp = [[False for i in range(n+1)] for i in range(m+1)]
	#the matching process starts from the end of s to the beginning of s(backwards)
	#because the matching status of a postion in s depends on the matching status behind
	# when the string s and pattern p are all null
	dp[m][n]=True
	# when the string is Null, pattern like "c*" can still match it
	for i in range(n-1,-1,-1):
		if p[i]=="*":
			dp[m][i]=dp[m][i+1]
		elif i+1<n and p[i+1]=="*":
			dp[m][i]=dp[m][i+1]
		else:
			dp[m][i]=False
	#after matching the null string and the pattern, we begin to match s and pattern 
	for i in range (m-1,-1,-1):
		for j in range (n-1,-1,-1):
			#when the current character is "*"
			if p[j]=="*":
				if j-1>=0 and p[j-1]!="*":
					dp[i][j]=dp[i][j+1]
				#if the pattern is starting with "*" or has "**"in it return false
				else:
					return False
			#when the character after the current pattern chacter is *
			elif j+1<n and p[j+1]=="*":
				if s[i]==p[j] or p[j]==".":
					dp[i][j]=dp[i][j+2] or dp[i+1][j] or dp[i+1][j+2]
				#ignore the first two characters("c*") in pattern since they cannot match
				#the current character in string
				else:
					dp[i][j]=dp[i][j+2]
			else:
				#when the current character is matched
				if s[i]==p[j] or p[j]==".":
					dp[i][j]=dp[i+1][j+1]
				else:
					dp[i][j]=False
	return dp[0][0]
if __name__=="__main__":
	print Solution().isMatch("aa","a")
	print Solution().isMatch("aa","aa")
	print Solution().isMatch("aaa","aa")
	print Solution().isMatch("aa","a*")
	print Solution().isMatch("aa",".*")
	print Solution().isMatch("ab",".*")
	print Solution().isMatch("aab","c*a*b")
