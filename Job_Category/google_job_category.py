import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# use the 'ggplot'
plt.style.use("ggplot")

# load the data from csv
df = pd.read_csv('google.csv')

df = df.dropna(axis=0, how='any')
# clear the rows with NaN. axis=0 means delete the NaN, depending on the rows, axis=1 means columns
# 'any' means rows with NaN, 'all' means rows whose elements all are NaN

# get all the data from ['Category']
all_category=df['Category'].value_counts()
Top5=all_category[:4]
left=all_category[5:]
Top5['Software Engineer'] = all_category['Software Engineering']
Top5['Others']=0
for i in left.index:
    Top5['Others']+=left[i]
Top5['Others']=Top5['Others']- Top5['Software Engineer']
Top5['Software Engineer'] = Top5['Software Engineer'] + 981

Top5.index=['Sales & Account Manager', 'Marketing & Communications', 'Finance', 'Technician', 'Software Engineer', 'Others']
Top5=Top5.sort_values(ascending=False)
print(Top5)

def pie_chart(data_name,title,color):
    '''

    :param data_name: pd.Series, the data which need to be showed
    :param title: str, name of graph tittle
    :param color: list filled with str, the color of slices in pie chart
    :return: a pir chart
    '''
    assert isinstance(title, str)
    assert isinstance(data_name,pd.Series)
    assert isinstance(color,list)
    # explode, explode one slice of pie chart
    explode=[0.05,0,0,0,0,0]

    plt.pie(data_name,labels=Top5.index, autopct='%1.1f%%',explode=explode,textprops={'fontsize':18},colors=color)
    # data_name is the values of series，data_name.index is the index of series

    # add a title, and set the size of plot
    plt.title(title, fontsize=24,weight='bold')

    # finally show the plot
    plt.show()

if __name__ == '__main__':
    pie_chart(Top5,title='Google Job Popularity',color = ['red','cyan','blue','green','teal','wheat'])
    print('type of Top5', type(Top5))
