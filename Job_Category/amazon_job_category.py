import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

# load the data from csv
df = pd.read_csv('amazon_jobs_dataset.csv')

df = df.dropna(axis=0, how='any')
# clear the rows with NaN. axis=0 means delete the NaN, depending on the rows, axis=1 means columns
# 'any' means rows with NaN, 'all' means rows whose elements all are NaN

# get all the data from ['Title']
all_jobs = df['Title'].value_counts()

# the following code has three functions:
# 1. use 'Software Engineer or Manager' to replace all index which includes 'software', and count appearance times j
# 'Software Engineer or Manager' must Top1 job
# 2. use 'Others' to replace all left index (except Top4), and count appearance times
# 3. count Top2-4 obs

SDE= df[df['Title'].str.contains("Software") & df['Title'].str.contains("Engineer")]

SDM = df[df['Title'].str.contains("Software") & df['Title'].str.contains("Manager")]

Web = df[df['Title'].str.contains("Web")]

Data = df[df['Title'].str.contains("Data")]

pop=dict()
pop['Software Engineer']= len(SDE)
pop['Software Manager'] = len(SDM)
pop['Web Engineer'] = len(Web)
pop['Data Analyst'] = len(Data)
pop['Others'] = len(df)-len(SDE)-len(SDM)-len(Web)

popularity = pd.Series(pop)
popularity = popularity.sort_values(ascending=False)
print(popularity)


def pie_chart(data_name,title):
    assert isinstance(title, str)
    explode = [0.05, 0, 0, 0, 0]
    plt.pie(data_name,explode=explode,labels=popularity.index)
    # add a title, and set the size of plot
    plt.title(title, fontsize=24)
    # add 图例 and set its format
    percent = 100. * no_SDE / no_SDE.sum()
    labels = ['{0} - {1} - {2:2.2f} %'.format(i, j, h) for i, j, h in zip(no_SDE.index, no_SDE, percent)]
    plt.legend(labels,loc="upper right",bbox_to_anchor=(1.35,0.95),fontsize=18)
    # bbox_to_anchor,is the distance to left-bottom corner
    plt.tight_layout()
    # finally show the plot
    plt.show()

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
    # explode, explode one slice of pie chart
    explode=[0.05,0,0,0,0]

    plt.pie(data_name,labels=popularity.index, autopct='%1.1f%%',explode=explode,textprops={'fontsize':14},colors=color)

    # add a title, and set the size of plot
    plt.title(title, fontsize=24,weight='bold')
    # add legend, and set the format
    labels = ['{0} - {1}'.format(i,j) for i,j in zip(data_name.index, data_name)]
    # plt.legend(labels,loc="upper right",bbox_to_anchor=(1.35,0.9),fontsize=18)
    # finally show the plot
    plt.show()

if __name__ == '__main__':
    # pie_chart(no_SDE,title='Amazon Top5 Popular Job')
    pie_chart_1(popularity, title='Amazon Job Popularity',color = ['red','cyan','blue','green','wheat'])