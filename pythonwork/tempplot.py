from datetime import datetime, timedelta
import time
from netCDF4 import Dataset, num2date
import numpy as np
import matplotlib.pyplot as plt

def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

infile='serial-temperature.tsv'
from csv import reader

times = []
temps = []

with open (infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))

base_time = times[0]
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)

time_units = "seconds since " + base_time.strftime('%Y-%m-%d %H:%M:%S')

output_file = "sensor_data.nc"
dataset = Dataset(output_file, "w", format='NETCDF4_CLASSIC')

time_dim = dataset.createDimension("time", None)

time_var = dataset.createVariable("time", np.float64, ("time",))
time_var[:] = time_values
time_var.units = time_units
time_var.standard_name = "time"
time_var.calendar = "standard"

temp = dataset.createVariable("temp", np.float32, ("time",))
temp[:] = temps

temp.var_id =  "temp"   
temp.long_name =  "Temperature   of sensor   (K)"  
temp.units  =  "K"   
temp.stabdard_name   =  "air_temperature" 

dataset.Conventions  =  "CF-1.6" 
dataset.institution  =  "NCAS"   
dataset.title  =  "My   first CF-netCDF   file" 
dataset.history   =  "%s:  Written  with  script:  write_sensor_data_to_netcdf.py"  %  (datetime.now().strftime("%x  %X"))

dataset.close()

# Tick "locators" c.f. http://matplotlib.org/api/dates_api.html
from matplotlib.dates import MinuteLocator, DateFormatter

datafile = 'sensor_data.nc'

nc = Dataset(datafile, mode='r')

temp = nc.variables['temp']
temps = temp[:]
time = nc.variables['time']

times = num2date(time[:],units=time.units, calendar=time.calendar)

#get "handles" to affect plot styling
fig, ax = plt.subplots()
#tick every tenth minute
ax.xaxis.set_major_locator(MinuteLocator(byminute=range(0,60,10)))

#format of date on x-axis (display minutes, uses strftime)
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))


#tick every minute
ax.xaxis.set_minor_locator(MinuteLocator())
ax.autoscale_view()

#line graph
plt.plot_date(times,temps,'-')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=10, horizontalalignment='center')
plt.xlabel(time.standard_name)
plt.title(nc.title)

#tidy up layout automatically
fig.tight_layout()

plt.savefig('sensor_data.png')



