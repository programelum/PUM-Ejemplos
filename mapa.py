from mpl_toolkits.basemap import Basemap as Map
from matplotlib.pyplot import *
from numpy import *

figure()

#http://matplotlib.org/basemap/users/mapsetup.html
m=Map(projection='cyl',lat_0=0,lon_0=0)
m.drawparallels([-45,0,45])
m.drawmeridians([0,90,180,270])
m.drawcoastlines()

x,y=m(20,45)

plot(x,y,'ro')

savefig("mapa.png")
