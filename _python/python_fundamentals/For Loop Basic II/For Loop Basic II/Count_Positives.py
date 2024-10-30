def count_positive(lst):
    positive_count= sum(1 for num in lst if num > 0)
    lst[-1] = positive_count
    return lst


print(count_positive([-1, 1, 1, 1]))  
print(count_positive([1, 6, -4, -2, -7, -2]))  
