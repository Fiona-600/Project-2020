# Fiona Lee
# Programming & Scripting Final Assigment - Iris Data Set

# Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Ref Source: https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
import seaborn as sns
# Set Default Seaborn Style
sns.set

# Open a new file called Iris_Dataset_Summary.txt to the redirect output of analysis.py
# Ref Source: https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
import sys
sys.stdout=open("Iris_Dataset_Summary.txt","w")

# Use 3 decimal places in output display
# Ref Source: https://realpython.com/pandas-groupby/
pd.set_option("display.precision", 2)

# Read all characters in the file 'irisdataset.csv'
# Ref Source: https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
irisdataset = pd.read_csv("irisdataset.csv" , names = None , index_col = 0)
irisdataset = pd.read_csv('irisdataset.csv',header=0).iloc[:,0:5]

# Print Outputs to Iris_Data_Summary.txt file
print ("IRIS DATA SET SUMMARY".center (70))
# Ref Source: https://www.geeksforgeeks.org/python-string-ljust-rjust-center/?ref=rp
print ("")
print ("Table 1 -  First 10 Results")
print ("")
print (irisdataset.head(10))
print ("")
print ("")
print ("Table 2 -  Number of Samples of each Variant")
print ("")
print(irisdataset["class"].value_counts())
print ("")
print ("")
print ("Table 3 -  Number of Columns and Number of Rows")
print ("")
print (irisdataset.shape)
print ("")
print ("")
print ("Table 4 -  General Information about the Iris Data Set")
print ("")
print(irisdataset.describe())
print ("")
print ("")
print ("Table 5 -  Mean, Median, Standard Deviation, Min and Max Values by Species")
# Ref Source: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40
print ("") 
print ("Sepal Length")
print (irisdataset.groupby(['class']).agg(['mean', 'median' , 'std', 'min', 'max']).sepal_length)
print ("")
print ("Sepal Width")
print (irisdataset.groupby(['class']).agg(['mean', 'median' , 'std', 'min', 'max']).sepal_width)
print ("")
print ("Petal Length")
print (irisdataset.groupby(['class']).agg(['mean', 'median' , 'std', 'min', 'max']).petal_length)
print ("")
print ("Petal Width")
print (irisdataset.groupby(['class']).agg(['mean', 'median' , 'std', 'min', 'max']).petal_width)
print ("")
print ("")
print ("Table 6  - List of Columns and Their Data Type")
print ("")
print (irisdataset.info())
print ("")
print ("")
print ("APPENDICES - List of Outputs")
print ("")
print ("HISTOGRAMS")
print ("Appendix 1  - Single Dimensional Historgram of Iris Data Set by Sepal Length")
print ("Appendix 2  - Multi-Dimensional Historgram of Iris Data Set showing the Frequency of Sepal Length by Variant")
print ("Appendix 3  - Single Dimensional Historgram of Iris Data Set by Sepal Width")
print ("Appendix 4  - Multi-Dimensional Historgram of Iris Data Set showing the Frequency of Sepal Width by Variant")
print ("Appendix 5  - Single Dimensional Historgram of Iris Data Set by Petal Length")
print ("Appendix 6  - Multi-Dimensional Historgram of Iris Data Set showing the Frequency of Petal Length by Variant")
print ("Appendix 7  - Single Dimensional Historgram of Iris Data Set by Petal Width")
print ("Appendix 8  - Multi-Dimensional Historgram of Iris Data Set showing the Frequency of Petal Width by Variant")
print ("")
print ("SCATTERPLOTS")
print ("Appendix 9   - Scatterplot without Regression Lines - Compare 'Petal Width' vs 'Petal Length' by Species")
print ("Appendix 9a  - Scatterplot without Regression Lines - Compare 'Petal Length' vs 'Sepal Length' by Species")
print ("Appendix 9b  - Scatterplot without Regression Lines - Compare 'Petal Width' vs 'Sepal Length' by Species")
print ("Appendix 10  - Scatterplot with Regression Lines - Compare 'Petal Width' vs 'Petal Length' by Species - With Regression Lines")
print ("Appendix 10a - Scatterplot with Regression Lines - Compare 'Petal Length' vs 'Sepal Length' by Species - With Regression Lines")
print ("Appendix 10b - Scatterplot with Regression Lines - Compare 'Petal Width' vs 'Sepal Length' by Species - With Regression Lines")
print ("Appendix 11  - Scatterplot Grid - Compare 'Sepal Width' vs 'Sepal Length' vs 'Petal Width' vs 'Petal Length' by Species - Without Regression Lines")

# HISTOGRAMS (By Feature Only)
# Ref Source: https://stackoverflow.com/questions/55718675/make-histogram-from-csv-file-with-python
# Histogram to plot 'Sepal Length' measurement in cms frequency in green  - All Varieties")
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
plt.figure(figsize = (10, 7)) 
x = irisdataset ["sepal_width"] 
plt.hist(x, bins = 20, color = "red", rwidth = 0.95) 
plt.title("Appendix 3 - Sepal Width Occurences in Iris Data Set") 
plt.xlabel("Sepal Width cm") 
plt.ylabel("Frequency") 
plt.show()
# Histogram to plot 'Petal Length' measurement in cms frequency in blue - All Varieties
plt.figure(figsize = (10, 7)) 
x = irisdataset["petal_length"] 
plt.hist(x, bins = 20, color = "blue", rwidth = 0.95) 
plt.title("Appendix 5 - Petal Length Occurences in Iris Data Set") 
plt.xlabel("Petal Length cm") 
plt.ylabel("Frequency") 
plt.show()
# Histogram to plot 'Petal Width' measurement in cms frequency in yellow - All Varieties
plt.figure(figsize = (10, 7)) 
x = irisdataset ["petal_width"] 
plt.hist(x, bins = 20, color = "yellow", rwidth = 0.95) 
plt.title("Appendix 7 - Petal Width Occurences in Iris Data Set") 
plt.xlabel("Petal Width cm") 
plt.ylabel("Frequency") 
plt.show()

