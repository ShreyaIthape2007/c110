import pandas as pd
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random

from six import create_bound_method


file = pd.read_csv('data2.csv')

data = file['reading_time'].tolist()


def findmeans():
    dataset=[]

    for i in range(0,100):
        randomindex=random.randint(0,len(data)-1)
        value = data[randomindex]

        dataset.append(value)



    sample_mean = statistics.mean(dataset)

    return sample_mean



def create_graph(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    
    graph = ff.create_distplot([meanlist,],['Means of Means'],show_hist=False)
    #graph.add_traces(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='Mean'))
    graph.show()




def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=findmeans()

        meanlist.append(setofmeans)

    print('Mean of meanlist:',statistics.mean(meanlist))
    print('std of meanlist:',statistics.stdev(meanlist))

    create_graph(meanlist)

setup()