import numpy as np
import matplotlib.pyplot as plt
age_list = [10, 20, 30, 30,30,30,40,60,70,75]
weight_list = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]
plt.plot(age_list, weight_list, "r")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()

#numpy 
np_age_list = np.array(age_list)
print(np_age_list)
np_weight_list = np.array(weight_list)
plt.plot(np_age_list, np_weight_list, "g")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")
plt.show()
numpy_arr1 = np.linspace(0,10,20)
print(numpy_arr1)
numpy_arr2 = numpy_arr1 ** 3
print(numpy_arr2)
plt.plot(numpy_arr1, numpy_arr2, "b.-")
plt.show()

plt.subplot(1, 2, 1)
plt.plot(numpy_arr1, numpy_arr2, "r.-")
plt.subplot(1, 2, 2)
plt.plot(numpy_arr2, numpy_arr1, "b--")
plt.show()