import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from matplotlib.patches import ConnectionPatch
def categories_dis(x):
    '''
    This function finds job categories distribution of amazon and subcategories of software engineer 
    '''
    assert isinstance(x,pd.core.frame.DataFrame)
    s=x
    x=x[x['Category'].str.contains('Software Engineering')] 
    cat={'Machine Learning Engineer':0,'Big Data Engineer':0,'Games Engineer':0,'Web Developer':0,'Network Engineer':0,'Cloud Engineer':0,'Other':0}
    n=x.shape[0]
    print(n)
    cat['Machine Learning Engineer']=s['Title'].str.contains('Machine Learning|Machine|Learning|Deep Learning').sum()   
    cat['Big Data Engineer']=s['Title'].str.contains('Big Data|Data').sum() 
    cat['Network Engineer']=s['Title'].str.contains('Network').sum()    
    
    cat['Web Developer']=s['Title'].str.contains('Web').sum()   
    cat['Software Development Manager']=x['Title'].str.contains('Software Development Manager|Manager').sum()   
    cat['Games Engineer']=s['Title'].str.contains('Game').sum()
    cat['Cloud Engineer']=x['Title'].str.contains('Cloud').sum()
    norm=sum(list(cat.values()))
    print(norm)
    cat['Other']==n-norm
    normalized_dic={nam[0]:nam[1]/500 for nam in cat.items()}
    res = sorted(normalized_dic.items(), key=lambda x: x[1], reverse=True)
    normalized_dic={nam[0]:nam[1] for nam in res}
  
    return cat
    
def amazon_job_graph(amazon):
 ''' 
  This file generates pie chart of all job cateogires of Amazon as well gives bar chart of subcateogires of software engineer
    I used str.contains to generate subcateogries of software developer engineer
    parameter:amazon is dataframe containing job categories 
    type: dataframe
 '''
 assert isinstance(amazon,pd.core.frame.DataFrame)
 
 '''
 Visualization of graphs
 '''
# style choice
 plt.style.use('fivethirtyeight')

# make figure and assign axis objects
 fig = plt.figure(figsize=(10,5))
 ax1 = fig.add_subplot(121)
 ax2 = fig.add_subplot(122)

# pie chart parameters
 
 ratios = [.64, .13, .23]
 labels = ['Software Engineer', 'Software Manager','Others']
 explode=[0.1,0,0]
# rotate so that first wedge is split by the x-axis
 angle = -180*ratios[0]
 angle = -180*ratios[0]
 wedge_a,labels_a,auto=ax1.pie(ratios, autopct='%1.1f%%', startangle=angle,
        explode=explode,colors=['r','b','g'],labels=labels )
 plt.setp(labels_a,weight='bold',fontsize=11)
 # bar chart parameters
 #Percentages of different subcatogries                                                                                                                                                                                                                                                nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn nnn nnn                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   )
 xpos = 0
 bottom = 0
 ratios = [.18, .15, .12, 0.1,0.09,0.36][::-1]
 width = .2
 colors = ['c','b','#ffcc99','#99ff99','m','y']

 for j in range(len(ratios)):
    height = ratios[j]
    ax2.bar(xpos, height, width, bottom=bottom, color=colors[j])
    ypos = bottom + ax2.patches[j].get_height()/2
    bottom += height
    ax2.text(xpos,ypos, "%d%%" %
        (ax2.patches[j].get_height()*100), ha='center')

 plt.title('Types of Software Engineer',weight='bold')
 plt.legend(('ML Engineer' , 'Web Developer','Big Data Engineer','Cloud Engineer','Network Engineer', 'Other'),fontsize=16,loc='upper right')
 plt.axis('off')
 plt.xlim(-2.5*width, 2.5*width)


# use ConnectionPatch to draw lines between the two plots
# get the wedge data for the first group
 theta1, theta2 = ax1.patches[0].theta1, ax1.patches[0].theta2
 center, r = ax1.patches[0].center, ax1.patches[0].r
 bar_height = sum([item.get_height() for item in ax2.patches])
 x = r*np.cos(math.pi/180*theta2)+center[0]
 y = np.sin(math.pi/180*theta2)+center[1]
 con = ConnectionPatch(xyA=(-width/2,bar_height), xyB=(x,y),
    coordsA="data", coordsB="data", axesA=ax2, axesB=ax1)
 con.set_color([0,0,0])
 con.set_linewidth(4)
 ax2.add_artist(con)

 x = r*np.cos(math.pi/180*theta1)+center[0]
 y = np.sin(math.pi/180*theta1)+center[1]
 con = ConnectionPatch(xyA=(-width/2,0), xyB=(x,y),
       coordsA="data", coordsB="data", axesA=ax2, axesB=ax1)
 con.set_color([0,0,0])
 ax2.add_artist(con)
 con.set_linewidth(4)

 plt.show()
 

