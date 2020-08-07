def has_negatives(a):
    
    list_1 = []
    #list_2 = []
    
    d = {}
    result = []

    for x in a:
        if x > 0:
            list_1.append(x)

        elif x < 0:
            y = (x *-1)
            list_1.append(y)
    
    for x in list_1:

        if x not in d:
            d[x] = 0

        d[x] +=1   

    for key, value in d.items():
        if value >1:
            result.append(key)         



                    

    # Your code here
    # so looking for the positive values in the list that have 
    # their negative selves, return positive values
    # so a represents an array of integers

    # you can make two arrays, one for positives, and one list for negatives
    # then take list of negative numbers, multiply them by -1 and insert them into a 
    # third list along with the list of positive integers from the first list
    
    #  scroll through the third list, append each value and their 
    # count to a dictionary, then iterate through dictionary, return any key who's
    # count, or value, is > 1 into a 4th array called result, and return that result 
    #return d
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
