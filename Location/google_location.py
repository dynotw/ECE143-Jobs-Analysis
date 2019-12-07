import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# use the 'ggplot'， one of matplotlib art styles
plt.style.use("ggplot")

# load the data from csv
df = pd.read_csv('google.csv')

df = df.dropna(axis=0, how='any')
# clear the rows with NaN. axis=0 means delete the NaN, depending on the rows, axis=1 means columns
# 'any' means rows with NaN, 'all' means rows whose elements all are NaN

# get all the data from ['Location']
all_location=df['Location'].value_counts()
# print(all_location)

# only get the location data which contains 'United States'
US=df[df['Location'].str.contains("United\sStates")]
# Notice the difference between str.contains and isin
# If want to delete the rows including specific words, df[~df['Location'].str.contains("United\sStates")]
US_Management=US[US['Category'].str.contains('Management')]

# Pick up Top10 US cities
US_city=(US['Location'].apply(lambda x : x.split(',')[0])).value_counts()[:10]
US_Management_city=(US_Management['Location'].apply(lambda x : x.split(',')[0])).value_counts()[:10]
# Pick up the State in US
US_state=(US['Location'].apply(lambda x: x.split(',')[1][1:])).value_counts()
print(US_state)
print(US_city)

# only keep the 'country' for location
df['country']=df['Location'].apply(lambda x: x.split(',')[-1])
f_M=df[df['Category'].str.contains('Management')]
# Pick up Top10 foreign countries
fc=df['country'].value_counts()[1:11]
fc_M=f_M['country'].value_counts()[1:11]
# print(fc)

# Draw Horizontal Histogram Graph
def histogram_h(data_name,tittle,xlabel='Popularity',ylabel='Country'):
    '''

    :param data_name: input, the pd.Series
    :param tittle:
    :param xlabel:
    :param ylabel:
    :return:
    '''
    assert isinstance(tittle,str)
    assert isinstance(xlabel,str)
    assert isinstance(ylabel,str)
    # plot.bar is vertical histogram; plot.barh is horizontal histogram
    data_name = data_name[::-1]
    data_name.plot.barh(figsize=(20, 20), color='#32CD32')

    # add a title, and set the size of plot
    plt.title(tittle, fontsize=24, weight='bold')
    plt.xlabel(xlabel, fontsize=17, weight='bold')
    plt.ylabel(ylabel, fontsize=17, weight='bold')
    # set the fontsize for mark of a,y axis
    plt.tick_params(labelsize=15)
    plt.xticks(weight='bold')
    plt.yticks(weight='bold')
    # finally show the plot
    plt.show()



state_data = US_state.to_frame()
state_data = pd.DataFrame(state_data.reset_index())
state_data.columns = ["state", "freq"]

def map(data_name):
    '''

    :param data_name: input, pd.DataFrame
    :return: map
    '''

    assert isinstance(data_name, pd.DataFrame)

    fig = go.Figure(data=go.Choropleth(
        locations=state_data['state'],  # Spatial coordinates
        z=state_data['freq'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Greens',
        colorbar_title="# of jobs",
    ))

    fig.update_layout(
        title_text='Google Jobs',
        font=dict(size=20),
        geo_scope='usa',  # limite map scope to USA,
        showlegend=True,
    )

    fig.update_layout(
        title={
            'text': 'Google Jobs Map',
            'x': 0.5,
            'y': 0.9,
            # 'xanchor': 'auto',
            # 'yanchor': 'auto'
        }
    )
    fig.show()

if __name__ == '__main__':
    histogram_h(US_city,tittle='Google Top 10 popular US Cities', ylabel='City')
    histogram_h(fc,tittle='Google Top 10 Popular Overseas Workplace')
    map(state_data)







