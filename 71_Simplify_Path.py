class Solution:
	def simplifyPath(self,path):
		stack=[]
		i=0
		res=''
		while i<len(path):
			end = i+1
			while end<len(path) and path[end]!="/":
				end+=1
			sub=path[i+1:end]
			if len(sub)>0:
				if sub=="..":
					if stack !=[]:stack.pop()
				elif sub!=".":
					stack.append(sub)
			i=end
		if stack==[]:return "/"
		for i in stack:
			res+="/"+i
		return res

class Solution2:
	def simplifyPath(self,path):
		path=path.split('/')
		cur='/'
		for i in path:
			if i=='..':
				if cur!='/':
					cur='/'.join(cur.split('/')[:-1])
					if cur=='':cur='/'
			elif i!='.' and i!='':
				cur+='/'+i if cur!='/' else i
		return cur


if __name__=="__main__":
	print Solution().simplifyPath("/home/")
	print Solution().simplifyPath("/a/./b/../../c/")
	print Solution().simplifyPath("/../")
	print Solution().simplifyPath("/home//foo/")
	print '-'*50
	print Solution2().simplifyPath("/home/")
        print Solution2().simplifyPath("/a/./b/../../c/")
        print Solution2().simplifyPath("/../")
        print Solution2().simplifyPath("/home//foo/")

