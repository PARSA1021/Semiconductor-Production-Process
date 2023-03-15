# -*- coding: utf-8 -*-
"""Semiconductor Production Process

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ctmyHDTi5UinPJVHZ71tQdRr-24YSlfu
"""

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

"""# **Import Data**"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("/content/gdrive/MyDrive/ML,DL datasets/Semiconductor Dataset/fab.csv")

"""# **Data Information**"""

df.info()

df.dtypes

df

df.head()

df.tail()

df.describe()

"""# **Data Visualization**"""

df['Pass_Fail'].value_counts()

plt.figure(figsize=(10,10))
sns.countplot('Pass_Fail',data = df)

plt.figure(figsize=(10,10))
plt.title('Pass_Fail Ratio')
df['Pass_Fail'].value_counts().plot.pie(explode=(0,0.2),autopct='%1.f%%',shadow=True)

px.scatter(df,x='SensorTime',y='Sensor0',color='Pass_Fail',template='plotly_dark')

"""# **Data Missing Value Processing**"""

df = df.drop(['SensorTime'],axis = 1)

for idx,val in enumerate(df.isna().mean()*100):
  print(f"{idx} columns Missing Value Ratio = {val: .1f}%")

missing_value = df.columns[df.isna().mean()>0.7]

df = df.drop(missing_value,axis = 1)

for column in df.columns:
  df[column] = df[column].fillna(df[column].mean())

df.isna().sum()

df.isna().mean()

"""# **Remove Collinear Features**"""

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cmap = 'summer_r')

corr_matrix = df.corr().abs()

print(corr_matrix)

up_tr = corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k = 1).astype(np.bool_))

print(up_tr)

to_drop = [column for column in up_tr.columns if any(up_tr[column]>0.75)]

print(); print(to_drop)

column = ['Sensor17', 'Sensor26', 'Sensor27', 'Sensor30', 'Sensor35', 'Sensor36', 'Sensor39', 'Sensor46', 'Sensor50', 'Sensor54', 'Sensor60', 'Sensor65', 'Sensor66', 'Sensor70', 'Sensor73', 'Sensor96', 'Sensor98', 'Sensor101', 'Sensor104', 'Sensor105', 'Sensor106', 'Sensor123', 'Sensor124', 'Sensor127', 'Sensor130', 'Sensor140', 'Sensor147', 'Sensor148', 'Sensor152', 'Sensor154', 'Sensor155', 'Sensor163', 'Sensor164', 'Sensor165', 'Sensor174', 'Sensor187', 'Sensor196', 'Sensor197', 'Sensor199', 'Sensor202', 'Sensor203', 'Sensor204', 'Sensor205', 'Sensor206', 'Sensor207', 'Sensor209', 'Sensor244', 'Sensor245', 'Sensor246', 'Sensor249', 'Sensor252', 'Sensor254', 'Sensor270', 'Sensor271', 'Sensor272', 'Sensor273', 'Sensor274', 'Sensor275', 'Sensor277', 'Sensor278', 'Sensor279', 'Sensor280', 'Sensor281', 'Sensor282', 'Sensor283', 'Sensor285', 'Sensor286', 'Sensor287', 'Sensor288', 'Sensor289', 'Sensor290', 'Sensor291', 'Sensor294', 'Sensor295', 'Sensor296', 'Sensor297', 'Sensor298', 'Sensor299', 'Sensor300', 'Sensor301', 'Sensor302', 'Sensor303', 'Sensor304', 'Sensor305', 'Sensor306', 'Sensor307', 'Sensor308', 'Sensor309', 'Sensor310', 'Sensor311', 'Sensor312', 'Sensor316', 'Sensor317', 'Sensor318', 'Sensor319', 'Sensor320', 'Sensor321', 'Sensor323', 'Sensor324', 'Sensor331', 'Sensor332', 'Sensor333', 'Sensor334', 'Sensor335', 'Sensor336', 'Sensor337', 'Sensor338', 'Sensor339', 'Sensor340', 'Sensor341', 'Sensor342', 'Sensor343', 'Sensor344', 'Sensor345', 'Sensor346', 'Sensor347', 'Sensor348', 'Sensor349', 'Sensor350', 'Sensor351', 'Sensor352', 'Sensor353', 'Sensor354', 'Sensor355', 'Sensor356', 'Sensor357', 'Sensor359', 'Sensor360', 'Sensor361', 'Sensor362', 'Sensor363', 'Sensor365', 'Sensor366', 'Sensor368', 'Sensor376', 'Sensor377', 'Sensor382', 'Sensor383', 'Sensor384', 'Sensor385', 'Sensor386', 'Sensor387', 'Sensor388', 'Sensor389', 'Sensor390', 'Sensor391', 'Sensor392', 'Sensor393', 'Sensor405', 'Sensor406', 'Sensor407', 'Sensor408', 'Sensor409', 'Sensor410', 'Sensor411', 'Sensor412', 'Sensor413', 'Sensor415', 'Sensor416', 'Sensor417', 'Sensor420', 'Sensor421', 'Sensor424', 'Sensor425', 'Sensor426', 'Sensor427', 'Sensor428', 'Sensor429', 'Sensor430', 'Sensor431', 'Sensor434', 'Sensor435', 'Sensor436', 'Sensor437', 'Sensor439', 'Sensor440', 'Sensor441', 'Sensor442', 'Sensor443', 'Sensor444', 'Sensor445', 'Sensor446', 'Sensor447', 'Sensor448', 'Sensor452', 'Sensor453', 'Sensor454', 'Sensor455', 'Sensor456', 'Sensor457', 'Sensor459', 'Sensor467', 'Sensor469', 'Sensor470', 'Sensor471', 'Sensor473', 'Sensor474', 'Sensor475', 'Sensor477', 'Sensor478', 'Sensor479', 'Sensor480', 'Sensor490', 'Sensor491', 'Sensor493', 'Sensor494', 'Sensor495', 'Sensor496', 'Sensor497', 'Sensor516', 'Sensor517', 'Sensor518', 'Sensor519', 'Sensor520', 'Sensor522', 'Sensor523', 'Sensor524', 'Sensor525', 'Sensor526', 'Sensor527', 'Sensor539', 'Sensor540', 'Sensor541', 'Sensor545', 'Sensor552', 'Sensor553', 'Sensor554', 'Sensor555', 'Sensor556', 'Sensor557', 'Sensor560', 'Sensor561', 'Sensor566', 'Sensor567', 'Sensor568', 'Sensor569', 'Sensor573', 'Sensor574', 'Sensor575', 'Sensor576', 'Sensor577', 'Sensor580', 'Sensor584', 'Sensor585', 'Sensor588']

