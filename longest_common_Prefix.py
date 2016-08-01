class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
	if len(strs)==0:
		return ""
        if len(strs)==1:
            return strs[0]
        else:
            shortest=len(strs[0])
	    com=strs[0]
            for i in range(1,len(strs)):
                c=0
		temp=""
		q=strs[i]
		length=min(len(com),len(q))
                for j in range(0,length):
                    if com[j]==q[j]:
                        c+=1
			temp+=q[j]
		    else:
			break
                if c<shortest:
                    shortest=c
	            com=temp
            return com
if __name__=="__main__":
	print Solution().longestCommonPrefix(["abc","ab","a"])
