class Solution(object):

    def intToRoman(self, num):

        """

        :type num: int

        :rtype: str

        """

        chart=[

            ["","I","II","III","IV","V","VI","VII","VIII","IX"],

            ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],

            ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],

            ["","M","MM","MMM"]

            ]

        roman=""

        roman+=chart[3][num/1000%10]

        roman+=chart[2][num/100%10]

        roman+=chart[1][num/10%10]

        roman+=chart[0][num%10]

        return roman

if __name__=="__main__":
	print Solution().intToRoman(3999)
