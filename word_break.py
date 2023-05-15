# 139. Word Break
# Medium
# 13.8K
# 582
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

def word_break(s,wordDict):

    res = ""
    
    temp = s[:]
    p = 0
    for e in wordDict:
        if e in temp:
            res += e * s.count(e) 
            p += len(e)
            temp = s[p:]
    print(res)        
    if len(res) == len(s):
        return True
    return False 

print(word_break("cars", ["car","ca","rs"]))