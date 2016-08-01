class Solution:
	def TextJustify(self, words,L):
		res=[]
		i=0
		while i<len(words):
			size=0;begin=i
			while i<len(words):
				newsize=len(words[i]) if size==0 else size+len(words[i])+1
				if newsize<=L:size=newsize
				else: break
				i+=1
			spacecount=L-size
			if i-1-begin>0 and i<len(words):
				everycount=spacecount/(i-1-begin)
				spacecount%=i-1-begin
			else:
				everycount=0
			j=begin
			while j<i:
				if j==begin:s=words[j]
				else:
					s+=' '*(everycount+1)
					if spacecount>0 and i<len(words):
						s+=' '
						spacecount-=1
					s+=words[j]
				j+=1
			s+=' '*spacecount
			res.append(s)
		return res
if __name__=="__main__":
	words=["This","is","an","example","of","text","justification."]
	print Solution().TextJustify(words,16)
