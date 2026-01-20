import pandas as pd
import numpy as np

np.random.seed(42)

set1no = 900
set2no = 100

df1 = pd.DataFrame({
    "feature_1" : np.random.normal(loc=0, scale=1, size=set1no),
    "feature_2" : np.random.normal(loc=0, scale=1, size=set1no),
    "target" : [0] * set1no
})

df2 = pd.DataFrame({
    "feature_1" : np.random.normal(loc=0, scale=1, size=set2no),
    "feature_2" : np.random.normal(loc=0, scale=1, size=set2no),
    "target" : [1] * set2no
})

df1.head()
df2.head()

df = pd.concat([df1, df2]).reset_index(drop=True)
df

df["target"].unique()
df["target"].value_counts()

#upsampling --> upsample minority ---> Azınlığı arttırmak
#downsampling --> downsampling majority ---> Çoğunluğu azaltmak

#upsampling
df_minority = df[df["target"] == 1]
df_minority

df_majority = df[df["target"] == 0]
df_majority

from sklearn.utils import resample
df_minority_upsampled=resample(df_minority, replace=True, n_samples=len(df_majority), random_state=42)
df_minority_upsampled.head()

df_upsampled = pd.concat([df_majority, df_minority_upsampled])
df_upsampled["target"].value_counts()


df_majority_upsampled=resample(df_majority, replace=True, n_samples=len(df_minority), random_state=42)
df_majority_upsampled["target"].value_counts()

#SMOTE ----> Benzer datalar oluşturarak veriyi çoğaltma.
df
import matplotlib.pyplot as plt
plt.scatter(df["feature_1"], df["feature_2"], c=df["target"])
plt.show()

from imblearn.over_sampling import SMOTE
oversample = SMOTE()
(X, y) = oversample.fit_resample(df[["feature_1", "feature_2"]], df["target"])

X
y
type(X)

oversample_df = pd.concat([X,y],axis=1)
oversample_df

plt.scatter(oversample_df["feature_1"], oversample_df["feature_2"], c=oversample_df["target"])
plt.show()