df = df.drop(column,axis = 1)

df.info()

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cmap = 'summer_r')

"""# **Data Split**"""

df.shape

x = df.iloc[:,:337]
y = df['Pass_Fail']

print("shape of x:", x.shape)
print("shape of y:", y.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

print("shape of x_train: ", x_train.shape)
print("shape of x_test: ", x_test.shape)
print("shape of y_train: ", y_train.shape)
print("shape of y_test: ", y_test.shape)

"""# **Data Standardization**"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train = sc.fit_transform (x_train)
x_test = sc.transform (x_test)

"""# **RandomForestClassifier**"""

from sklearn.metrics import confusion_matrix,accuracy_score

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 200, random_state= 1, verbose = 1)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

cm = confusion_matrix(y_test,y_pred)
plt.figure(figsize=(5,5))
sns.heatmap(cm,annot = True, annot_kws = {"size":15})

print('Accuracy: ',model.score(x_test,y_test)*100)

"""# **LogisticRegression**"""

from sklearn.linear_model import LogisticRegression

LR = LogisticRegression(random_state = 1)
LR.fit(x_train, y_train)
y_pred = LR.predict(x_test)

cm = confusion_matrix(y_test,y_pred)
plt.figure(figsize=(5,5))
sns.heatmap(cm,annot = True, annot_kws = {"size":15})

print('Accuracy: ',LR.score(x_test,y_test)*100)

"""# **GradientBoostingClassifier**"""

from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cm = confusion_matrix(y_test,y_pred)
plt.figure(figsize=(5,5))
sns.heatmap(cm,annot = True, annot_kws = {"size":15})

print("Accuracy:", accuracy_score(y_test, y_pred)*100)

"""# **SMOTE**"""

from imblearn.over_sampling import SMOTE

x_resample, y_resample  = SMOTE(random_state=1).fit_resample(x, y.values.ravel())

print(x_resample.shape)
print(y_resample.shape)

x_train_over, x_test_over, y_train_over, y_test_over = train_test_split(x,y,test_size = 0.3,random_state =1)

print(x_train_over.shape)
print(y_train_over.shape)
print(x_test_over.shape)
print(y_test_over.shape)

sc = StandardScaler()
x_train_over = sc.fit_transform(x_train_over)
x_test_over = sc.transform(x_test_over)

"""# **SMOTE RandomForestClassifier**"""

model = RandomForestClassifier(n_estimators=200, random_state=1,verbose=0 )
model.fit(x_train_over, y_train_over)

y_pred = model.predict(x_test_over)
print("Accuracy: ", model.score(x_test_over,y_test_over)*100)

"""# **SMOTE LogisticRegression**"""

LR = LogisticRegression(random_state = 1)
LR.fit(x_train_over, y_train_over)
y_pred = LR.predict(x_test_over)

print('Accuracy: ',LR.score(x_test_over,y_test_over)*100)