import matplotlib.pyplot as plt

times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.plot(times, co2, 'b--', times, temp, 'r*-')
plt.show()
plt.savefig("co2_temp.pdf")