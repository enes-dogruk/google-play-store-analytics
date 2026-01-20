import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
pd.set_option('display.max_columns', None)

# Konsol genişliğini yapay olarak 1000 karaktere çıkar (Satır kırılmasını engeller)
pd.set_option('display.width', 1000)

# Sütun içindeki verilerin kesilmesini de engelle (Opsiyonel ama öneririm)
pd.set_option('display.max_colwidth', None)
df
df.isnull().sum()
df.shape


sns.histplot(data=df ["age"])
plt.show()

df["Age_mean"] = df["age"].fillna(df["age"].mean())
df
df[["Age_mean", "age"]]

sns.boxplot(data = df, y = "age")
plt.show()

#median
df["Age_median"] = df["age"].fillna(df["age"].median())
df
df[["Age_mean","Age_median", "age"]]