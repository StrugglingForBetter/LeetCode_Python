class Solution:
	def groupAnagrams(self, strs):
		map={}
		for word in strs:
			sortedword=''.join(sorted(word))
			map[sortedword]=[word] if sortedword not in map else map[sortedword]+[word]
		ret=[]
		for item in map:
			ret.append(map[item])
		return ret
if __name__=="__main__":
	print Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
