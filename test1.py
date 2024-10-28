import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
sns.set(color_codes = True)
%matplotlib inline
foresthealthdata = pd.read_csv('forest_health_data.csv')
foresthealthdata.count()
