import csv
import math
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

lat = []
lng = []
hgt = []

fr = open('WG20150812003959.log','r')
reader = csv.reader(fr)
for row in reader:
	if(row[0] == "$GPGGA" and 30000 < int(row[1]) and int(row[1]) < 50000):
		print row[1]
		print row[2], row[4]
		lat_adp, lat_int = math.modf(float(row[2])/100)
		lng_adp, lng_int = math.modf(float(row[4])/100)
		lat.append(lat_int + lat_adp/60*100)
		lng.append(lng_int + lng_adp/60*100)
		hgt.append(float(row[9]))

#print lat,lng,hgt

fig = plt.figure()
#ax = fig.add_subplot(111)
ax = fig.gca(projection = '3d')
sc = ax.scatter(lng,lat,hgt)
ax.plot(lng,lat,hgt,'.r-')
plt.xlabel = "lng"
plt.ylabel = "lat"
plt.show()
