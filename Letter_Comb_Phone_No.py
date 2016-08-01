class Solution:
	def letterCombinations(self, digits):
		if not digits:
			return []
		dic={
			0:"0", 1:"1",2:"abc",3:"def",4:"ghi",5:"jkl",
			6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
		ret=[""]
		for digit in digits:
			temp_list=[]
			for ch in dic[int(digit)]:
				for str in ret:
					temp_list.append(str+ch)
			ret = temp_list
		return ret

if __name__=="__main__":
	print Solution().letterCombinations("23")
