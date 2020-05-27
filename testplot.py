from gmplot import gmplot

gmap3 = gmplot.GoogleMapPlotter(30.3164945,
                                78.03219179999999, 13)


latitude_list = [30.3358376, 30.307977, 30.3216419]
longitude_list = [77.8701919, 78.048457, 78.0413095]


# Plot method Draw a line in
# between given coordinates
gmap3.plot(latitude_list, longitude_list,
           'cornflowerblue', edge_width=2.5)