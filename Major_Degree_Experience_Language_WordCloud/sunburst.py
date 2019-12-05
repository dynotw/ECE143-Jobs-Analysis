from plotly.offline import iplot, init_notebook_mode,plot
import plotly.graph_objs as go
import plotly.io as pio
import plotly.offline
import os
import matplotlib.pyplot as plt
import numpy as np

'''
This is summary plot that generates sunburst plot based on preferred qualifications of top three subcategories
of software engineer of each Amazon, Google, Facebook
Output: Sunburst plot
Colors:
    Amazon: Drakorange
    Google: Lime Green
    Fcaebook:MediumBlue
'''

trace = go.Sunburst(
    labels=[ "Facebook", "Google", "Amazon", "Big Data Engineer","Python","CS or EE","Bachelors", "AI Engineer"," Python","CS or CE","Bachelor","ML Engineer" ,"Hadoop","Stats or CE"," Bachelors"," Big Data Engineer","  Python","Stats or Maths","    Bachelors","Cloud Engineer","Java","Computer Science","Masters or Bachelors"," ML Engineer","   Python","  Computer Science","Masters","  ML Engineer"," Java","CS or CE or EE"," Masters","Web Developer","Java or javascript","   Computer Science"," Masters or PhD","  Big Data Engineer","Spark and Python"," CS or CE"," Bachelors or Masters"],
    parents=[" ", " "  ," ", "Facebook", "Big Data Engineer", "Big Data Engineer",  "Big Data Engineer",  "Facebook",  "AI Engineer","AI Engineer","AI Engineer","Facebook","ML Engineer", "ML Engineer","ML Engineer","Google"," Big Data Engineer"," Big Data Engineer"," Big Data Engineer","Google","Cloud Engineer","Cloud Engineer","Cloud Engineer","Google"," ML Engineer"," ML Engineer"," ML Engineer","Amazon","  ML Engineer","  ML Engineer","  ML Engineer","Amazon","Web Developer","Web Developer","Web Developer","Amazon","  Big Data Engineer","  Big Data Engineer","  Big Data Engineer"],
    
    marker = {"line": {"width": 2}},
)

layout = go.Layout(
    margin = go.layout.Margin(t=0, l=0, r=0, b=0),colorway=['mediumblue','limegreen','darkorange'],font=dict(family='times new roman', size=18,color='#7f7f7f'),
)

fig=go.Figure([trace], layout)

iplot(fig)
#iplot(go.Figure([trace], layout), filename='basic_sunburst_chart.html')
