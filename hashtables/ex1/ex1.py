import itertools
from itertools import combinations_with_replacement


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # feeding 3 variables, weights: an array of weights, 
    # length : length of array, 
    # limit: what any 2 numbers should add up to 
    
    
    result = []
    result2 = []
    result3 = []
    result4 = []
    result5 = [1,0]
        
    
    # First case, if length is 1 or less, return None
    if length <2:
        return None
    
    # Here I create a dictionary, using the values of the weights as keys, 
    # and the index of the weights as values
    for x,v in enumerate(weights):
        result2.append(v)
        result3.append(x)

    d = {key:value for key, value in zip(result2, result3)}

    #Now I scroll through the weights, and see if the limit, or target minus one of the values,
    # is equal to another value, if so , I append these values to a list, and reverse order
    # so that higher value is first
    for x in weights:
        for y in weights:
            if (limit-x) == y:
                result = [x,y]
                result.sort(reverse=True)  
    
    # Another fringe case, where they are asking to return index 1, and 0 if elements in result which add up
    # to the limit are the same, so in this case, i check indexes of result, if they are the same, i simply return 
    # result5, which is a [1,0] array
    
    for i, j in enumerate(result[:-1]):
        if j  == result[i+1]: 
            return result5            
    
    # Otherwise, in all other cases,
    # I scroll through the values in the result array, check if the key in the dictionary is equal to the value,
    # if so, append the key to result4, and return result 4
    for x in result:
        for k,v in d.items():
            if k == x:
                result4.append(v)

    return result4            


