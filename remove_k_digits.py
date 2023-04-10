# 402. Remove K Digits
# Medium
# 7.3K
# 308
# Companies
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest


# def removeKDigits(num, k):
    
#    stack = []
   
#    for digit in num:
       
#        if stack and k and digit < stack[-1]:
#            stack.pop()
#            k -= 1
           
#        stack.append(digit)
       
#    if k:
#         answerstack = answerstack[:-k]
        
#    return ''. join(stack)
        
        

# print(removeKDigits("10200", 1))