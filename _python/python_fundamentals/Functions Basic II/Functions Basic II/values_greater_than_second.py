def greater_than_second(lst):
    if len(lst) < 2:
        return False
    
    second_value =lst[1]
    new_list = [x for x in lst if x > second_value]
    
    print(len(new_list))
    return new_list
    
    
    
result1= greater_than_second([5,2,3,2,1,4])
print(result1) 

result2= greater_than_second([3])
print(result2)   