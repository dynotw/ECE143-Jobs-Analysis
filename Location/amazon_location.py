import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# use the 'ggplot'， an art style of matplotlib
plt.style.use("ggplot")

# load the data from csv
df = pd.read_csv('amazon_jobs_dataset.csv')

df = df.dropna(axis=0, how='any')
# clear the rows with NaN. axis=0 means delete the NaN, depending on the rows, axis=1 means columns
# 'any' means rows with NaN, 'all' means rows whose elements all are NaN

# get all the data from ['Location']
all_location=df['location'].value_counts()

# only get the location data which contains 'United States'
US=df[df['location'].str.contains("US")]
US_SDE=US[US['Title'].str.contains("Software")]
# Notice the difference between str.contains and isin
# Pick up Top10 US cities
US_city=(US['location'].apply(lambda x : x.split(',')[-1])).value_counts()[:10]
US_SDE_city=(US_SDE['location'].apply(lambda x : x.split(',')[-1])).value_counts()[:10]
print(US_city)

# Only keep the 'country' for location
df['country']=df['location'].apply(lambda x: x.split(',')[0])
# Use full name to replace the abbreviation
df['country']=df['country'].replace(['CA','IN','UK','IE','DE','IL','CN',"PL",'RO','ZA','ES'],['Canada','India','United Kingdom','Ireland','Germany','Israel','China','Poland','Romania','South Africa','Spain'])
f_SDE=df[df['Title'].str.contains("Software")]
# Pick up Top10 foreign countries
fc=df['country'].value_counts()[1:11]
fc_SDE=f_SDE['country'].value_counts()[1:11]
print(fc)

def histogram_h(data_name,tittle,xlabel='Popularity',ylabel='Country'):
    '''

    :param data_name: pd.Series, data which need to show the graphs
    :param tittle: str, name plot tittle
    :param xlabel: str, name of xlabel
    :param ylabel: srt, name of ylabel
    :return:
    '''

    assert isinstance(tittle,str)
    assert isinstance(xlabel,str)
    assert isinstance(ylabel,str)
    # plot.bar is vertical histogram; plot.barh is horizontal histogram
    # [::-1], make the order is from big ro small
    data_name = data_name[::-1]
    data_name.plot.barh(figsize=(20, 20),color='#fc910d')
    # add a title, and set the size of plot
    plt.title(tittle, fontsize=24, weight='bold')
    plt.xlabel(xlabel, fontsize=17,weight='bold')
    plt.ylabel(ylabel, fontsize=17,weight='bold')
    # set the fontsize for mark of a,y axis
    plt.tick_params(labelsize=15)
    plt.xticks(weight='bold')
    plt.yticks(weight='bold')
    # finally show the plot
    plt.show()

# Pick up the State in US
US_state=(US['location'].apply(lambda x: x.split(',')[1][1:])).value_counts()
print(US_state)
state_data = US_state.to_frame()
state_data = pd.DataFrame(state_data.reset_index())
state_data.columns = ["state", "freq"]

def map(data_name):
    '''

    :param data_name: input, pd.DataFrame
    :return: map
    '''

    fig = go.Figure(data=go.Choropleth(
        locations=state_data['state'],  # Spatial coordinates
        z=state_data['freq'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="# of jobs",
        zmax=50,
        zmid=10,
        zmin=0,))

    fig.update_layout(
        title_text='Amazon Jobs Map',
        geo_scope='usa',  # limite map scope to USA,
        font=dict(size=20)
    )


    fig.update_layout(
        title={
            'x': 0.5,
            'y': 0.9,
            # 'xanchor': 'auto',
            # 'yanchor': 'auto'
        }
    )

    fig.show()

if __name__ == '__main__':
    histogram_h(US_city,tittle='Amazon Top 10 popular US Cities', ylabel='City')
    # histogram_h(US_SDE_city, tittle='Amazon Top 10 popular US Cities for Software', ylabel='City')
    histogram_h(fc,tittle='Amazon Top 10 Popular Overseas Workplace')
    # histogram_h(fc_SDE, tittle='Amazon Top 10 Popular Overseas Workplace for Software')
    map(state_data)