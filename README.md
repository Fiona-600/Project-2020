**Programming & Scripting Final Project Submission** -
**GMIT Higher Diploma in Data Analytics**

**Submitted by Fiona Lee - 29 April 2020**

**Introduction**

The Iris flower data set or Fisher’s Iris data was introduced by the British statistician and biologist Ronald Fisher 1936 as an example of linear discriminant analysis.  The data set is a multivariate data set which involves the observation and analysis of more than one statistical outcome variable at a time.  It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. 

*source: https://en.wikipedia.org/wiki/Iris_flower_data_set*

There are 3 species of iris flower (Setosa, Virginica, Versicolour), with 50 examples of each type. 

*Fig 1 – 3 Species of Iris*

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Fig%201%20Iris%20variants.png?raw=true)

*Repository Link: https://github.com/Fiona-600/Project-2020/blob/master/Fig%201%20Iris%20variants.png*


**Preliminary Findings & Interpretation of the Data Set**

**Qualities and attributes of the Iris dataset**

The Iris dataset contains 150 examples (rows), and 5 variables (columns) named; sepal length, sepal width, petal length, petal width, and species    

Each row of the table represents one Iris flower, including its species and dimensions of its botanical anatomy (sepal length, sepal width, petal length, petal width) - see fig. 2 below..


*Fig. 2 - Iris Data Set Sample*

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Fig%202%20%20Iris%20Data%20Set%20-%20First%2010%20Results.PNG?raw=true)

*Repository Link: https://github.com/Fiona-600/Project-2020/blob/master/Fig%202%20%20Iris%20Data%20Set%20-%20First%2010%20Results.PNG




For each sample, four features were measured i.e. 

  -	Sepal length in centimetres
  -	Sepal width in centimetres
  -	Petal length in centimetres
  -	Petal width in centimetres 

A flower is classified as either among those based on the four features given. Fisher developed a linear discriminant model to distinguish the species from each other based on the combination of these four features.

The iris 'petal' and 'sepal' are indicated in fig. 3 below.


*Fig 3 - Iris Petals and Sepals

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Fig%203%20%20Iris%20petal%20and%20sepal.png?raw=true)

*Repository link: https://github.com/Fiona-600/Project-2020/blob/master/Fig%203%20%20Iris%20petal%20and%20sepal.png*

**Detailed Analysis - Initial Findings**

The detailed results of the initial analysis on ‘Iris Data Set’ are contained in the Iris_Dataset_Summary.txt file.

*Repository Link: https://github.com/Fiona-600/Project-2020/blob/master/Iris_Dataset_Summary.txt*

A summary of the initial analysis is detailed below:

*Table 2 - Number of Samples of each Variant*

  There are 3 species of iris flower (Setosa, Virginica, Versicolour), with 50 examples of each type. The number of data points for each class is equal, thus it is a balanced dataset.

*Table 3 - Number of Columns and Number of Rows*

  The Iris dataset contains 150 rows and 5 columns

*Table 4 - General Information about the Iris Data Set*

  General information gives us mean, standard deviation, min and max information about the combined averages across the three iris species. This tells us only that iris versicolor is the closest to the average iris overall species measurement.

*Table 5 - Mean, Median, Standard Deviation, Min and Max Values by Species*

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Fig%204%20Dataset%20Information%20by%20variable.PNG?raw=true)

**Conclusions**

  *Sepal Length:*

  ‘Iris_Setosa’ is the most consistent variety of Iris in terms of sepal length measurements in the sample.  The standard deviation of 0.35 is a calculation of the variation or spread of measurements recorded between the min value of 4.3 and max value of 5.8 across the sample versus the average measurement of 5.01.

   ‘Iris Virginica’ is the least consistent with a standard deviation of 0.64, mean of 6.59 and samples ranging from 4.9 to 7.9.

  *Sepal Width:*

   ‘Iris_Versicolor’ is the most consistent in terms of sepal width as it has the lowest standard deviation of 0.31 versus the average value of 2.77 and samples ranging from 2.0 to 3.4.

   ‘Iris Setosa’ is the least consistent with a standard deviation of 0.38, mean of 3.42 and samples ranging from 2.3 to 4.4.

  *Petal Length:*

  ‘Iris_Setosa’ is by far the most consistent in terms of petal length as it has the lowest standard deviation of 0.17 versus the average value of 1.46 and samples ranging from 1.0 to 1.9.

  ‘Iris Virginica’ is the least consistent with a standard deviation of 0.55, mean of 5.55 and samples ranging from 4.5 to 6.9.

  *Petal Width:*

  ‘Iris_Setosa’ is again by far the most consistent in terms of petal width as it has the lowest standard deviation of 0.11 versus the average value of 0.24 and samples ranging from 0.1 to 0.6.

  ‘Iris Virginica’ is the least consistent with a standard deviation of 0.27, mean of 2.03 and samples ranging from 1.4 to 2.5.

  Overall, ‘Iris Setosa is the most consistent across the sample measured and Iris Virginica’ was the least consistent.

**Purpose of the project**

To research the iris flower data set and to prepare a presentation to investigate the data set with a view to explaining it to your colleagues in a few weeks’ time.

The presentation will include:

1.	An explanation of what investigating a data set entails
2.	How python can be used to investigate the data set
3.	The required code for the analysis using python
4.	The resulting output of the code


**Structure & Project Navigation**

The project will be stored in a GITHUB Repository at url: https://github.com/Fiona-600/Project-2020.git

