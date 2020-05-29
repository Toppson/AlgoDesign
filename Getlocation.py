
import webbrowser
import numpy as np
import googlemaps
from gmplot import gmplot
import os
from math import radians, cos, sin, asin, sqrt
from geopy.distance import great_circle

path = 'options'
colors = ['red','blue','gray','purple','fuchsia','gold','pink','white']
files = os.listdir(path)
# center of map
gmap = gmplot.GoogleMapPlotter(4.144082, 101.081438, 8)
gmap.apikey='AIzaSyB-T4FGL-A6zZ_p6lbNgD4eHtjnV9b44a0'
gmap1= gmplot.GoogleMapPlotter(4.144082, 101.081438, 8)
gmap1.apikey='AIzaSyB-T4FGL-A6zZ_p6lbNgD4eHtjnV9b44a0'


route=[]


strr = ""
count=0;
distance=[]
for ls in files:

    data = open("options/" + ls, 'r').read().replace("\n", "")
    strr = ' '.join(data.split())
    strr = strr.replace(" ", "&")
    fullcoordinatex = [[]*7]
    fullcoordinatey = [[]*7]
    coor = strr.split("&")
    coordinatex = []
    coordinatey = []
    temp1=0;
    for (ind, i) in enumerate(coor, 0):
        temp = i.split(',')
        coordinatey.append(float(temp[0]))
        coordinatex.append(float(temp[1]))
    for k in range (len(coordinatey)-1):
        newport_ri = (coordinatex[k], coordinatey[k])
        cleveland_oh = (coordinatex[k+1], coordinatey[k+1])
        temp1+=(great_circle(newport_ri, cleveland_oh).miles)

    distance.append(temp1)
    gmap.plot(coordinatex, coordinatey, colors[count], edge_width=6)
    count+=1



def minRoute(distance,route):
    choose=distance[0]
    best=0;
    for i in range(len(distance)):
        if distance[i]<choose:
            choose=distance[i]
            road=route[i]
            best=i;
    print("Shortest path=",road,"(",choose,"km )")
    data1 = open("options/" + files[best], 'r').read().replace("\n", "")
    strr1 = ' '.join(data1.split())
    strr1 = strr1.replace(" ", "&")
    coor1 = strr1.split("&")
    bestcoorx=[]
    bestcoory=[]
    for (ind, i) in enumerate(coor1, 0):
        temp = i.split(',')
        bestcoory.append(float(temp[0]))
        bestcoorx.append(float(temp[1]))
    gmap1.plot(bestcoorx, bestcoory, "cornflowerblue", edge_width=6)

for (ind,f) in enumerate (files,1):
    print("Option ",ind," (",colors[ind-1],") = ",f.split('.')[0], "-",distance[ind-1] ,"km")
    route.append(f.split('.')[0])
minRoute(distance,route)

# //find shortest distance and show graph

# Draw
gmap.draw("my_map.html")
url = "my_map.html"
webbrowser.open(url)

gmap1.draw("best.html")
url1 = "best.html"
webbrowser.open(url1)


#    distance.append(temp)

#print(distance)
