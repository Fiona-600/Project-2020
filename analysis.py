
#Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
import seaborn as sns
# Set Default Seaborn Style
sns.set

#define the column names
header_list = ["Sepal Length", "Sepal Width", "Petal Length" , 'Petal Width' ,'Species' ]

#Read all characters in the file 'irisdataset.csv'

#irisdataset = pd.read_csv("irisdataset.csv", names = header_list)
#alternative coded
irisdataset = pd.read_csv("irisdataset.csv" , names = None)

#type(irisdataset.data)
#Data_Frame = pd.DataFrame (irisdataset.data , columns = Class)
#print (Data_Frame)


#https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

print ("")
print ("First 10 Results")
print ("")
print (irisdataset.head(11))
print ("")
print ("Information about the Iris Data Set")
print ("")
print(irisdataset.describe())
print ("")
print ("List of columns and their data type")
print ("")
print (irisdataset.info())
print ("")
print ("Number of Samples of each variant")
print(irisdataset["class"].value_counts())
print ("")
print (irisdataset.shape)

#plt.figure(figsize = (10, 7)) 
x = irisdataset ["sepal_length"] 
plt.hist(x, bins = 30, color = "green")
x = irisdataset[min ("class")] 
plt.title("Sepal Length Occurences in Iris Data Set") 
plt.xlabel("Sepal Length in cm") 
plt.ylabel("Frequency") 
#plt.show()

#plt.figure(figsize = (10, 7)) 
x = irisdataset["petal_length"] 
plt.hist(x, bins = 20, color = "green") 
plt.title("Petal Length Occurences in Iris Data Set") 
plt.xlabel("Petal Length cm") 
plt.ylabel("Frequency") 
#plt.show()

#divide the data set into three parts
#iris_setosa = irisdataset.loc [irisdataset ["class"]=="Iris-setosa"]
#iris_virginica = irisdataset.loc [irisdataset ["class"]=="Iris-virginica"]
#iris_versicolor = irisdataset.loc [irisdataset ["class"]=="Iris-versicolor"]
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python

#plt.figure(figsize = (10, 7)) 
#x = data["SepalLengthCm"] 
  
#plt.hist(x, bins = 20, color = "green") 
#plt.title("Sepal Length in cm") 
#plt.xlabel("Sepal_Length_cm") 
#plt.ylabel("Count") 


#Working Outputs:

#print (irisdataset.head())

#print("columns",irisdataset.columns)
#print("shape:",irisdataset.shape)
#print(irisdataset["class"].value_counts())
#print (dataset)
#print(irisdataset.describe()) - used
#print("Size:",irisdataset.size)
#source: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#print (irisdataset.info)
#https://kite.com/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python


#This code does not work:
#Data_Frame.hist(column ='Class')
#Data_Frame[‘target’] = dataset[‘Class’]
#print(Data_Frame.headers_list)
#https://medium.com/@gangulym23/practical-pandas-50586fe90cf8
#Print (Data_Frame) produces NaN returns
#print (Data_Frame)
#print(Data_Frame.head())
#print('\n')
#print (irisdataset.data())
#print (iris_setosa) - prints headers only
#print (irisdataset ["Class"]=="Iris-setosa") - prints false for measurements
#f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
#sns.distplot(irisdataset(float["Sepal Length"]) , color="red", ax=axes[0, 0])
#sns.distplot( iris["SepalWidthCm"] , color="yellow", ax=axes[0, 1])
#sns.distplot( iris["PetalLengthCm"] , color="grey", ax=axes[1, 0])
#sns.distplot( iris["PetalWidthCm"] , color="blue", ax=axes[1, 1])


#Label versicolor_petal_length
#versicolor_petal_length = ****This is specifying the input for the histogram, not reading from csv file***
#versicolor_petal_length = np.array([ 4.7, 4.5, 4.9, 4. , 4.6, 4.5,  4.7,  3.3,  4.6,  3.9,  3.5,4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,    4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9, 5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3, 4.2,  4.2,  4.2,  4.3,  3. ,  4.1])
# Plot histogram of versicolor petal lengths
#_ = plt.hist(iris_versicolor_petal_length)

#Working Code
#Plot Histogram with 50 equally spaced intervals
#plt.hist(dataset, density=True, bins = 50)
#Label X and Y Axes in Histogram
#plt.xlabel ('Measurement in cms - X axis')
#plt.ylabel ('Frequency - Y axis')
#plt.show()
#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python




#from pandas.ploting import scatter_matrix
#import holoviews as hv
#import scipy as sp
#from csv import reader

#def load_iris.csv 
   #file = open iris.csv
   #lines = reader (irisdataset)
   #irisdataset = list(lines)
   #return irisdataset