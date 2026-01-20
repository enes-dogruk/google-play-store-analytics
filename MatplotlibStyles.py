import numpy as np
import matplotlib.pyplot as plt


data1 = np.linspace(0, 10, 20)
print(data1)

data2 = data1 ** 2
print(data2)
plt.subplots()

my_fig, my_axes = plt.subplots()
type(my_fig)
type(my_axes)

(my_fig, my_axes) = plt.subplots()
my_axes.plot(data1, data2, color = "#145E8F")
my_axes.plot(data2, data1, color = "#DB7BD4")
plt.show()



(my_fig, my_axes) = plt.subplots()
my_axes.plot(data1, data1 + 2, color = "#FF0000", linewidth = 1.0)
my_axes.plot(data1, data1 + 3, color = "#006C8A", linewidth = 4.0, linestyle = "--")
plt.show()



#scatter
plt.scatter(data1, data2)
plt.show()


#histogram
plt.hist(data1, data2)
plt.show()