
import webbrowser
import numpy as np
import googlemaps
from gmplot import gmplot
import os
from math import radians, cos, sin, asin, sqrt
from geopy.distance import great_circle
import Find_Shortest_Path as sp

path = 'options'
colors = ['red','blue','gray','purple','fuchsia','gold','pink','white']
files = os.listdir(path)
# center of map
gmap = gmplot.GoogleMapPlotter(4.144082, 101.081438, 8)
gmap.apikey='AIzaSyB-T4FGL-A6zZ_p6lbNgD4eHtjnV9b44a0'
gmap1= gmplot.GoogleMapPlotter(4.144082, 101.081438, 8)
gmap1.apikey='AIzaSyB-T4FGL-A6zZ_p6lbNgD4eHtjnV9b44a0'
gmap2= gmplot.GoogleMapPlotter(4.144082, 101.081438, 8) #central point
gmap2.apikey='AIzaSyB-T4FGL-A6zZ_p6lbNgD4eHtjnV9b44a0'

route=[]

strr = ""
count=0;
distance=[]
fullcoordinate_distance = []
fullcoordinate = []
for ls in files:
    data = open("options/" + ls, 'r').read().replace("\n", "")
    strr = ' '.join(data.split())
    strr = strr.replace(" ", "&")
    coor = strr.split("&")
    coordinatex = []
    coordinatey = []
    temp1=0;
    points_coor = []
    for (ind, i) in enumerate(coor, 0):
        temp = i.split(',')
        coordinatey.append(float(temp[0]))
        coordinatex.append(float(temp[1]))
        points_coor.append("{},{}".format(temp[1],temp[0]))

    fullcoordinate.append(points_coor)

    points_Distance = []
    for k in range (len(coordinatey)-1):
        newport_ri = (coordinatex[k], coordinatey[k])
        cleveland_oh = (coordinatex[k+1], coordinatey[k+1])
        d = great_circle(newport_ri, cleveland_oh).miles
        temp1+=d
        points_Distance.append("{}_{}_{}".format(newport_ri,cleveland_oh,d))

    fullcoordinate_distance.append(points_Distance)

    distance.append(temp1)
    gmap.plot(coordinatex, coordinatey, colors[count], edge_width=6)
    count+=1

to_check = [] # to remove duplicate so that we know how many nodes in the graph
for i in range(len(fullcoordinate)):
    for n in fullcoordinate[i]:
        if n not in to_check:
            to_check.append(n)

start = str("{}".format(fullcoordinate[0][0]))
end = str("{}".format(fullcoordinate[0][len(fullcoordinate[0])-1]))
print(start)
print(end)
# print(to_check, start, end)

graph = sp.Graph(to_check, start, end)
for i in range(len(fullcoordinate_distance)):
    for n in fullcoordinate_distance[i]:
        tempstr = n.split("_")
        From = tempstr[0][1:len(tempstr[0])-1].replace(" ", "")
        To = tempstr[1][1:len(tempstr[1])-1].replace(" ", "")
        distance_between = tempstr[2]
        graph.addDistance(From,To,distance_between)
#print(graph.distanceNode_Node())

graph.search()
best_coor, shortest_distance = graph.shortestPath()
best_coorx = []
best_coory = []
for i in best_coor:
    a = i.split(",")
    best_coorx.append(float(a[0]))
    best_coory.append(float(a[1]))
print("The shortest distance is ",shortest_distance)
# gmap2.plot(best_coorx, best_coory, "cornflowerblue", edge_width=6)

def minRoute(distance,shortest_distance,route):
    closest_choose = distance[0] - shortest_distance
    print(closest_choose)
    best = 0
    for i in range(1,len(distance)):
        compare = distance[i] - shortest_distance
        if compare > 0 and compare < closest_choose:
            closest_choose = compare
            best = i
    print("Shortest path =\n", route[best], "(", shortest_distance, "km )")
    data1 = open("options/" + files[best], 'r').read().replace("\n", "")
    strr1 = ' '.join(data1.split())
    strr1 = strr1.replace(" ", "&")
    coor1 = strr1.split("&")
    bestcoorx = []
    bestcoory = []
    for (ind, i) in enumerate(coor1, 0):
        temp = i.split(',')
        bestcoory.append(float(temp[0]))
        bestcoorx.append(float(temp[1]))
    gmap1.plot(bestcoorx, bestcoory, "cornflowerblue", edge_width=6)

for (ind,f) in enumerate (files,1):
    # print("Option ",ind," (",colors[ind-1],") = ",f.split('.')[0], "-",distance[ind-1] ,"km")
    print("Option ",ind," (",colors[ind-1],") = ",f.split('.')[0])
    route.append(f.split('.')[0])
minRoute(distance,shortest_distance,route)

# //find shortest distance and show graph

# Draw
gmap.draw("my_map.html")
url = "my_map.html"
webbrowser.open(url)

gmap1.draw("best.html")
url1 = "best.html"
webbrowser.open(url1)

# gmap2.draw("sp.html")
# url2 = "sp.html"
# webbrowser.open(url2)


#    distance.append(temp)

#print(distance)
