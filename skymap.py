from map import *

figure()

m=drawMap(proj='cyl',proj_opts=dict(lon_0=180))

stars,props=readStars()

magnitudes=props[:,3]

x,y=m(props[magnitudes<19,0]*15,props[magnitudes<19,1])

plot(x,y,'ko',markersize=0.2)

savefig("skymap.png")
