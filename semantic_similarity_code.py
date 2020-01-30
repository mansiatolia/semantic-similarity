#!/usr/bin/env python
# coding: utf-8

# # Computes the semantic similarity and return the similar sentences together.

# In[3]:


import numpy as np
import pandas as pd
def similarity(filepath):
    def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
        """ levenshtein_ratio_and_distance:
            Calculates levenshtein distance between two strings.
            If ratio_calc = True, the function computes the
            levenshtein distance ratio of similarity between two strings
            For all i and j, distance[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        """
        # Initialize matrix of zeros
        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                else:
                    # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                    # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                     distance[row][col-1] + 1,          # Cost of insertions
                                     distance[row-1][col-1] + cost)     # Cost of substitutions
        if ratio_calc == True:
            # Computation of the Levenshtein Distance Ratio
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:
            return "The strings are {} edits away".format(distance[row][col])


    ls = []
    ### Directory path to read the file
    f = open(filepath, "r")  
    ls.append(f.read())
    d = [x.strip().split("\n") for x in ls]
    result = []
    for el in d:
         result = result + el 
    ls_final_new = []
    for i in range(len(result)):
        ls1 = []
        ls3=[]
        ls2 = []
        val = 0
        ls_final = []
        for j in range(len(result)):
            Distance = levenshtein_ratio_and_distance(result[i],result[j])
            Ratio = levenshtein_ratio_and_distance(result[i],result[j],ratio_calc = True)
            if Ratio == 1.0:
                pass
            else:
                ls1.append(Ratio)

                if val < max(ls1):
                    val = max(ls1)
                    sent = result[j]
                #print(result[i],"----",result[j],'-----',Ratio)
        # val = max(ls1)
        ls2.append(val)
        ls3.append(sent)
        ls_final.append(result[i])
        ls_final.append(sent)
        ls_final_new.append(ls_final)

    return(ls_final_new)
similarity(input("enter the file path"))


# In[ ]:




