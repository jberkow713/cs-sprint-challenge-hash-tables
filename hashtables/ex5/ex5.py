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
    
    
    for x in files:
        result2.append(x)
    
    for x in files:
        x2 = x.rsplit('/', 1)[-1] 
        result3.append(x2)  

    d = {key: value for key, value in zip(result2, result3)} 

    #for x in queries:
    #    result4.append(x)
    # so now we have a dictionary with full filepath, and ending of filepath
    # want to iterate through queries and match up queries with 
    # value in dictionary. If matches, return that correlating key to result 
    # array, and return array
    
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
