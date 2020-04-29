#Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
import seaborn as sns
# Set Default Seaborn Style
sns.set

# Open a new file called Iris_Dataset_Summary.txt to the redirect output of analysis.py
# Source: https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
import sys
sys.stdout=open("Iris_Dataset_Summary.txt","w")

# Use 3 decimal places in output display
# Source: https://realpython.com/pandas-groupby/
pd.set_option("display.precision", 2)

# Read all characters in the file 'irisdataset.csv'
# Source: https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
irisdataset = pd.read_csv("irisdataset.csv" , names = None , index_col = 0)
irisdataset = pd.read_csv('irisdataset.csv',header=0).iloc[:,0:5]

print ("IRIS DATA SET SUMMARY".center (70))
# Source: https://www.geeksforgeeks.org/python-string-ljust-rjust-center/?ref=rp
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
print ("Appendices")
print ("")

# HISTOGRAMS (By Feature Only)
# https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python
print ("HISTOGRAMS")
print ("")
# Histogram to plot 'Sepal Length' measurement in cms frequency in green  - All Varieties")
print ("Appendix 1  - Single Dimensional Historgram of Iris Data Set by Sepal Length")
plt.figure(figsize = (10, 7)) 
x = irisdataset ["sepal_length"] 
plt.hist(x, bins = 20, color = "green" , rwidth = 0.95)
# rwidth adds a space between the bars, bins are the number of bars
plt.title("Appendix 1 - Sepal Length Occurences in Iris Data Set") 
plt.legend
plt.xlabel("Sepal Length in cm") 
plt.ylabel("Frequency") 
plt.show()
# Histogram to plot 'Sepal Width' measurement in cms frequency in red - All Varieties
print ("Appendix 2  - Single Dimensional Historgram of Iris Data Set by Sepal Width")
plt.figure(figsize = (10, 7)) 
x = irisdataset ["sepal_width"] 
plt.hist(x, bins = 20, color = "red", rwidth = 0.95) 
plt.title("Appendix 2 - Sepal Width Occurences in Iris Data Set") 
plt.xlabel("Sepal Width cm") 
plt.ylabel("Frequency") 
plt.show()
# Histogram to plot 'Petal Length' measurement in cms frequency in blue - All Varieties
print ("Appendix 3  - Single Dimensional Historgram of Iris Data Set by Petal Length")
plt.figure(figsize = (10, 7)) 
x = irisdataset["petal_length"] 
plt.hist(x, bins = 20, color = "blue", rwidth = 0.95) 
plt.title("Appendix 3 - Petal Length Occurences in Iris Data Set") 
plt.xlabel("Petal Length cm") 
plt.ylabel("Frequency") 
plt.show()
# Histogram to plot 'Petal Width' measurement in cms frequency in yellow - All Varieties
print ("Appendix 4  - Single Dimensional Historgram of Iris Data Set by Petal Width")
plt.figure(figsize = (10, 7)) 
x = irisdataset ["petal_width"] 
plt.hist(x, bins = 20, color = "yellow", rwidth = 0.95) 
plt.title("Appendix 4 - Petal Width Occurences in Iris Data Set") 
plt.xlabel("Petal Width cm") 
plt.ylabel("Frequency") 
plt.show()

