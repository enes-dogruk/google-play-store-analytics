import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

df = sns.load_dataset("titanic")
df

df[["sex", "class", "embark_town"]].isna().sum()
df = df.dropna(subset=['embark_town'])
df

#one hot encoding
df["sex"].value_counts()

df["embark_town"].value_counts()

df["class"].value_counts()

df_onehot = pd.get_dummies(df, columns=["sex", "embark_town"], drop_first = True)
df_onehot

#label encoder
label_encoder = LabelEncoder()
df_label = df.copy()
df_label

df_label["sex"] = label_encoder.fit_transform(df_label["sex"])
df_label

#ordinal encoder
df_ordinal = df.copy()
class_order = ["Third", "Second", "First"]
ordinal_encoder = OrdinalEncoder(categories=[class_order])
df_ordinal["class"] = ordinal_encoder.fit_transform(df_ordinal[["class"]])
df_ordinal

fig, axes = plt.subplots(1,3,figsize=(15,5))
df["sex"].value_counts().plot(kind="bar", ax=axes[0], title="Original Categorical")
df_label["sex"].value_counts().plot(kind="bar", ax=axes[1], title="Label Encoded")
df_onehot["sex_male"].value_counts().plot(kind="bar", ax=axes[2], title="Original Categorical")
plt.show()





