class Solution:
	def isValid(self, s):
		stack=[]
		for i in range(len(s)):
			if s[i]=="(" or s[i]=="[" or s[i]=="{":
				stack.append(s[i])
			elif s[i]==")":
				if stack==[] or stack.pop()!="(":
					return False
			elif s[i]=="]":
                                if stack==[] or stack.pop()!="[":
                                        return False
			elif s[i]=="}":
                                if stack==[] or stack.pop()!="{":
                                        return False
		if stack:
			return False
		else:
			return True

if __name__=="__main__":
	print Solution().isValid("()[]{}")
	print Solution().isValid("(]")
	print Solution().isValid("[")
