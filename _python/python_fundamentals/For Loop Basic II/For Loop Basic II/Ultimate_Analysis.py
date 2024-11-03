def ultimate_analysis(numbers):
    if not numbers:
        return {}
    
    sum_total=0
    min_val=numbers[0]
    max_val=numbers[0]
    count=0
    
    for num in numbers:
        #claculate the summation 
        sum_total+=num
        #calculate minimumn value
        if num < min_val:
            min_val= num
        #calculate max value
        if num > max_val:
            max_val= num
        #count numbers of elemnets in list
        count += 1
        
    avg = sum_total/count  
    
    result = {
        'sumTotal': sum_total,
        'average' : avg,
        'minimum' : min_val,
        'maximum' : max_val,
        'length'  : count
    }  
    
    return result
                

print(ultimate_analysis([37, 2, 1, -9]))  
print(ultimate_analysis([]))  

    