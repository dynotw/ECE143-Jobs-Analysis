


import pandas as pd
import string
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def build_dict(x):
    '''
    Build a dictionary sorted in reverse order of word frequencies
    :param: x
    :type: pd.Series
    :return: dictionary
    '''
    assert isinstance(x,pd.Series)
    word_dict = defaultdict(int)
    stopwords = set(STOPWORDS)
    for i in range(len(x)):
        cur = x[i]
        if(isinstance(cur, str)):
            cur = cur.translate(str.maketrans('','',string.punctuation))
            cur = cur.lower()
            keys = cur.split()
            for key in keys:
                if(key not in stopwords):
                    word_dict[key] += 1
    dict_sorted = {k: v for k, v in sorted(word_dict.items(), key=lambda x: x[1],reverse=True)}
    return dict_sorted


Google = pd.read_csv("job_skills.csv")
Google_description = Google['Preferred Qualifications']

Facebook = pd.read_csv("facebook_jobs.csv")
Facebook_description = Facebook['responsibilities']

Amazon = pd.read_csv("amazon_jobs_dataset.csv")
Amazon_description = Amazon['DESCRIPTION']

Google_dict = build_dict(Google_description)

Facebook_dict = build_dict(Facebook_description)

Amazon_dict = build_dict(Amazon_description)

def plot_wordcloud(x, k):
    '''
    Plot the wordcloud graph
    :param: x, k
    :type: pd.Series, list
    '''
    assert isinstance(x,pd.Series)
    assert isinstance(k,list)
    assert len(k) >= 1
    unremoved = set()
    for i in k:
        unremoved.add(i)
    word_dict = defaultdict(int)
    for i in range(len(x)):
        cur = x[i]
        if(isinstance(cur, str)):
            cur = cur.translate(str.maketrans('','',string.punctuation))
            cur = cur.lower()
            keys = cur.split()
            for key in keys:
                if(key in unremoved):
                    word_dict[key] += 1
    dict_sorted = {k: v for k, v in sorted(word_dict.items(), key=lambda x: x[1],reverse=True)}
    wordcloud = WordCloud(background_color="white", width = 1000, height = 1000).generate_from_frequencies(dict_sorted)
    plt.figure(figsize=(20,20))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

Google_list = ['experience','management','confident','proactively','decisionmaking','comprehensive','supporting','illustrator','thrive','attitude','multitasking','enthusiasm','responsibility','innovative','credibly','timesensitive','teamwork','manner','competitive','leader','integrity','productive','focused','acumen','multitask','communication','ideas','detailoriented','distinctive','learning','insights','selfmotivated','troubleshooting','networking','interaction','thinker','critical','collaboration','language','selfstarter','passion','flexibility','strategy','judgment','creative','independent','professional','leadership','problemsolving','influence','analytical','understanding','interpersonal','interest','fastpaced']

Facebook_list = ['management','strategic','networking','empathy','professional','manner','rigorous','insights','active','trusted','unique','reliable','articulate','interaction','impactful','proactive','innovation','robust','positive','comprehensive','creative','novel','social','detailed','focused','troubleshooting','critical','sharing','analytical','coordination','competitive','responsible','supporting','contribute','integrity','collaboration','innovative','partnership','efficiency','leadership','experience','understanding','learning','influence','communication','effective']

Amazon_list = ['experience','management','critical','reliability','customerfacing','competitive','interacting','judgment','efficient','thrived','inventive','focused','flexible','collaborative','strategic','fastpaced','networking','robust','groundbreaking','creative','idea','comprehensive','hardworking','understanding','influence','innovative','leadership','support','responsible','unique','passionate']

plot_wordcloud(Google_description, Google_list)

plot_wordcloud(Facebook_description, Facebook_list)

plot_wordcloud(Amazon_description, Amazon_list)
