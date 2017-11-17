import matplotlib.pyplot as plt
plt.subplot(1, 3, 1)
x = range(0, 10, 1)
plt.plot(x)
plt.subplot(1, 3, 2)
y = range(10, 0, -1)
plt.plot(y)
plt.subplot(1, 3, 3)
z = [4] * 10
plt.plot(z)
plt.show()