import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from matplotlib.patches import ConnectionPatch
import math
def categories_dis_g(x):
    '''
    This function finds job categories distribution of google and subcategories of software engineer 
    '''
    assert isinstance(x,pd.core.frame.DataFrame)
    xS=x.loc[x['Category'].isin(['Technical Solutions','Software Engineering','Hardware Engineer'])]
    xF=x.loc[x['Category'].isin(['Finance'])]
    xSA=x.loc[x['Category'].isin(['Sales & Account Management'])]
    cat={'Software and Hardware Engineering':0,'Finance':0,'Sales and Account Management':0}
    
    cat['Software and Hardware Engineering']=xS.shape[0]
    cat['Sales and Account Management']= xF.shape[0] 
    cat['Finance']=xSA.shape[0]
 
    cat['Cloud Engineering']=x['Category'].str.contains('Cloud').sum()    
    cat['Big Data']=x['Category'].str.contains('Big Data|Data').sum()    
    
    cat['Network Engineer']=x['Title'].str.contains('Network').sum()   
    cat['Machine Learning Engineer']=x['Title'].str.contains('Machine Learning|Learning|Deep Learning').sum()   
    cat['Research Scientist']=x['Title'].str.contains('Research Intern').sum()
    norm=sum(list(cat.values()))

    normalized_dic={nam[0]:nam[1]/norm for nam in cat.items()}
    res = sorted(normalized_dic.items(), key=lambda x: x[1], reverse=True)
    normalized_dic={nam[0]:nam[1] for nam in res}
  
    return normalized_dic
def google_job_graph(amazon):
 ''' 
  This file generates pie chart of all job cateogires of Google as well gives bar chart of subcateogires of software engineer
    I used str.contains to generate subcateogries of software developer engineer
    parameter:google is dataframe containing job categories 
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
 ratios = [.33, .15, .10,0.24,0.14,0.04]
 labels = ['Software Engineer', 'Technician', 'Finance','Marketing and Communication','Sales &Account Manager','Other']
 explode=[0.1,0,0,0,0,0]


# pie chart parameters

# rotate so that first wedge is split by the x-axis
 angle = -180*ratios[0]
 angle = -180*ratios[0]
 wedge_a,labels_a,auto=ax1.pie(ratios, autopct='%1.1f%%', startangle=angle,
        explode=explode,colors=['r','c','m','cadetblue','olive','g'],labels=labels )
 plt.setp(labels_a,weight='bold',fontsize=11)   
# bar chart parameters                                                                                                                                                                                                                                                nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn nnn nnn                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   )
 xpos = 0
 bottom = 0
 ratios = [.25, 0.22,.14, .07,0.06,0.26][::-1]
 width = .2
 colors = ['#ffcc99','#99ff99','c','b','m','y'][::-1]


 for j in range(len(ratios)):
    height = ratios[j]
    ax2.bar(xpos, height, width, bottom=bottom, color=colors[j])
    ypos = bottom + ax2.patches[j].get_height()/2
    bottom += height
    ax2.text(xpos,ypos, "%d%%" %
        (ax2.patches[j].get_height()*100), ha='center')

 plt.title('Types of Software Engineer',weight='bold')
 plt.legend(('Big Data' , 'Cloud Engineer','ML Engineer','Web Engineer','Network Engineer', 'Other'),fontsize=16,loc='upper right')
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



