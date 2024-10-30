def maximum(numbers):
    if not numbers:
        return False
    
    max_val=numbers[0]
    for num in numbers:
        if num > max_val:
            max_val= num
     
    return max_val     


print(maximum([37,2,1,-9]))  
print(maximum([]))