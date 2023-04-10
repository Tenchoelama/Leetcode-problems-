# 7. Reverse Integer
# Medium
# 10.1K
# 11.8K
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321


def reverseInteger(num):
    
    max_int = 2**31 -1
    min_int = -2**31
    
    if num == 0:
        return 0 
    
    if num < 0:
        str_num = str(num)
        str_num1 = str_num[0]
        temp = str_num.replace('-',"")
        temp = temp[::-1]
        str_num1 += temp 
        after = int(str_num1)
        if after > max_int or  after < min_int:
            return 0
        else:
            return after
        
    else:
        before = str(num)  
        after = int("".join(reversed(before)))
        if after > max_int or  after < min_int:
            return 0
        else:
            return after
    
    
print(reverseInteger(-123))