class intToEnglish:
    def __init__(self):
        self.less20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousand = ["", "Thousand", "Million", "Billion"]

    def intToWord(self, nums):
        pass

    def helper(self, nums):
        
        if nums < 20:
            return  self.less20[nums]
        elif nums < 100:
            return  (self.tens[nums // 10] + " " + self.helper(nums%10)).strip()
        elif nums < 1000:
            return  (self.less20[nums // 100] + " Hundred " + self.helper(nums % 100)).strip()
        elif nums < 1000000:
            return  (self.helper(nums // 1000) + " Thousand " +  self.helper(nums % 1000)).strip()
        elif nums < 1000000000:
            return  (self.helper(nums // 1000000) + " Million " + self.helper(nums % 1000000)).strip()
        else:
            return (self.helper(nums // 1000000000) + " Billion " + self.helper(nums % 1000000000)).strip()
        
        
    def main(self, nums):
        res = self.helper(nums)
        if nums == 0:
            return "Zero"
        else:
            return res.strip()
 

i = intToEnglish()
print(i.helper(100000))