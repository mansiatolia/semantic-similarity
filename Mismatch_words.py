#!/usr/bin/env python
# coding: utf-8

# # Mismatch Words

# In[14]:


import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def mismatch_words(correct_city_filename,incorrect_city_filename):

    correct_city = pd.read_csv(correct_city_filename)
    incorrect_city =  pd.read_csv(incorrect_city_filename)

    ls_correct = [correct_city.name[i] for i in range(len(correct_city))]
    ls_incorrect = [incorrect_city.misspelt_name[i] for i in range(len(incorrect_city))]



    df1 = pd.DataFrame({'Col1':ls_correct})
    df2 = pd.DataFrame({'Col2':ls_incorrect})

    def fuzzy_merge(df_1, df_2, key1, key2, threshold=80, limit=2):
        """
        df_1 is the left table to join
        df_2 is the right table to join
        key1 is the key column of the left table
        key2 is the key column of the right table
        threshold is how close the matches should be to return a match, based on Levenshtein distance
        limit is the amount of matches that will get returned, these are sorted high to low
        """
        s = df_2[key2].tolist()

        m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit))    
        df_1['matches'] = m

        m2 = df_1['matches'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
        df_1['matches'] = m2

        return df_1


    output_data = fuzzy_merge(df1, df2, 'Col1', 'Col2', 80) ### Here 80 is the threshold limit of 80%
    output_data['country'] = pd.Series(correct_city['country'])
    output_data['id'] = pd.Series(correct_city['id'])
    return output_data

mismatch_words(input("correct city filepath"),input("incorrect city filepath"))

