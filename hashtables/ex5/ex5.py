# Your code here

import os 
from urllib.parse import urlparse

def finder(files, queries):


    """
    YOUR CODE HERE
    """
    # Your code here
    # so basically you have 2 arrays, files, and queries,
    # if queries is found in ANY part of files, 
    # append the files to result, return the result

    # take queries letter by letter to a list
    # 
    d = {}
    
    result = []
    result2 = []
    result3 = []
    #result4 = []
    
    # add full files to result 2
    for x in files:
        result2.append(x)
    #split end of filepath, add to result 3
    for x in files:
        x2 = x.rsplit('/', 1)[-1] 
        result3.append(x2)  
    #create dictionary with full filepaths as key, and ending of filepaths as value

    d = {key: value for key, value in zip(result2, result3)} 

    #scroll through keys and values in dictionary, if value = query, append the key
    
    for k,v in d.items():
        for x in queries:
            if v == x:
                result.append(k)

    #for x in result4:
    #    for k,v in d.items():
    #        if x == v:
    #            result.append(k) 
     
    return result   


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
