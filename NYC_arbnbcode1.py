## all imports will be used for examples below
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error
#%matplotlib inline
## Use pandas to read the csv download and view the data
df = pd.read_csv('./AB_NYC_2019.csv')
df.head()