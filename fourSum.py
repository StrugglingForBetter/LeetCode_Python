class Solution:
	def fourSum(self,num,target):
		numLen, res, dic=len(num),set(),{}
		if numLen<4:
			return []
		num.sort()
		for p in range(numLen-1):
			for q in range(p+1,numLen):
				if num[p]+num[q] not in dic:
					dic[num[p]+num[q]]=[(p,q)]
				else:
					dic[num[p]+num[q]].append((p,q))
		
		for i in range(numLen-3):
			for j in range(i+1,numLen-2):
				T=target-num[i]-num[j]
				if T in dic:
					for k in dic[T]:
						if k[0]>j:res.add((num[i],num[j],num[k[0]],num[k[1]]))
		return [list(i) for i in res]

if __name__=="__main__":
	print Solution().fourSum([1,0,-1,0,-2,2],0)
