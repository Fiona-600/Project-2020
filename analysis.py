
#Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
import seaborn as sns
# Set Default Seaborn Style
sns.set

# open a new file called Iris_Dataset_Summary.txt to the redirect output of analysis.py
import sys
sys.stdout=open("Iris_Dataset_Summary.txt","w")
#source: https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python

# Use 3 decimal places in output display
pd.set_option("display.precision", 2)
#source: https://realpython.com/pandas-groupby/

#define the column names
header_list = ["Sepal Length", "Sepal Width", "Petal Length" , 'Petal Width' ,'Species' ]

#Read all characters in the file 'irisdataset.csv'
irisdataset = pd.read_csv("irisdataset.csv" , names = None)
#alternative code
#irisdataset = pd.read_csv("irisdataset.csv", names = header_list)

#type(irisdataset.data)
#Data_Frame = pd.DataFrame (irisdataset , columns = header_list)
#print (Data_Frame)

#https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

print ("IRIS DATA SET SUMMARY".center (70))
#source: https://www.geeksforgeeks.org/python-string-ljust-rjust-center/?ref=rp
print ("")
print ("First 10 Results")
print ("")
print ("")
print (irisdataset.head(10))
print ("")
print ("")
print ("Information about the Iris Data Set")
print ("")
print(irisdataset.describe())
print ("")
print ("")
print ("Average(Mean) Length/Width of Petals & Sepals by Species")
print ("")
Mean = irisdataset.groupby(['class']).mean()
print (Mean)
print ("")
print ("")
print ("Standard Deviation of Length/Width of Petals & Sepals by Species")
print ("")
Std = irisdataset.groupby(['class']).std()
print (Std)
print ("")
print ("")
print ("List of columns and their data type")
print ("")
print (irisdataset.info())
print ("")
print ("")
print ("Number of Samples of each Variant")
print ("")
print(irisdataset["class"].value_counts())
print ("")
print ("")
print ("Number of Columns and Number of Rows")
print ("")
print (irisdataset.shape)
print ("")

#divide the data set into three parts
iris_setosa = irisdataset.loc [irisdataset ["class"]=="Iris-setosa"]
iris_virginica = irisdataset.loc [irisdataset ["class"]=="Iris-virginica"]
iris_versicolor = irisdataset.loc [irisdataset ["class"]=="Iris-versicolor"]
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d


plt.figure(figsize = (10, 7)) 
x = irisdataset ["sepal_length"] 
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length Occurences in Iris Data Set") 
plt.xlabel("Sepal Length in cm") 
plt.ylabel("Frequency") 
#plt.show()

x = irisdataset["petal_length"] 
plt.hist(x, bins = 20, color = "blue") 
plt.title("Petal Length Occurences in Iris Data Set") 
plt.xlabel("Petal Length cm") 
plt.ylabel("Frequency") 
#plt.show()

x = irisdataset ["sepal_width"] 
plt.hist(x, bins = 20, color = "red") 
plt.title("Sepal Width Occurences in Iris Data Set") 
plt.xlabel("Sepal Width cm") 
plt.ylabel("Frequency") 
#plt.show()

x = irisdataset ["petal_width"] 
plt.hist(x, bins = 30, color = "yellow") 
plt.title("Petal Width Occurences in Iris Data Set") 
plt.xlabel("Petal Width cm") 
plt.ylabel("Frequency") 
#plt.show()
#https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python

#Multi-dimensional historgram of iris data set by feature and by flower type
Petal_Length = sns.FacetGrid(irisdataset,hue="class",height=3).map(sns.distplot,"petal_length").add_legend().fig.suptitle('Petal Length Occurences by Species')
Petal_Width = sns.FacetGrid(irisdataset,hue="class",height=3).map(sns.distplot,"petal_width").add_legend().fig.suptitle('Petal Width Occurences by Species') 
Sepal_Length = sns.FacetGrid(irisdataset,hue="class",height=3).map(sns.distplot,"sepal_length").add_legend().fig.suptitle('Sepal Length Occurences by Species') 
Sepal_Width = sns.FacetGrid(irisdataset,hue="class",height=3).map(sns.distplot,"sepal_width").add_legend().fig.suptitle('Sepal Width Occurences by Species')
#plt.show()
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

#plt.figure(figsize = (10, 7)) 

#Working Outputs:
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

#./analysis.py > Summary_Text_File.txt

sys.stdout.close()