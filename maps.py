from example_code.map_data import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.figure()
plt.title('Change in Surface Air Temperature from MOHC HadGEM2-ES')
m = Basemap(projection = 'cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

im1 = m.pcolormesh(lons,lats,tas,shading='flat', cmap=plt.cm.jet, latlon=True)
cb = m.colorbar(im1, "bottom", size="5%", pad="2%")

plt.savefig("tas1.png")
plt.show()