#MULTI DIMENSIONAL HISTOGRAMS (By Feature & Species)
# Source: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
print ("Appendix 5  - Multi-Dimensional Historgram of iris data set showing frequency of Sepal Length by Flower type")
Sepal_Length = sns.FacetGrid(irisdataset,hue="class",height=6).map(sns.distplot,"sepal_length").add_legend().fig.suptitle('Appendix 5 - Sepal Length Occurences by Species') 
sns.set_style ("whitegrid")
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Sepal_Length = sns.figsize = a4_dims
plt.show()
print ("Appendix 6  - Multi-Dimensional Historgram of iris data set showing frequency of Sepal Width by Flower type")
Sepal_Width = sns.FacetGrid (irisdataset, hue = "class", height = 6).map (sns.distplot,"sepal_width").add_legend().fig.suptitle ('Appendix 6 - Sepal Width Occurences by Species')
sns.set_style ("whitegrid")
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Sepal_Width = sns.figsize = a4_dims
plt.show()
print ("Appendix 7  - Multi-Dimensional Historgram of iris data set showing frequency of Petal Length by Flower type")
Petal_Length = sns.FacetGrid (irisdataset, hue = "class", height =6).map (sns.distplot,"petal_length").add_legend().fig.suptitle ('Appendix 7 - Petal Length Occurences by Species')
sns.set_style ('whitegrid')
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Petal_Length = sns.figsize = a4_dims
plt.show()
print ("Appendix 8  - Multi-Dimensional Historgram of iris data set showing frequency of Petal Width by Flower type")
Petal_Width = sns.FacetGrid (irisdataset, hue = "class", height = 5).map (sns.distplot,"petal_width").add_legend().fig.suptitle ('Appendix 8 - Petal Width Occurences by Species') 
sns.set_style ('whitegrid')
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Petal_Width = sns.figsize = a4_dims
plt.show()

# SCATTER PLOTS:
# Source: Scatterplot Tutorial - https://seaborn.pydata.org/generated/seaborn.scatterplot.html
# SCATTERPLOT BY SPECIES - WITHOUT REGRESSION LINES
print ("Appendix 9 - Scatterplot without Regression Lines - Sample Code to compare 'Petal Width' vs 'Petal Length' by Species")
sns.set (style = "whitegrid", palette ='Set2')
sns.set_style ("ticks")
ax = sns.scatterplot(x="petal_width", y="petal_length", hue = "class" , data=irisdataset)
ax.set_title ("Appendix 9 - Scatterplot Petal Width vs Petal Length")
a4_dims = (11.7, 8.27)
fig , ax = sns.figsize = a4_dims
plt.show()
# SCATTERPLOT BY SPECIES - WITH REGRESSION LINES
# Source: https://stackoverflow.com/questions/46307941/how-can-i-add-title-on-seaborn-lmplot
print ("Appendix 10  - Scatterplot with Regression Lines - Sample Code to compare 'Petal Width' vs 'Petal Length' by Species - With Regression Lines")
sns.set_style ("whitegrid")
sns.set_style ("ticks")
ax = sns.lmplot (x ="petal_width" , y = "petal_length" , palette = 'Set2', hue = "class", data = irisdataset, height = 6)
ax.fig.suptitle ("Appendix 10 - Scatterplot Petal Width vs Petal Length", fontsize = 12)
a4_dims = (11.7, 8.27)
fig , ax = sns.figsize = a4_dims
plt.show()
# This code can be changed to compare other variables by replacing 'petal_width' and 'petal_length in lines 146/147 and 157/158
# with alternate variables i.e sepal_length and sepal_width
# A more efficient way to perform this comparison is to use the 'Scatterplot grid' method which compares all variables
# in one plot (see below)

# SCATTERPLOT GRID COMPARING ALL VARIABLES
# Source: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
print ("Appendix 11 - Scatterplot Grid - Compare 'Sepal Width' vs 'Sepal Length' vs 'Petal Width' vs 'Petal Length' by Species - Without Regression Lines")
sns.set_style ("whitegrid")
sns.set_style ("ticks")
ax = sns.pairplot (irisdataset, hue="class", height=2);
# Source: https://stackoverflow.com/questions/52096050/seaborn-title-position
plt.title('title', loc='left')
plt.subplots_adjust(top=0.9)
# Source: https://stackoverflow.com/questions/36813396/how-to-show-the-title-for-the-diagram-of-seaborn-pairplot-or-pridgrid
# Source: y=1 refers to location of the heading - https://stackoverflow.com/questions/52096050/seaborn-title-position
ax.fig.suptitle ("Appendix 11 - Scatterplot Grid - Compare All Variables i.e. Petal Width, Petal Length, Sepal Width, Sepal Length by Species", fontsize = 11)
# Scale to print on A4 sheet
a4_dims = (11.7, 8.27)
fig , ax = sns.figsize = a4_dims
plt.show()

#Close output text file
sys.stdout.close()
