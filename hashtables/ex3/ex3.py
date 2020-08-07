def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
        # want to find similar values within a list of lists
    # have to scroll through all lists and append values 
    # make a count of each value,
    # return elements who have a count equal to length of all lists
    pre_result = []
    #almost = []
    result = []
    d = {}
    #This scrolls through every value in every list, and appends it to this 
    # pre-result array
    for lists in arrays:
        for values in lists:
            pre_result.append(values)
    # this then takes the pre-result array, adds it to dictionary, count of each number == value
    for x in pre_result:
        if x not in d:
            d[x] = 0

        d[x] +=1
    # This checks if the value equals the length of the arrays, 
    # because the numbers can only appear, or do only appear in this case once per list
    # then i append the key to result list, and return the key
    for key, value in d.items():
        if value == len(arrays):
            result.append(key)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
