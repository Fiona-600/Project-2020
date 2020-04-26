
import pandas as pd

#Read all characters in the file 'irisdataset.csv'

#dataset = pd.read_csv("irisdataset.csv") 
#https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

dataset = pd.read_csv("irisdataset.csv" , header = None)
#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python

#define the column names
dataset_column_names = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#To create column headers
#header_list = ["Sepal Length", "Sepal Width", "Petal Length" , 'Petal Width' ,'Species' ]
#df = pd.read_csv("irisdataset.csv", names=header_list)
#https://kite.com/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python

#print first 5 lines
print (dataset.head())

print (dataset)
#print (df)

import numpy as np

import seaborn as sns
# Set default Seaborn style
sns.set

import matplotlib.pyplot as plt
#plt.hist(dataset, bins='auto', density=True, histtype='step'
plt.hist(dataset, density=True, bins='auto')
plt.show()
#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python



#import holoviews as hv
import scipy as sp

#from csv import reader

#def load_iris.csv 
   #file = open iris.csv
   #lines = reader (irisdataset)
   #dataset = list(lines)
   #return dataset