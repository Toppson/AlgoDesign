import plotly.graph_objs as go
import plotly.offline as ply
x=[1,2,3,4,5]
y=[1,2,3,4,5]

graph1=go.Scatter(
    x=x,
    y=y,
    name='line'
)
graph2=go.Scatter(
    x=x,
    y=y,
    name='scatters',
    mode='markers'
)
graph3=go.Histogram(
    x=x,
    name='histogram',
    nbinsx=max(x)
)
data=[graph1,graph2,graph3]
layout=go.Layout(title={'text':'Graph Frequency vs Word Count','x':0.5},
                 xaxis=dict(title='Word Count'),
                 yaxis=dict(title='Frequency'))
fig=dict(data=data,layout=layout)
ply.plot(fig,filename='graph.html')

