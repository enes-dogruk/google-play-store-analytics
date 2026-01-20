import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('athlete_events.csv')
import pandas as pd

# Sütun sınırını kaldır
pd.set_option('display.max_columns', None)

# Konsol genişliğini yapay olarak 1000 karaktere çıkar (Satır kırılmasını engeller)
pd.set_option('display.width', 1000)

# Sütun içindeki verilerin kesilmesini de engelle (Opsiyonel ama öneririm)
pd.set_option('display.max_colwidth', None)

print(data.describe())
print(data.head())
data.isnull()
data.info()


plt.scatter("Height", "Weight", data = data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Athletes Weight vs Height")
plt.show()

sns.set_style("whitegrid")
sns.scatterplot(x = "Height", y = "Weight", data=data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes Weight vs Height")
plt.show()


sns.set_style("whitegrid")
sns.scatterplot(x = "Height", y = "Weight", hue = "Sex", data=data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes Weight vs Height")
plt.show()

data.columns

data["Medal"].unique()
data["Sex"].unique()

sns.set_style("whitegrid")
sns.lineplot(x = "Height", y = "Weight", hue = "Sex", data = data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes Weight vs Height")
plt.show()


sns.set_style("white")
sns.displot(x = "Height", hue = "Sex", data = data)
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.show()


sns.set_style("white")
sns.displot(x = "Height", hue = "Sex", data = data, kind = "kde")
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")


sns.barplot(x = "Medal", y = "Height", hue = "Sex", data = data)
plt.title("Medals by Height")
plt.show()

sns.catplot(x = "Medal", y = "Height", hue = "Sex", col = "Season", data = data)
plt.show()

