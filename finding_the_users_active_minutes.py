# 1817. Finding the Users Active Minutes
# Medium
# 685
# 257
# Companies

# You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

# Return the array answer as described above.

 

# Example 1:

# Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
# Output: [0,2,0,0,0]
# Explanation:
# The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
# The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
# Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.
               
def test(logs, k):
    
    res = [0] * k
    d = {}
    
    for id, time in logs:
        if id not in d:
            d[id] = set()
        d[id].add(time)
        
    for id in d:
        j = len(d[id])
        res[j-1] += 1
        
    return res        
    
    
    
print(test([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))


#---------------------------------------------------------------------------------------------------------------------------------------------------