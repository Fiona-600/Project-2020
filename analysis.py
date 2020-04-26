
import pandas as pd

dataset = pd.read_csv("irisdataset.csv") 
#Read all characters in the file 'irisdataset.csv'
#dataset = pd.read_csv("irisdataset.csv" , header = None)
#https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

#define the column names
header_list = ["Sepal Length", "Sepal Width", "Petal Length" , 'Petal Width' ,'Class' ]

#divide the data set into three parts
iris_setosa = dataset.loc [dataset ["class"]=="Iris-setosa"]
iris_virginica = dataset.loc [dataset ["class"]=="Iris-virginica"]
iris_versicolor = dataset.loc [dataset ["class"]=="Iris-versicolor"]
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python

#Define a Data Frame
#df = pd.read_csv("irisdataset.csv", names=header_list)
#https://kite.com/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python

#print first 5 lines
#print (dataset.head())
import numpy as np
# Create a Data Frame
Data_Frame = pd.DataFrame(dataset,columns=header_list)
#print (Data_Frame.describe(include=[np.number]))
#print (dataset.info)

Data_Frame.hist(column ='Class')

#print(Data_Frame.columns)
#https://medium.com/@gangulym23/practical-pandas-50586fe90cf8

#Working Outputs
#print("columns",dataset.columns)
#print("shape:",dataset.shape)
#print (dataset)

#Print (Data_Frame) produces NaN returns
print (Data_Frame)

#Data_Frame[‘target’] = dataset[‘class’]
#print(“Checking top records: “)
#print(Data_Frame.head())
#print(‘\n’)


import matplotlib.pyplot as plt
#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
import seaborn as sns
# Set default Seaborn style
sns.set

#Label versicolor_petal_length
#versicolor_petal_length = ****This is specifying the input for the histogram, not reading from csv file***
#versicolor_petal_length = np.array([ 4.7, 4.5, 4.9, 4. , 4.6, 4.5,  4.7,  3.3,  4.6,  3.9,  3.5,4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,    4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9, 5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3, 4.2,  4.2,  4.2,  4.3,  3. ,  4.1])
# Plot histogram of versicolor petal lengths
#_ = plt.hist(versicolor_petal_length)

#Plot Histogram with 50 equally spaced intervals
#plt.hist(dataset, density=True, bins = 50)
#Label X and Y Axes in Histogram
plt.xlabel ('Measurement in cms - X axis')
plt.ylabel ('Frequency - Y axis')
#plt.show()
#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python




#from pandas.ploting import scatter_matrix
#import holoviews as hv
#import scipy as sp
#from csv import reader

#def load_iris.csv 
   #file = open iris.csv
   #lines = reader (irisdataset)
   #dataset = list(lines)
   #return dataset