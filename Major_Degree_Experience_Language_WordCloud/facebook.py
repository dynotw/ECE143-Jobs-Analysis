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


# read the data set using pandas .read_csv() method
df = pd.read_csv('./facebook.csv')
# print the top 5 row from the dataframe
df.head()


# In[3]:


def histogram_h(data_name,title,xlabel='Popularity',ylabel='Country', color=None):
    '''
    To create vertical histograms
    
    :param: data_name
    :type: pd.Series
    :param: title
    :type: str
    :param: xlabel
    :type: str
    :param: ylabel
    :type: str
    :param: color
    :type: str
    '''
    assert isinstance(data_name, pd.Series)
    assert isinstance(title, str)
    assert isinstance(xlabel, str)
    assert isinstance(ylabel, str)
    assert isinstance(color, str)
    data_name = data_name[::-1]
    data_name.plot.barh(figsize=(15, 15), color=color)
    plt.title(title, fontsize=27, weight='bold')
    plt.xlabel(xlabel, fontsize=30, weight='bold')
    plt.ylabel(ylabel, fontsize=30, weight='bold')
    plt.yticks(fontsize=24, weight='bold')
    plt.xticks(fontsize=24, weight='bold')
    plt.savefig(title + ".jpeg", bbox_inches = 'tight')
    plt.show()
    
def histogram(data_name,title,ylabel='Popularity',xlabel='Country', color=None):
    '''
    To create horizontal histograms
    
    :param: data_name
    :type: pd.Series
    :param: title
    :type: str
    :param: xlabel
    :type: str
    :param: ylabel
    :type: str
    :param: color
    :type: str
    '''
    assert isinstance(data_name, pd.Series)
    assert isinstance(title, str)
    assert isinstance(xlabel, str)
    assert isinstance(ylabel, str)
    assert isinstance(color, str)
    data_name = data_name[::-1]
    data_name.plot.bar(figsize=(15, 15), color=color)
    plt.title(title, fontsize=27, weight='bold')
    plt.xlabel(xlabel, fontsize=30, weight='bold')
    plt.ylabel(ylabel, fontsize=30, weight='bold')
    plt.yticks(fontsize=24, weight='bold')
    plt.xticks(fontsize=24, weight='bold', rotation=0)
    plt.savefig(title + ".jpeg", bbox_inches = 'tight')
    plt.show()
    
def pie_chart(data_name,title):
    '''
    Create pie chart by matplotlib
    
    :param: data_name
    :type: pd.Series
    :param: title
    :type: str
    '''
    assert isinstance(data_name, pd.Series)
    assert isinstance(title, str)

    explode=[0.03,0.03,0.03]
    plt.figure(figsize=(10,10))
    plt.pie(data_name,autopct='%1.1f%%',explode=explode, textprops={'fontsize':24,'weight': 'bold'})
    plt.title(title, fontsize=25, weight='bold')
    labels = ['{0}'.format(i) for i in data_name.index]
    plt.legend(labels,loc="upper right",bbox_to_anchor=(1.35,0.9),fontsize=20)
    plt.savefig(title + ".jpeg", bbox_inches = 'tight')
    plt.show()

def list_to_series(lst):
    '''
    Convert list to pd.Series
    
    :param: lst
    :type: list
    
    :return: pd.Series
    '''
    assert isinstance(lst, list)
    zlst = list(zip(*lst))
    res = pd.Series(zlst[1], index = zlst[0])
    return res


# In[4]:


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
        print(len(sorted_exp) - int(year))
        sorted_exp[len(sorted_exp) - int(year) - 1] = (sorted_exp[len(sorted_exp) - int(year) - 1][0] + count, year)
named_exp = [(y + '+', x) for (x,y) in sorted_exp]
print(named_exp)
histogram(list_to_series(named_exp), 'Facebook Preferred Experience Years', xlabel='Experience Years', color='#436EEE')


# In[5]:


