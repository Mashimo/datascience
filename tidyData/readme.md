# TidyData - Get and clean data from wearables UCI repository
## About
This readme describes the transformations performed to convert the raw data into the tidy data.

You can run the file *run_analysis.R* on the raw data to get the tidy data.  
There are no parameters in the script.  
Below are the steps performed in the script.

## Pre-requisites:
The raw dataset has been downloaded and unzipped in the same directory where the script is located. An alert message is displayed if the files do not exist.

## Steps for tidying the data:
Assuming that all files have been read in memory.

1. Merge the training and the test sets to create one data set. This will be the main data frame.  
Since test and train files have variables with common names - you can verify with _intersect(names(df1), names(df2))_,
 then you can use a normal _merge()_ function.  
Just be sure you always follow the same order. In this case it's first test, then train.

2. Uses descriptive activity names to name the activities in the data set  
The variables of the X data are the single measurements and they are described in the file features.txt 
(that went into the data frame called “features”): each feature has a label in the text.  
The script simply extracts the labels (variable “name” in features) and add them to the X data set.

3. Extracts only the measurements on the mean and standard deviation for each measurement.  
Some measurements (such as mean or max) have been derived in the original data set. We want only them.  
Which they are, it can be found from the column name of the X data set, for example using the _grepl()_ function.  
Every feature that contains the string “mean” OR “Mean” OR “std” is taken.

4. Appropriately labels the data set with descriptive variable names.  
The  features have already the correct name (step 2); the script now:
 - adds the subject to the main data frame (allX) and change its column into “Subject”
 - adds the activity to the main data frame (allX) and map the correct activity label using the _match()_ function.

5. From the data set in step 4, **creates a second, independent tidy data set with the average of each variable for each activity and each subject.**
 - Creates a new data frame called tidy by first grouping the main data set by Subject and Activity; using the *group_by()* function from the _dplyr_ package
 - the result is piped into the the function *summarise_each()* and passing to it the function _mean()_. This calculates the mean for each group.

6. Last, create the final tidy data set to be uploaded  
The file is created in the same directory where the script is. **The name is “tiny_data.txt”**

## How to read the tidy data set
Use these R lines (from the path where the file is):
<pre>
  data <- read.table("tiny_data.txt", header = TRUE)
  View(data)
</pre>