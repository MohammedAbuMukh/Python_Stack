def minimum(numbers):
    if not numbers:
        return False
    min_val=numbers[0]
    for num in numbers:
        if num < min_val:
            min_val=num
    
    return min_val        


print(minimum([])) 
print(minimum([7,9,8,6]))       