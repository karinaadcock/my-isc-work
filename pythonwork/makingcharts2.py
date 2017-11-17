import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
ax1.plot(times, co2, "b--")
ax1.set_ylabel("[CO2]")
ax2 = ax1.twinx()
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
ax2.plot(times,temp, "r*-")
ax2.set_ylabel("Temp (degC)")
plt.legend()
plt.show()
plt.savefig("co2")