import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

# load the data from csv
df = pd.read_csv('facebook_jobs (1).csv')

df = df.dropna(axis=0, how='any')
# clear the rows with NaN. axis=0 means delete the NaN, depending on the rows, axis=1 means columns
# 'any' means rows with NaN, 'all' means rows whose elements all are NaN

# get all the data from ['Title']
all_jobs = df['Title'].value_counts()
print(all_jobs)

all_category = df['Category'].value_counts()
print(all_category)
# the following code has three functions:
# 1. use 'Software Engineer or Manager' to replace all index which includes 'software', and count appearance times j
# 'Software Engineer or Manager' must Top1 job
# 2. use 'Others' to replace all left index (except Top4), and count appearance times
# 3. count Top2-4 obs

# SD=df.loc[df['Category'].str.contains("Software")]
SDE= df[df['Title'].str.contains("Software") & df['Title'].str.contains("Engineer")]
#
SDM = df[df['Title'].str.contains("Software") & df['Title'].str.contains("Manager")]
#
AR = df[df['Category'].str.contains("AR|VR")]
Marketing = df.loc[df['Category'].str.contains('Marketing')]

HR=df.loc[df['Title'].str.contains("HR|Recruiting|Recruiter|Sourcer")]
#
Data = df[df['Title'].str.contains("Data")]
#
print(Data.index)

all = pd.concat([SDE,AR,Marketing,HR,Data], axis=1)
other=df.drop(all.index)

pop=dict()
# pop['SD']=len(SD)
pop['HR']=len(HR)
pop['Software Engineer']= len(SDE)
pop['AR/VR Engineer'] = len(AR)
pop['Data Analyst'] = len(Data)
pop['Sales & Marketing']=len(Marketing)
pop['Others']=len(other)

popularity = pd.Series(pop)
popularity = popularity.sort_values(ascending=False)
print(popularity)


def pie_chart_1(data_name,title,color):
    '''

    :param data_name: pd.Series, the data which need to be showed
    :param title: str, name of graph tittle
    :param color: list filled with str, the color of slices in pie chart
    :return: a pir chart
    '''

    assert isinstance(title, str)
    assert isinstance(data_name, pd.Series)
    assert isinstance(color, list)

    explode=[0,0,0,0,0.1, 0]

    plt.pie(data_name,labels=popularity.index, autopct='%1.1f%%',explode=explode,textprops={'fontsize':16},colors=color)

    # add a title, and set the size of plot
    plt.title(title, fontsize=24,weight='bold')

    # plt.legend(labels,loc="upper right",bbox_to_anchor=(1.35,0.9),fontsize=18)
    # finally show the plot
    plt.show()

if __name__ == '__main__':
    # pie_chart(no_SDE,title='Amazon Top5 Popular Job')
    print(popularity)
    pie_chart_1(popularity, title='Facebook Job Popularity',color = ['cyan','green','blue','wheat','red','teal'])