#MULTI DIMENSIONAL HISTOGRAMS (By Feature & Species)
# Ref Source: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
Sepal_Length = sns.FacetGrid (irisdataset,hue="class",height = 6).map(sns.distplot,"sepal_length").add_legend().fig.suptitle('Appendix 2 - Sepal Length Occurences by Species') 
sns.set_style ("whitegrid")
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Sepal_Length = sns.figsize = a4_dims
plt.show()
Sepal_Width = sns.FacetGrid (irisdataset, hue = "class", height = 6).map (sns.distplot,"sepal_width").add_legend().fig.suptitle ('Appendix 4 - Sepal Width Occurences by Species')
sns.set_style ("whitegrid")
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Sepal_Width = sns.figsize = a4_dims
plt.show()
Petal_Length = sns.FacetGrid (irisdataset, hue = "class", height = 6).map (sns.distplot,"petal_length").add_legend().fig.suptitle ('Appendix 6 - Petal Length Occurences by Species')
sns.set_style ('whitegrid')
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Petal_Length = sns.figsize = a4_dims
plt.show()
Petal_Width = sns.FacetGrid (irisdataset, hue = "class", height = 5).map (sns.distplot,"petal_width").add_legend().fig.suptitle ('Appendix 8 - Petal Width Occurences by Species') 
sns.set_style ('whitegrid')
sns.set_style ("ticks")
a4_dims = (11.7, 8.27)
fig , Petal_Width = sns.figsize = a4_dims
plt.show()

# SCATTER PLOTS:
# Ref Source: Scatterplot Tutorial - https://seaborn.pydata.org/generated/seaborn.scatterplot.html
# SCATTERPLOT BY SPECIES - WITHOUT REGRESSION LINES
sns.set (style = "whitegrid", palette ='Set2')
sns.set_style ("ticks")
ax = sns.scatterplot (x = "petal_width", y ="petal_length", hue = "class" , data = irisdataset)
ax.set_title ("Appendix 9 - Scatterplot Petal Width vs Petal Length")
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()
sns.set (style = "whitegrid", palette ='Set2')
sns.set_style ("ticks")
ax = sns.scatterplot (x = "petal_length", y ="sepal_length", hue = "class" , data = irisdataset)
ax.set_title ("Appendix 9a - Scatterplot Petal Length vs Sepal Length")
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()
sns.set (style = "whitegrid", palette ='Set2')
sns.set_style ("ticks")
ax = sns.scatterplot (x = "petal_width", y ="sepal_length", hue = "class" , data = irisdataset)
ax.set_title ("Appendix 9b - Scatterplot Petal Width vs Sepal Length")
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()
# SCATTERPLOT BY SPECIES - WITH REGRESSION LINES
# Ref Source: https://stackoverflow.com/questions/46307941/how-can-i-add-title-on-seaborn-lmplot
sns.set_style ("whitegrid")
sns.set_style ("ticks")
ax = sns.lmplot (x = "petal_width" , y = "petal_length" , palette = 'Set2', hue = "class", data = irisdataset, height = 6)
ax.fig.suptitle ("Appendix 10 - Scatterplot Petal Width vs Petal Length", fontsize = 12)
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()
sns.set_style ("whitegrid")
sns.set_style ("ticks")
ax = sns.lmplot (x = "petal_length" , y = "sepal_length" , palette = 'Set2', hue = "class", data = irisdataset, height = 6)
ax.fig.suptitle ("Appendix 10a - Scatterplot Petal Length vs Sepal Length", fontsize = 12)
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()
sns.set_style ("whitegrid")
sns.set_style ("ticks")
ax = sns.lmplot (x = "petal_width" , y = "sepal_length" , palette = 'Set2', hue = "class", data = irisdataset, height = 6)
ax.fig.suptitle ("Appendix 10b - Scatterplot Petal Width vs Sepal Length", fontsize = 12)
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()

# This code can be changed to compare other variables by replacing 'petal_width' and 'petal_length in lines 159/160 and 182/183
# with alternate variables i.e sepal_length and sepal_width
# A more efficient way to perform this comparison is to use the 'Scatterplot grid' method which compares all variables
# in one plot (see below)

# SCATTERPLOT GRID COMPARING ALL VARIABLES
# Ref Source: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
sns.set_style ("whitegrid")
sns.set_style ("ticks")
ax = sns.pairplot (irisdataset, hue="class", height=2);
# Ref Source: https://stackoverflow.com/questions/52096050/seaborn-title-position
plt.title('title', loc ='left')
plt.subplots_adjust(top=0.9)
# Ref Source: https://stackoverflow.com/questions/36813396/how-to-show-the-title-for-the-diagram-of-seaborn-pairplot-or-pridgrid
# Ref Source: y=1 refers to location of the heading - https://stackoverflow.com/questions/52096050/seaborn-title-position
ax.fig.suptitle ("Appendix 11 - Scatterplot Grid - Compare All Variables i.e. Petal Width, Petal Length, Sepal Width, Sepal Length by Species", fontsize = 11)
# Scale to print on A4 sheet
a4_dims = (11.7, 8.27)
fig, ax = sns.figsize = a4_dims
plt.show()

#Close output text file
sys.stdout.close()
