def add_binary(a, b):
    
    res = ""
    carry = 0
    a, b = a[::-1], b[::-1]
    
    
    
    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0 
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0 

        total = digitA + digitB + carry 
        char = str(total % 2)
        res = char + res
        carry = total // 2
        
    if carry:
        res = "1" + res    
        
    return res 

print(add_binary("1010","1011"))

