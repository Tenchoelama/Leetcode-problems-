# 500. Keyboard Row
# Easy
# 1.3K
# 1.1K
# Companies
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]


# def test(words):
    
#     res = []
    
#     first = "qwertyuiop"
#     second = "asdfghjkl"
#     third = "zxcvbnm"
    
#     for elm in words:
#         temp = ""
#         temp2 = ""
#         temp3 = ""
#         for l in elm:
#             if l.lower() in first:
#                 temp += l
#             if l.lower() in second:
#                 temp2 += l
#             if l.lower() in third:
#                 temp3 += l
                
#         print(temp)
#         print(temp2)
#         print(temp3)
#         if temp in words or temp2 in words or temp3 in words:
#             res.append(elm)
        
#     return res
        
    
    
    
# print(test(["Hello","Alaska","Dad","Peace"]))

#-----------------------------------------------------------------------------------------------------------------

