import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('WineQT.csv')
# Sütun sınırını kaldır
pd.set_option('display.max_columns', None)

# Konsol genişliğini yapay olarak 1000 karaktere çıkar (Satır kırılmasını engeller)
pd.set_option('display.width', 1000)

# Sütun içindeki verilerin kesilmesini de engelle (Opsiyonel ama öneririm)
pd.set_option('display.max_colwidth', None)
df
df.shape
df.info()
df.head()
df.tail()
df.describe().T
df.isnull().sum()
df.duplicated().sum()
df["quality"].unique()

df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True)
plt.show()

df.groupby("quality").mean()

df['quality'].value_counts().plot(kind = "bar")
plt.show()

sns.histplot(df["alcohol"])
plt.show()

sns.pairplot(df)
plt.show()

sns.boxplot(x="quality", y="alcohol", data = df)
plt.show()

sns.scatterplot(x="fixed acidity", y="density", hue="quality", data=df)
plt.show()

columns = df.columns
(fig, ax) = plt.subplots(4,4, figsize=(16,15))
ax = ax.flatten()

for i, column in enumerate(columns):
    sns.kdeplot(
        data=df,
        x=column,
        hue="quality",
        ax=ax[i],
        legend=False
    )
    ax[i].set_title(f"{column} Distribution")
    ax[i].set_xlabel(None)

# Boş kalan grafikleri kapat
for j in range(i+1, len(ax)):
    ax[j].axis("off")

# Tek bir legend
fig.legend(title="quality", loc="upper right")

plt.tight_layout()
plt.show()
