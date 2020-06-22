import string
from Information_extraction import text_list_links

with open('pw.txt', mode='r',encoding='utf-8') as myfile:
  data = myfile.read()
  data=data.lower()
  data=data.encode("ascii","ignore")
  data=data.decode()

for i in string.punctuation:
    if i!= "," and i in data:
         data=data.replace(i,"")
    if "  " in data:
        data=data.replace("  ","")
    if "\n" in data:
        data=data.replace(" ","")
data=data.split(",")

with open('nw.txt', 'r',encoding="utf-8") as file1:
    file1 = file1.read()
    file1 = file1.encode("ascii", "ignore")
    file1 = file1.decode()
for i in string.punctuation:
    if i!= "," and i in file1:
         file1=file1.replace(i,"")
    if "    " in file1:
        file1=file1.replace("    ","")
file1=file1.split(",")


positiveword=[0]*len(text_list_links)
negativeword=[0]*len(text_list_links)
neutralword=[len(text_list_links[i]) for i in range(len(text_list_links))]

new_list=[]

for i in text_list_links:
    str1=" "

    for j in i:
        str1=str1+j+" "
    new_list.append(str1)

def KMPSearch(new_list,data):
    lentxt=len(new_list)
    lensub=len(data)
    array=[0]*lensub
    computeArray(data,lensub,array)
    sum=0
    i=0
    j=0
    while i<lentxt:
        if new_list[i]==data[j]:
            i+=1
            j+=1
        if j==lensub:
            sum=sum+1
            j=array[j-1]

        elif i<lentxt and new_list[i]!=data[j]:
            if j!=0:
                j=array[j-1]
            else:
                i+=1
    return sum
def computeArray(sub, lensub, array):
    array[0]=0
    i=1
    length=0
    while i<lensub:
        if sub[length]==sub[i]:
            length+=1
            array[i]=length
            i+=1
        else:
            if length!=0:
                length=array[length-1]
            else:
                array[i]=0
                i+=1


for i in range(len(new_list)):
    for j in data:
        positiveword[i]=positiveword[i]+KMPSearch(new_list[i],j)
    for j in file1:
        negativeword[i]=negativeword[i]+KMPSearch(new_list[i],j)

for i in range(len(new_list)):
    neutralword[i]=neutralword[i]-positiveword[i]-negativeword[i]


# for k in range(len(text_list_links)):
#         print("Article ",k+1)
#         print("Positive Words:",positiveword[k],end=" ")
#         print(", Negative Words:",negativeword[k],end=" ")
#         print(", Neutral Words:",neutralword[k])
#         if positiveword[k] > negativeword[k]:
#             print("This is a positive sentiment")
#         elif positiveword[k] < negativeword[k]:
#             print("This is a negative sentiment")
#         else:
#             print("This is a neutral sentiment")
print("\n m=len of text ,n= len of subtext")
print("Best Time Complexity of KMP: O(m+n)")
print("Worst Time Complexity of KMP: O(mn)")
print(("In this case, the time complexity would times m+n"))

#plot
neutral=[i for i in neutralword]
positive=[j for j in positiveword]
negative=[k for k in negativeword]
x=[]
for i in range(len(text_list_links)):
    x.append((i))

import plotly.graph_objs as go
import plotly.offline as ply
graph1 = go.Scatter(x=x,y=positive,name='positive')
graph2 = go.Scatter(x=x,y=positive,name='positive',mode='markers')
graph3 = go.Scatter(x=x,y=negative,name='negative')
graph4 = go.Scatter(x=x,y=negative,name='negative',mode='markers')
graph5 = go.Scatter(x=x,y=neutral,name='neutral')
graph6 = go.Scatter(x=x,y=neutral,name='neutral',mode='markers')

data = [graph1, graph2,graph3,graph4,graph5,graph6]
layout = go.Layout(title={'text': 'Semantic Analysis', 'x': 0.5},
                   xaxis=dict(title='Article'),
                   yaxis=dict(title='Word Count'))
fig = dict(data=data, layout=layout)
ply.plot(fig, filename='Semantic Analysis.html')