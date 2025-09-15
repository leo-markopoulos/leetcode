class Solution:
    def intToRoman(self, num):
        numerals = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL', 10 : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV', 1 : 'I'}
        result = ''
        for current_num in numerals:
            while num >= current_num:
                num -= current_num
                result += numerals[current_num]
        
        return result