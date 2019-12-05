import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from matplotlib.patches import ConnectionPatch
def facebook_job_graph(facebook):
 ''' 
  This file generates pie chart of all job cateogires of Facebook as well gives bar chart of subcateogires of software engineer
    I used str.contains to generate subcateogries of software developer engineer
    parameter:facebook is dataframe containing job categories 
    type: dataframe
 '''
 assert isinstance(facebook,pd.core.frame.DataFrame)
 
 z=facebook['Category'].value_counts()
 s=sum([z['Artificial Intelligence'],z['Software Engineering'],z['Data Center Design and Construction'],
   z['Data & Analytics'],z['Data Center Strategy and Development'],z['IT'],z['Network Engineering']])
 s=s+sum([z['Database, Storage, Systems Engineering'],z['Analytics'],z['Machine Learning'],z['Data Center Design and Construction']])
 s=s+facebook['Category'].str.contains('Data').sum()
 total=facebook.shape[0]
 s=s/total
 f1=z['AR/VR']/total

 f3=facebook['Category'].str.contains('Legal|Finance').sum()/total
 f4=facebook['Category'].str.contains('Marketing|People|Public|HR|Customer|Media|Communications').sum()/total
 f5=facebook['Category'].str.contains('Management|Account|Sales|Monetization|Business|Payments').sum()/total
 other=1-s-f1-f3-f4-f5   

 d=facebook 
 x1=d[d['Category'].str.contains('Software Engineering|Data|Machine Learning|Artificial Intelligence|Database|Network|IT|Analytics')] 
 cat={'Machine Learning Engineer':0,'Big Data Engineer':0,'Artificial Intelligence':0,'Network Engineer':0,'Database Engineer':0,'Other':0}
 n=x1.shape[0]
 cat['Machine Learning Engineer']=x1['Title'].str.contains('Machine Learning|Machine|Learning|Deep Learning').sum()/n
 cat['Big Data Engineer']=x1['Title'].str.contains('Big Data|Data').sum()/n
 cat['Network Engineer']=x1['Title'].str.contains('Network').sum()/n  
    
 cat['IT Engineer']=x1['Category'].str.contains('IT').sum()/n  
    #cat['Software Development Manager']=x['Title'].str.contains('Software Development Manager|Manager').sum()   
 cat['Artificial Intelligence']=x1['Category'].str.contains('Artificial').sum()/n
 cat['Database Engineer']=x1['Category'].str.contains('Database|Storage').sum()/n
 norm=sum(list(cat.values()))
 print(norm)
 cat['Other']==n-norm
 normalized_dic={nam[0]:nam[1]/500 for nam in cat.items()}
 res = sorted(normalized_dic.items(), key=lambda x: x[1], reverse=True)
 normalized_dic={nam[0]:nam[1] for nam in res}
  

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
 ratios = [s, f1, f3,f4,f5,other]
 labels = ['Software Engineer', 'Global Operations', 'Legal & Finance','Marketing and Communication','Sales &Account Manager','Other']
 explode=[0.1,0,0,0,0,0]
# rotate so that first wedge is split by the x-axis
 angle = -180*ratios[0]
 angle = -180*ratios[0]
 wedge_a,labels_a,auto=ax1.pie(ratios, autopct='%1.1f%%', startangle=angle,
        explode=explode,colors=['r','hotpink','m','cadetblue','olive','g'],labels=labels )
 plt.setp(labels_a,weight='bold',fontsize=11)
# bar chart parameters
#Percentages of different subcatogries
 #plt.setp(labels_a,weight='bold',fontsize=14)                                                                                                                                                                                                                                                 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn nnn nnn                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   )
 xpos = 0
 bottom = 0
 ratios = [.28, 0.20,.12, .05,0.04,0.3][::-1]
 width = .2
 colors = ['#ffcc99','slategrey','c','m','plum','y'][::-1]

 for j in range(len(ratios)):
    height = ratios[j]
    ax2.bar(xpos, height, width, bottom=bottom, color=colors[j])
    ypos = bottom + ax2.patches[j].get_height()/2
    bottom += height
    ax2.text(xpos,ypos, "%d%%" %
        (ax2.patches[j].get_height()*100), ha='center')

 plt.title('Types of Software Engineer',weight='bold')
 plt.legend(('Big Data' , 'Cloud Engineer','Machine Learning','Network Engineer','IT Engineer','Other'),fontsize=16,loc='upper right')
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