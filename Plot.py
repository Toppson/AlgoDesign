import plotly.graph_objs as go
import plotly.offline as ply
from Information_extraction import dictt,newtext
words=newtext.split()
new=[a for a in words]
x=[]
y=[]

for i in dictt:
    x.append(i)

for j in dictt:
    y.append(dictt[j])

print('x =',x)
print('y =',y)
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
    x=new,
    name='histogram',
    nbinsx=50
)
data=[graph1,graph2,graph3]
layout=go.Layout(title={'text':'Graph Frequency vs Word Count','x':0.5},
                 xaxis=dict(title='Word '),
                 yaxis=dict(title='Frequency/count'))
fig=dict(data=data,layout=layout)
ply.plot(fig,filename='graph.html')

