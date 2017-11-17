import netCDF4
ds = netCDF4.Dataset("example_data/ggas2014121200_00-18.nc")
for v in ds.variables:
    print v

sst = ds.variables["SSTK"]
print sst

for d in sst.dimensions:
    print d, len(ds.variables[d])

print sst.shape, sst.size

for attr in sst.ncattrs():
    print attr, "=", getattr(sst,attr)

arr = sst[1,0,10:20, 30:35]
print type(arr)

dims = sst.dimensions
print dims

vars = ds.variables
arr_time = vars['time'][1]
arr_level = vars['surface'][0]
arr_lats = vars['latitude'][10:30]
arr_lons = vars['longitude'][30:35]

for vals in (arr_time, arr_level, arr_lats, arr_lons):
    print vals

metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst, attr)

print metadata