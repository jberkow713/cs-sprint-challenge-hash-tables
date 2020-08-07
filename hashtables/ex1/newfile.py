import itertools
from itertools import product
'''
weights = [1, 2, 3, 7, 7, 9, 10]
limit = 14

result2 = []
result3 = []

d = {}

for x,v in enumerate(weights):
    result2.append(v)
    result3.append(x)

d = {key:value for key, value in zip(result2, result3)}

keys = d.keys()
for x in keys:
    
  

print(d)   
'''


from itertools import permutations
from itertools import combinations_with_replacement

numbers = [4, 4]

result = []
limit = 8
#solutions = [pair for pair in permutations(numbers, 2) if sum(pair) == 8]
#for x in solutions:
#    a = (x.sort)
#    result.append(a)

result = []
result2 = []
result3 = []
result4 = []
result5 = [1,0]    
    #create a dictionary with keys, and values for all weights
    # keys = weight values, values = weight indexes

for x,v in enumerate(numbers):
    result2.append(v)
    result3.append(x)

d = {key:value for key, value in zip(result2, result3)}

#if length < 2:
#    return None

for x in numbers:
    for y in numbers:
        if (limit-x) == y:
            result = [x,y]
            result.sort(reverse=True)  
for x in result:
    if result(x) == result(x+1):
        return result5
    
for x in result:
    for k,v in d.items():
        if k == x:
            result4.append(v)
            


    
print(result5)
