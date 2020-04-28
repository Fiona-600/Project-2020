
#Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
import seaborn as sns
# Set Default Seaborn Style
sns.set

import sys
# open a new file called Iris_Dataset_Summary.txt to the redirect output of analysis.py
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


#print(iris_setosa.describe())
#print(iris_versicolor.describe())
#print(iris_virginica.describe())

#Plot Histogram with 20 equally spaced intervals in various colours
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
plt.hist(x, bins = 20, color = "yellow") 
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


#TRIAL
#sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
#title="Compare the Distributions of Sepal Length"
#sns.scatterplot(x="class", y="sepal_length", data=irisdataset)

# increasing font size
#plt.title(title, fontsize=26)
# Show the plot
#plt.show()


#sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
#title="Compare the Distributions of Sepal Width"
#sns.scatterplot(x="class", y="sepal_width", data=irisdataset)

# increasing font size
#plt.title(title, fontsize=26)
# Show the plot
#plt.show()


#sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
#title="Compare the Distributions of Petal Length"
#sns.boxplot(x="species", y="petal_length", data=iris_data)

# increasing font size
#plt.title(title, fontsize=26)
# Show the plot
#plt.show()


#sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
#title="Compare the distributions of Petal Width"
#sns.boxplot(x="species", y="petal_width", data=iris_data)

# increasing font size
#plt.title(title, fontsize=26)
# Show the plot
#plt.show()


#for iris_setosa
#counts,bin_edges=np.histogram(iris_setosa["petal_length"],bins=10,density=True)
#pdf=counts/(sum(counts))
#print(pdf)
#print(bin_edges)
#cdf=np.cumsum(pdf)
#plt.plot(bin_edges[1:],pdf)
#plt.plot(bin_edges[1:],cdf)
#plt.show()

#for iris_virginica
#counts,bin_edges=np.histogram(iris_virginica["petal_length"],bins=10,density=True)
#pdf=counts/(sum(counts))
#print(pdf)
#print(bin_edges)

#cdf=np.cumsum(pdf)
#plt.plot(bin_edges[1:],pdf)
#plt.plot(bin_edges[1:],cdf)
#plt.show()

#for iris_versicolor
#counts,bin_edges=np.histogram(iris_versicolor["petal_length"],bins=10,density=True)
#pdf=counts/(sum(counts))
#print(pdf)
#print(bin_edges)
#cdf=np.cumsum(pdf)
#plt.plot(bin_edges[1:],pdf)
#plt.plot(bin_edges[1:],cdf)
#plt.show()



#Scatter Plot
# The indices of the features that we are plotting
#x_index = 0
#y_index = 1

# this formatter will label the colorbar with the correct target names
#formatter = plt.FuncFormatter(lambda i, *args: irisdataset.target_names[int(i)])

#plt.figure(figsize=(5, 4))
#plt.scatter(irisdataset[:, x_index], irisdataset[:, y_index], c=irisdataset.target)
#plt.colorbar(ticks=[0, 1, 2], format=formatter)
#plt.xlabel(irisdataset.feature_names[x_index])
#plt.ylabel(irisdataset.feature_names[y_index])
#plt.tight_layout()
#plt.show()

#source: http://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html


#from sklearn import datasets
# Load some data
#iris = datasets.load_irisdataset()
#iris_df = pd.DataFrame(irisdataset['data'], columns= header_list)
#iris_df = pd.DataFrame (irisdataset , columns = header_list)
#iris_df ['class'] = irisdataset ['target']

#colours = ['red', 'orange', 'blue']
#species = ['I. setosa', 'I. versicolor', 'I. virginica']

#for i in range(0, 3):    
    #species_df = iris_df[iris_df['species'] == i]    
    #plt.scatter(        
        #species_df['sepal length (cm)'],        
        #species_df['petal length (cm)'],
        #color=colours[i],        
        #alpha=0.5,        
        #label=species[i]   
    #)

#plt.xlabel('sepal length (cm)')
#plt.ylabel('petal length (cm)')
#plt.title('Iris dataset: petal length vs sepal length')
#plt.legend(loc='lower right')

#plt.show()

#Scatterplot Grid
#sns.set_style("whitegrid")
#sns.pairplot(irisdataset,hue="class",height=3);
#plt.show()
#source: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d




#https://kite.com/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python
#https://medium.com/@gangulym23/practical-pandas-50586fe90cf8

#This code does not work:
#Data_Frame.hist(column ='Class')
#Data_Frame[‘target’] = dataset[‘Class’]
#print(Data_Frame.headers_list)
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


#from pandas.ploting import scatter_matrix
#import holoviews as hv
#import scipy as sp
#from csv import reader


sys.stdout.close()