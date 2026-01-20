import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = np.array([5, 7, 9, 15, 20, 22, 25, 30, 32, 35, 37, 40, 50, 55, 60, 100])
plt.figure(figsize=(6,5))
sns.boxplot(y = data)
plt.title("Box Plot")
plt.ylabel("Data Value")
plt.show()

df = sns.load_dataset("titanic")
df

plt.figure(figsize = (13, 6))

plt.subplot(1, 2, 1)
sns.boxplot(x="class", y="age", data = df)
plt.title("Age by Class")
plt.xlabel("Class")
plt.ylabel("Age")

plt.subplot(1, 2, 2)
sns.boxplot(x="class", y="fare", data = df)
plt.title("Fare by Class")
plt.xlabel("Class")
plt.ylabel("Fare")

plt.tight_layout()
plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize = (13, 6))
age_list = [1, 2, 3, 3, 3, 3, 4, 6, 7, 8, 9, 10, 200]

df = pd.DataFrame({"age": age_list})

sns.boxplot(y="age", data=df)
plt.show()