def extract_topk_data(targets_list, words):
    '''
    find the topk frequent data points
    
    :param: targets_list
    :type: list
    :param: words
    :type: list
    
    :return: list
    '''
    assert isinstance(targets_list,list)
    assert isinstance(words,list)
    popularity = dict((x,0) for x in targets_list)
    for word in words:
        if word in popularity:
            popularity[word] += 1
    sorted_popularity = sorted(popularity.items(), key=lambda x: x[1], reverse=True)
    return sorted_popularity


def preferred_programming_languages(panda_read_data):
    '''
    find the topk preferred programming languages
    
    :param: panda_read_data
    :type: dataframe
    
    :return: list
    '''
    assert isinstance(panda_read_data,pd.DataFrame)
    languages = ['swift','matlab','mongodb','hadoop','cosmos', 
                      'sql','spark', 'pig', 'python', 'java', 
                      'c++', 'php', 'javascript', 'objectivec', 'ruby', 
                      'perl','c','c#']
    qualifications = panda_read_data['minimum qualifications'].tolist()
    words = "".join(re.sub('[·,-/’()]', '', str(v)) for v in qualifications).lower().split(' ')
    return extract_topk_data(languages, words)

def preferred_degrees(panda_read_data):
    '''
    find the topk preferred degrees
    
    :param: panda_read_data
    :type: dataframe
    
    :return: list
    '''
    assert isinstance(panda_read_data,pd.DataFrame)
    degrees = ["BA", "Bachelor", "BS", "PhD", "MS", "Master"]
    qualifications = panda_read_data['minimum qualifications']
    res = {"Bachelor": 0, "Master": 0, "PhD": 0}
    for k in degrees:
        v = qualifications.str.contains(k).sum()
        if k == "BA" or k == "Bachelor" or k == "BS":
            res["Bachelor"] += v
        elif k == "MS" or k == "Master":
            res["Master"] += v
        elif k == "PhD":
            res["PhD"] += v
    res = sorted(res.items(), key=lambda x: x[0], reverse=True)
    return res

def preferred_majors(panda_read_data):
    '''
    find the topk preferred majors
    
    :param: panda_read_data
    :type: dataframe
    
    :return: list
    '''
    assert isinstance(panda_read_data,pd.DataFrame)
    majors = ["Computer Science", "Computer Engineering", "CS", "CE", 
              "Electrical Engineering","EE", "MIS", "CIS", "Management Information Systems", 
              "Mathematics", "Computer Information Systems",
              "Math", "Physics", "Psychology", "psychology", "Business", "business", "Finance", "finance",
             "Account", "account", "Statistics", "statistics", "Marketing", "marketing", "Advertising", "advertising"]
    qualifications = panda_read_data['minimum qualifications'].tolist()
    
    popularity = {"Computer Science":0, "Computer Engineering":0, "Electrical Engineering":0,
                 "Mathematics":0, "Management Information Systems": 0, "Computer Information Systems": 0,
                 "Psychology":0, "Business":0, "Finance":0, "Account":0, "Physics":0, "Statistics":0, "Marketing":0, "Advertising":0}
    for qualification in qualifications:
        if type(qualification) is not str:
            continue
        for major in majors:
            if major in qualification:
                if major == "Computer Science" or major == "CS":
                    popularity["Computer Science"] += 1
                elif major == "Computer Engineering" or major == "CE":
                    popularity["Computer Engineering"] += 1
                elif major == "Electrical Engineering" or major == "EE":
                    popularity["Electrical Engineering"] += 1
                elif major == "Management Information Systems" or major == "MIS":
                    popularity["Management Information Systems"] += 1
                elif major == "Computer Information Systems" or major == "CIS":
                    popularity["Computer Information Systems"] += 1
                elif major == "Math" or major == "Mathematics":
                    popularity["Mathematics"] += 1
                elif major == "Physics":
                    popularity["Physics"] += 1 
                elif major == "Psychology" or major == "psychology":
                    popularity["Psychology"] += 1
                elif major == "Business" or major == "business":
                    popularity["Business"] += 1
                elif major == "Finance" or major == "finance":
                    popularity["Finance"] += 1
                elif major == "Account" or major == "account":
                    popularity["Account"] += 1
                elif major == "Statistics" or major == "statistics":
                    popularity["Statistics"] += 1
                elif major == "Marketing" or major == "marketing":
                    popularity["Marketing"] += 1
                elif major == "Advertising" or major == "advertising":
                    popularity["Advertising"] += 1
    return sorted(popularity.items(), key=lambda x: x[1], reverse=True)