1.	The GITHUB repository will contain:

    •	Png files called ‘Fig 1 iris variants.png’ and ‘fig 3 iris petals and sepals.png’ which contains images of the variants of iris identified in the study i.e. Iris setosa, Iris    virginica and Iris versicolor and an indication of the location of the flower's petals and sepals.

    •	Png files called Fig 2 Iris Data Set - First 10 Results.PNG and Fig 4 Dataset Information by variable.png which are samples from the Iris_Dataset_Summary.txt file       

    •	A text file called ‘irisdataset.txt’ containing a download the data set
     
    •	A text file called ‘irisdataset.csv’ containing a download the data set

    •	A ‘LICENSE’ file containing a copy of the MIT Licence

    •	A ‘README.md’ file which contains:

          •	The data set itself
          •	Online and other research into the data set
          •	Investigations into the data set
          •	How to run the python code
          •	What that code does.
          •	All references used in completing the project

    •	A python program file called ‘analysis.py’ which will:

          1.  Output a summary of each variable to 'Iris_Dataset_Summary.txt
          2.  Save a histogram of each variable to png. ﬁles (Appendices 1-8)
          3.  Output a scatter plot of each pair of variables (Appendices 9-11)


**Investigation Approach using Python**

An explanation of what investigating a data set entails

Python program file ‘analysis.py’ will analyse the following aspects of the data set 

    1.  Summarises each variable to a single text ﬁle
    2.  Presents a histogram of each variable to png. ﬁles
    3.  Outputs a scatter plot of each pair of variables

*Insight into raw data*

*The data analysis*

*Variables*

    •	sepal_length: Sepal length, in centimeters, used as input.
    •	sepal_width:  Sepal width, in centimeters, used as input.
    •	petal_length: Petal length, in centimeters, used as input.
    •	petal_width:  Petal width, in centimeters, used as input.
    •	class: Iris Setosa, Versicolor or Virginica, used as target

**Findings and Conclusions**

**Fig ?. Histogram - Sepal Length**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%201%20-%20Sepal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set.png?raw=true)
**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%201%20-%20Sepal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set.png



**Fig ?. Histogram - Sepal Length by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%202%20-%20Sepal%20Length%20Occurances%20in%20the%20Iris%20Data%20Set%20by%20Species.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%202%20-%20Sepal%20Length%20Occurances%20in%20the%20Iris%20Data%20Set%20by%20Species.png


**Fig ?. Histogram - Sepal Width**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%203%20-%20Sepal%20Width%20%20Occurences%20in%20the%20Iris%20Data%20Set.png?raw=true)
**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%203%20-%20Sepal%20Width%20%20Occurences%20in%20the%20Iris%20Data%20Set.png


**Fig ?. Histogram - Sepal Width by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%204%20-%20Sepal%20Width%20Occurences%20in%20the%20Iris%20Data%20Set%20by%20Species.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%204%20-%20Sepal%20Width%20Occurences%20in%20the%20Iris%20Data%20Set%20by%20Species.png


**Fig ?. Histogram - Petal Length**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%205%20-%20Petal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set.png?raw=true)
**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%205%20-%20Petal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set.png


**Fig ?. Histogram - Petal Length by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%206%20-%20Petal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set%20by%20Species.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%206%20-%20Petal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set%20by%20Species.png


**Fig ?. Histogram - Petal Width**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%207%20-%20Petal%20Width%20Occurences%20in%20the%20Iris%20Data%20Set.png?raw=true)
**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%207%20-%20Petal%20Width%20Occurences%20in%20the%20Iris%20Data%20Set.png


**Fig ?. Histogram - Petal Width by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%208%20-%20Petal%20Width%20Occurences%20in%20the%20Iris%20Data%20Set%20by%20Species.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%207%20-%20Petal%20Length%20Occurences%20in%20the%20Iris%20Data%20Set%20by%20Species.png


**Fig ?. Scatter Plot - Petal Width vs Petal Length by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%209%20-%20Sample%20Scatterplot%20Petal%20Width%20vs%20Petal%20Length%20by%20Species%20-%20Without%20%20Regression%20Lines.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%209%20-%20Sample%20Scatterplot%20Petal%20Width%20vs%20Petal%20Length%20by%20Species%20-%20Without%20%20Regression%20Lines.png


**Fig ?. Sample Scatter Plot with Regression Lines- Petal Width vs Petal Length by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%2010%20-%20Sample%20Scatterplot%20Petal%20Width%20vs%20Petal%20Length%20by%20Speciesv-%20with%20Regression%20Lines.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%2010%20-%20Sample%20Scatterplot%20Petal%20Width%20vs%20Petal%20Length%20by%20Speciesv-%20with%20Regression%20Lines.png


**Fig ?. Scatter Plot Grid - Comparison of All Variables by Species**

![alt text](https://github.com/Fiona-600/Project-2020/blob/master/Appendix%2011%20-%20Scatter%20Plot%20Grid%20-%20Compare%20All%20Variables.png?raw=true)

**Repository Link**: https://github.com/Fiona-600/Project-2020/blob/master/Appendix%2011%20-%20Scatter%20Plot%20Grid%20-%20Compare%20All%20Variables.png




**Technology Used**

*Required Programs*

	•	Anaconda Navigator 3
	•	Visual Studio Code
	•	Python version 3.7.4
  •	Cmder 
	•	GitHub
 	•	MS Office 
	•	Firefox Internet Explorer

  *Procedure for downloading required programs
  
*Libraries and Modules*

•	NumPy - The fundamental package for scientific computing with Python

    ‘import numpy as np’

•	Pandas – An open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools

    ‘import pandas as pd’
    
•	Matplotlib

    ‘import matplotlib.pyplot as plt’

•	Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

    ‘import seaborn as sns’

Iris Data Set

![alt text](![alt text](https://raw.githubusercontent.com/Fiona-600/Project-2020/master/Iris%20petal%20and%20sepal.png?raw=true)?raw=true)

source: https://drive.google.com/file/d/1UJWvXXA5OygZa5cQg7N5xLfSxrXKg6An/view