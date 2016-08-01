class Solution:
	def strStr(self, haystack, needle):
		if len(needle)>len(haystack):
			return -1
		i=0
		while i<len(haystack)-len(needle)+1:
			k,j=i,0
			while j<len(needle):
				if haystack[k]==needle[j]:
					k+=1;j+=1
				else:
					break
			if j==len(needle):
				break
			else:
				i+=1
		if i==len(haystack)-len(needle)+1:
			return -1
		else:
			return haystack[i:]

if __name__=="__main__":
	print Solution().strStr('abcdefabc','de')
