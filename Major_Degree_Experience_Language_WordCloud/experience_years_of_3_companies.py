#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from collections import defaultdict

# matplotlib for plotting
import matplotlib.pyplot as plt
# use ggplot style
plt.style.use('ggplot')
# seaborn for beautiful visualizations
import seaborn as sns
# regualar expression
import re
# print inline in this notebook
get_ipython().magic(u'matplotlib inline')


# In[2]:


df_amazon = pd.read_csv('./amazon.csv')
df_facebook = pd.read_csv('./facebook.csv')
df_google = pd.read_csv('./google.csv')


# In[5]:


def amazon_experience(df):
    '''
    Find preferred experience years of Amazon
    
    :param: df
    :type: pd.DataFrame
    
    :return: list
    '''
    assert isinstance(df, pd.DataFrame)
    df['Experience1'] = df['BASIC QUALIFICATIONS'].str.extract(r'([0-9]+) year')
    dff = df[['Experience1','Title']]
    dff = dff.dropna()
    exp = dff.Experience1.value_counts().iloc[:10].sort_values()
    exp_list = list(zip(exp,exp.index))
    exp_list += [(0, '11'), (0, '0'), (0, '12')]
    sorted_exp = sorted(exp_list, key=lambda x: int(x[1]), reverse=True)
    df['Experience2'] = df['BASIC QUALIFICATIONS'].str.extract(r'([0-9]) year')
    dff = df[['Experience2','Title']]
    dff = dff.dropna()
    exp = dff.Experience2.value_counts().iloc[:10].sort_values()
    exp_list = list(zip(exp,exp.index))
    for (count, year) in exp_list: 
        if int(year) <= 12:
            sorted_exp[len(sorted_exp) - int(year) - 1] = (sorted_exp[len(sorted_exp) - int(year) - 1][0] + count, year)
    named_exp = [(y + '+', x) for (x,y) in sorted_exp]
    return named_exp

def google_experience(df):
    '''
    Find preferred experience years of Google
    
    :param: df
    :type: pd.DataFrame
    
    :return: list
    '''
    assert isinstance(df, pd.DataFrame)
    df = df.rename(columns={'Minimum Qualifications': 'Minimum_Qualifications', 
                        'Preferred Qualifications': 'Preferred_Qualifications'})
    pd.isnull(df).sum()
    df = df.dropna(how='any',axis='rows')
    df = df[df.Company == 'Google']
    df['Experience1'] = df['Minimum_Qualifications'].str.extract(r'([0-9]+) year')
    dff = df[['Experience1','Category']]
    dff = dff.dropna()
    exp = dff.Experience1.value_counts().iloc[:10].sort_values()
    exp_list = list(zip(exp,exp.index))
    exp_list += [(0, '9'), (0, '11'), (0, '0')]
    sorted_exp = sorted(exp_list, key=lambda x: int(x[1]), reverse=True)
    df['Experience2'] = df['Minimum_Qualifications'].str.extract(r'([0-9]) year')
    dff = df[['Experience2','Category']]
    dff = dff.dropna()
    exp = dff.Experience2.value_counts().iloc[:10].sort_values()
    exp_list = list(zip(exp,exp.index))
    for (count, year) in exp_list: 
        if int(year) <= 12:
            sorted_exp[len(sorted_exp) - int(year) - 1] = (sorted_exp[len(sorted_exp) - int(year) - 1][0] + count, year)
    named_exp = [(y + '+', x) for (x,y) in sorted_exp]
    return named_exp

def facebook_experience(df):
    '''
    Find preferred experience years of Facebook
    
    :param: df
    :type: pd.DataFrame
    
    :return: list
    '''
    assert isinstance(df, pd.DataFrame)
    df['Experience1'] = df['minimum qualifications'].str.extract(r'([0-9]+)')
    dff = df[['Experience1','title']]
    dff = dff.dropna()
    exp = dff.Experience1.value_counts().iloc[:10].sort_values()
    exp_list = list(zip(exp,exp.index))
    exp_list += [(0, '9'), (0, '11'), (0, '0')]
    sorted_exp = sorted(exp_list, key=lambda x: int(x[1]), reverse=True)
    df['Experience2'] = df['minimum qualifications'].str.extract(r'([0-9]) year')
    dff = df[['Experience2','title']]
    dff = dff.dropna()
    exp = dff.Experience2.value_counts().iloc[:10].sort_values()
    exp_list = list(zip(exp,exp.index))
    for (count, year) in exp_list: 
        if int(year) <= 12:
            sorted_exp[len(sorted_exp) - int(year) - 1] = (sorted_exp[len(sorted_exp) - int(year) - 1][0] + count, year)
    named_exp = [(y + '+', x) for (x,y) in sorted_exp]
    return named_exp


# In[7]:


exp_amazon = amazon_experience(df_amazon)
exp_google = google_experience(df_google)
exp_facebook = facebook_experience(df_facebook)
exp_amazon.reverse()
exp_google.reverse()
exp_facebook.reverse()


# In[8]:


df = pd.DataFrame({'Amazon':[i[1] for i in exp_amazon], 
                           'Google':[i[1] for i in exp_google],
                      'Facebook':[i[1] for i in exp_facebook]}, 
                  index=[i[0] for i in exp_facebook]) 

df.plot.bar(figsize=(30, 18), color=['#fc910d', '#436EEE', '#32CD32'], width=0.8)
plt.legend(prop={'size':25, 'weight':'bold'})
plt.title('Preferred Experience Years', fontsize=30, weight='bold')
plt.xlabel('Experience Years', fontsize=30, weight='bold')
plt.ylabel('Popularity', fontsize=30, weight='bold')
plt.yticks(fontsize=28, weight='bold')
plt.xticks(fontsize=28, weight='bold', rotation=0)
plt.savefig('Preferred Experience Years.jpeg', bbox_inches = 'tight')
plt.show()


# In[ ]:




