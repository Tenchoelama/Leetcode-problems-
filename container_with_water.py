# 11. Container With Most Water
# Medium
# 23.7K
# 1.3K
# Companies
# You are given an integer array height of length n. There are n vertical lines drawn such that the two 
# endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
# (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

def most_water(arr):
    
    p1, p2 = 0, len(arr)-1
    largest_space = 0
    
    while p1 < p2:
       
        temp = (p2-p1) * min(arr[p1],arr[p2])
        if temp > largest_space:
            largest_space = temp
        if arr[p2] >= arr[p1]:
            p1 += 1 
        elif arr[p2] <= arr[p1]:
            p2 -= 1 
    
    return largest_space     
            
        
        


#input = list 
#output = area of the shape(int)
#two pointer algorithm 
#define a variable that stores the largest container 
#while loop to go thru each elements and compare them with each other. 
#if statement to check if the area computed is larger than the one defined earlier 


print(most_water([1,1]))