class Solution:
	def longestPalindrome(self,s):

		def preProcess(s):
                	if not s:
                        	return ['^','$'] # if s is null, return ['^','$']
                	T=['^'] # process s by adding prefix ^ and postfix $ and each character followed by #
                	for c in s:
                        	T+=['#',c]
                	T+=['#','$']
                	return T
		
		T=preProcess(s)
		P=[0]*len(T) #initial P[i] to 0
		center,right=0,0
		for i in xrange(1,len(T)-1):
			i_mirrow = 2*center - i
			if right>i:
				P[i]=min(right-i,P[i_mirrow])
			else:
				P[i]=0
			while T[i+1+P[i]]== T[i-1-P[i]]:
				P[i]+=1
			if i+P[i]>right:
				center,right=i,i+P[i]
		max_i=0
		for i in xrange(1,len(T)-1):
			if P[i]>P[max_i]:
				max_i=i
		start=(max_i-1-P[max_i])/2 # how to get this formula? still have question
		return s[start: start+P[max_i]] # offset substring python		
if __name__=="__main__":
      print Solution().longestPalindrome("abbab")
