from fuzzywuzzy import fuzz
import itertools

# Download Fuzzywuzzy library. https://github.com/seatgeek/fuzzywuzzy
# The library can be installed with pip. pip install fuzzywuzzy[speedup]
# Run the function fuzz_matching_name. The two names are given as input argument to the function. The function computes
# Full Match and Partial Match. If the Partial Match is above 90, it is a match otherwise it is not a match. This criteria can 
# be changed based on the performance in the real world application. The output is printed on the screen and is also returned
# as full_match, partial_match value that can be stored in a variable.

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def new_match_function(a,b):
    full_match=fuzz.ratio(a,b)
    partial_match= fuzz.partial_ratio(a,b)
    if partial_match<=90:
        match=False
    else:
        match=True
             
    #print('Full Match Percentage is:',full_match)
    #print('Partial Match Percentage is:',partial_match)
    return full_match,partial_match,match



def fuzz_matching_name(a,b):
    a = a.lower()
    b = b.lower()
    c = (a.split())
    d = (b.split())
    y = list(itertools.permutations(c))
    z = list(itertools.permutations(d))
    
    for i in y:
        for j in z:
        #print(i)
        #print(j)
            p = convertTuple(i)
            q = convertTuple(j)
            full_match,partial_match,match=new_match_function(p,q)
            if match==True:
                print('\n')
                print('Partial Match criteria fulfilled')
                print('Match Percentage is:',full_match) 
                print('Partial Match Percentage is:',partial_match)
                return full_match,partial_match
    
    print('\n')
    print('Match is less likely because partial match is below 90')
    print('Match Percentage is:',full_match) 
    print('Partial Match Percentage is:',partial_match)
    return full_match,partial_match