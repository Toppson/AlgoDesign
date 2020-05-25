import codecs
import urllib
import webbrowser
from random import random

import googlemaps
import xml.etree.ElementTree as et


import urllib3 as urllib3
from Tools.scripts import google
from bs4 import BeautifulSoup
from gmplot import gmplot

import plotly.offline as ply
import os

path = 'options'
colors = ['red','blue','green','purple','orange','yellow','pink','white']
files = os.listdir(path)
gmap = gmplot.GoogleMapPlotter(4.144082, 101.081438, 8)

for (ind,f) in enumerate (files,1):
	print("Option ",ind," = ",f.split('.')[0])

strr = ""
count=0;
for ls in files:

    data = open("options/" + ls, 'r').read().replace("\n", "")
    strr = ' '.join(data.split())
    strr = strr.replace(" ", "&")

    coor = strr.split("&")
    coordinatex = []
    coordinatey = []
    for (ind, i) in enumerate(coor, 0):
        temp = i.split(',')
        coordinatey.append((float)(temp[0]))
        coordinatex.append((float)(temp[1]))

    gmap.plot(coordinatex, coordinatey, colors[count], edge_width=5)
    count+=1

# UM TO USM
# option 1 = taxi to klia, flight to penang airport,
# center of map



# input array of coordinates from kml files


# Scatter points
# top_attraction_lats, top_attraction_lons = zip(*[
#     (37.769901, -122.498331),
#     (37.768645, -122.475328),
#     (37.771478, -122.468677),
#     (37.769867, -122.466102),
#     (37.767187, -122.467496),
#     (37.770104, -122.470436)
#     ])
# gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# Marker
# hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
# gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")
url = "my_map.html"
webbrowser.open(url)
