import plotly.graph_objs as go
import plotly.offline as ply
from Information_extraction import dictt_links,total_stopwords
#words=newtext_list.split()

x = []
y=[0]*21
y1=total_stopwords

for i in range(len(dictt_links)):  #21 article
    x.append(i+1)
    for j in dictt_links[i].keys():
        num=int(dictt_links[i][j])
        y[i]=y[i]+num

graph1 = go.Scatter(x=x,y=y,name='line for word count')
graph2 = go.Scatter(x=x,y=y,name='dot for word count',mode='markers')
graph3 = go.Scatter(x=x,y=y1,name='line for stopword')
graph4 = go.Scatter(x=x,y=y1,name='dot for stopword',mode='markers')
data = [graph1, graph2,graph3,graph4]
layout = go.Layout(title={'text': 'Graph Word Count/ stopword vs Article', 'x': 0.5},
                   xaxis=dict(title='Article'),
                   yaxis=dict(title='Word Count / Stop word'))
fig = dict(data=data, layout=layout)
name = 'Word Count ' + str(i) + '.html'
ply.plot(fig, filename=name)
