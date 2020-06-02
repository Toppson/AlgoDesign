import plotly.graph_objs as go
import plotly.offline as ply
from Information_extraction import dictt_links
#words=newtext_list.split()

x = []
y=[0]*21
for i in range(len(dictt_links)):  #21 article
    x.append(i+1)
    for j in dictt_links[i].keys():
        num=int(dictt_links[i][j])
        y[i]=y[i]+num

    print('x =', x)
    print('y =', y)

graph1 = go.Scatter(
        x=x,
        y=y,
        name='line'
    )
graph2 = go.Scatter(
        x=x,
        y=y,
        name='scatters',
        mode='markers'
    )
    # graph3 = go.Histogram(
    #     x=new,
    #     name='histogram',
    #     nbinsx=50
    # )
    #graph 3
data = [graph1, graph2]
layout = go.Layout(title={'text': 'Graph Frequency vs Word Count', 'x': 0.5},
                   xaxis=dict(title='Word '),
                   yaxis=dict(title='Frequency/count'))
fig = dict(data=data, layout=layout)
name = 'graph ' + str(i) + '.html'
ply.plot(fig, filename=name)
