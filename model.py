## Importing the libraries and dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('breastCancer\data.csv')

## Data exploration
head = dataset.head()
# print(head)

shape = dataset.shape
# print(shape)

# dataset.info()


dataset = dataset.drop(columns='Unnamed: 32')

# Statistical summary
describe = dataset.describe()
# print(describe)


columns = dataset.columns
# print(columns)

## Dealing with the missing data

# check if there are any null values
(dataset.isnull().values.any())

(dataset.isnull().values.sum())


## Encoding the categorical data

print(dataset.select_dtypes(include='object').columns)


(dataset['diagnosis'].unique())

(dataset['diagnosis'].nunique())


dataset = pd.get_dummies(data=dataset, drop_first=True)
print(dataset.shape)

sns.countplot(dataset['diagnosis_M'], label='Count')
plt.show()

print((dataset.diagnosis_M == 0).sum())
print((dataset.diagnosis_M == 1).sum())