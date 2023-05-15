
def two_sum(arr, target):
    
    d = {}
    l = []
    for i, num in enumerate(arr):
        ans = target - num 
        if ans in d:
            l.extend([d[ans], i])
            return l
        d[num] = i
   
            
    
print(two_sum([3,3],6))


        