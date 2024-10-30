import random

def randInt(min=0, max=100):
    if max < 0:
        return "Error: max cannot be less than 0"
    if min > max:
        return "Error: min cannot be greater than max"
    
   
    if min is None and max is None:
        num = random.random() * 100
    elif max is not None and min is None:
        num = random.random() * max
    elif min is not None and max is None:
        num = random.random() * (100 - min) + min
    else:
        num = random.random() * (max - min) + min

    return round(num)


print(randInt())               # should print a random integer between 0 and 100
print(randInt(max=50))        # should print a random integer between 0 and 50
print(randInt(min=50))        # should print a random integer between 50 and 100
print(randInt(min=50, max=500)) # should print a random integer between 50 and 500
print(randInt(min=500, max=50)) # should return error
print(randInt(max=-10))       # should return error
