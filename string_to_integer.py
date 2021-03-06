class Solution(object):
    def atoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX =  2147483647
        INT_MIN = -2147483648
	
	result=0
	if not str:
		return result
	
	i=0
	while i<len(str) and str[i]==" ": #ignore space
		i+=1
	sign=1
	if str[i]=="+":
		i+=1
	elif str[i]=="-":
		sign=-1
		i+=1
	
	while i<len(str) and str[i]>='0' and str[i]<='9':
		result=result*10+ord(str[i])-ord('0')
		i+=1
	if sign==1 and result>INT_MAX:
		return INT_MAX
	if sign==-1 and result>abs(INT_MIN):
		return INT_MIN
	return sign*result

if __name__ == "__main__":
    print Solution().atoi("") 
    print Solution().atoi("-1")
    print Solution().atoi("2147483647") 
    print Solution().atoi("2147483648") 
    print Solution().atoi("-2147483648")  
    print Solution().atoi("-2147483649")  