# In[6]:


temp = preferred_programming_languages(df)
languages = [(x.capitalize(), y) for (x,y) in temp]
for (x,y) in languages:
    index = languages.index((x,y))
    if x == 'Sql':
        languages[index] = ('SQL', y)
        print(languages[index])
    if x =='Php':
        languages[index] = ('PHP', y)
    if x =='Mongodb':
        languages[index] = ('MongoDB', y)
    if x =='Objectivec':
        languages[index] = ('ObjectiveC', y)
    if x =='Javascript':
        languages[index] = ('JavaScript', y)
histogram_h(list_to_series(languages), 'Facebook Preferred Programming Languages', ylabel='Programming Languages', color='#436EEE')


# In[7]:


degrees = preferred_degrees(df)
pie_chart(list_to_series(degrees), 'Facebook Preferred Degrees')


# In[8]:


majors = preferred_majors(df)
histogram_h(list_to_series(majors), 'Facebook Preferred Majors', ylabel='Majors', color='#436EEE')


# In[9]:


get_ipython().system(u'pip install wordcloud')


# In[10]:


skills_1 = ['SDN', 'Android', 'Cloud', 'Machine Learning', 'Front-end', 'Back-end', 'Test', 'Deep Learning', 
           'Video', 'Image', 'Distributed Systems', 'User Interface', 'Virtualization', 'Linux', 'Big Data',
           'SaaS', 'PaaS', 'IaaS', 'IOS', 'VPN', 'Chrome', 'Unix', 'Database', 'Visualization', 'Artificial Intelligence',
           'Security', 'GPU programming', 'Container Management', 'Web Development', 'Infrastructure',
           'Advisory Program', 'Data Mining', 'Statistic Analysis', 'Commerce Engine', 'AutoCAD', 'AWS', 'RPM Packaging',
           'AJAX', 'React', 'Kafka', 'Natural Language Processing', 'Embedded', 'Git', 'Dynamo DB', 'Server-less', 'ElasticSearch',
           'API', 'Audio', 'TCP/IP', 'MapReduce', 'Speech Enhancement', 'Data Analytics', 'TensorFlow', 
           'Scikit-Learn', 'FPGA', 'Verilog', 'Web Technology', 'Quantitative Analysis', 'ML', 'Unity', 'Angular', 'Vue',
           'Compiler', 'LLVM', 'GCC', 'Computer Vision', 'NLP', 'AR/VR', 'Server', 'Client', 'Game',
           'Neural Network']
skills_2 = [i.lower() for i in skills_1]
skills = {}
for skill in skills_1:
    count = df['minimum qualifications'].str.contains(skill).sum()
    skills[skill] = count
for skill in skills_2:
    count = df['minimum qualifications'].str.contains(skill).sum()
    index = skills_2.index(skill)
    skills[skills_1[index]] += count

remove_list = []    
for skill in skills:
    if skills[skill] == 0:
        remove_list.append(skill)
for skill in remove_list:
    skills.pop(skill)


# In[11]:


from wordcloud import WordCloud, ImageColorGenerator

wordcloud = WordCloud(background_color="white",width=1000, height=1000, margin=0).generate_from_frequencies(skills)
# Display the generated image:
plt.figure(figsize=(20,20))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.savefig("facebook_wordcloud.png")
plt.show()


# In[ ]:




