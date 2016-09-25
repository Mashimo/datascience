Codebook wearable data
======================
title: "Codebook wearable data”  
author: “Mashimo”  
date: June 2015  
 
## Project Description
 Prepare tidy data that can be used for later analysis about wearables.  
 Part of Getting and cleaning Data course.
 
## Collection of the raw data
The experiments have been carried out with a group of 30 volunteers within an age bracket of 19-48 years. 
Each person performed six activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. 
Using its embedded accelerometer and gyroscope, we captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. 
The experiments have been video-recorded to label the data manually. 
The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data. 
 
### Notes on the original (raw) data 
* activity_labels.txt : simply the six labels and a code associated
* features.txt : description for each of the 561 variables measured
* X-test  / X_train : train and test files contain observations of time and frequency domain 561 variables. 
These variables are described in the file features.txt
* Y_test/ Y_train : for each observation this is the activity code (relation between obs. and label)
* subject_test / subject_train : for each observation this is the volunteer who did the activity. 
Its range is from 1 to 30.  

## Creating the tidy datafile
 
### Guide to create the tidy data file
1. download the data from [the UCI repository](https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip)
2. download the script *run_analysis.R* from [this GitHub repo](https://github.com/Mashimo/JHU-DataScience-TidyData)
3. store the two files in the same directory
4. unzip the dataset so it creates a folder called "UCI HAR Dataset”
5. run the script - no parameters are needed
6. the script produces a text file called tiny_data.txt in the same directory  


### Cleaning of the data
The included script performs the following steps:  

1. merge the training and the test data into one set
2. use descriptive activity names to name the activities in the data set
3. extract only the measurements on the mean and standard deviation for each measurement. 
4. appropriately label the data set with descriptive variable names. 
5. create a second, independent tidy data set with the average of each variable for each activity and each subject

**Details for each step are in the readMe document:  readMe.md  (same GitHub repo)**
 
## Description of the variables in the tiny_data.txt file
### Dimensions of the dataset:  
   30 subjects * 6 activities = 180 observations (lines)  
   Subject + Activity + 86 features = 88 variables (columns) 
### Variables present in the dataset  
* Subject: code identifying the test subject (int from 1 to 30)
* Activity: factor with 6 levels such as “LAYING”, “SITTING”
* a list of total 86 features for the mean or standard deviations measured

If you are really curious, here are the 86 features, separated by comma:

tBodyAcc-mean()-X, tBodyAcc-mean()-Y, tBodyAcc-mean()-Z, tBodyAcc-std()-X, tBodyAcc-std()-Y,
 tBodyAcc-std()-Z, tGravityAcc-mean()-X (dbl), tGravityAcc-mean()-Y (dbl), tGravityAcc-mean()-Z (dbl), tGravityAcc-std()-X (dbl), tGravityAcc-std()-Y (dbl), tGravityAcc-std()-Z (dbl), tBodyAccJerk-mean()-X (dbl), tBodyAccJerk-mean()-Y (dbl),
  tBodyAccJerk-mean()-Z (dbl), tBodyAccJerk-std()-X (dbl), tBodyAccJerk-std()-Y (dbl), tBodyAccJerk-std()-Z (dbl),
  tBodyGyro-mean()-X (dbl), tBodyGyro-mean()-Y (dbl), tBodyGyro-mean()-Z (dbl), tBodyGyro-std()-X (dbl), tBodyGyro-std()-Y
  (dbl), tBodyGyro-std()-Z (dbl), tBodyGyroJerk-mean()-X (dbl), tBodyGyroJerk-mean()-Y (dbl), tBodyGyroJerk-mean()-Z (dbl),
  tBodyGyroJerk-std()-X (dbl), tBodyGyroJerk-std()-Y (dbl), tBodyGyroJerk-std()-Z (dbl), tBodyAccMag-mean() (dbl),
  tBodyAccMag-std() (dbl), tGravityAccMag-mean() (dbl), tGravityAccMag-std() (dbl), tBodyAccJerkMag-mean() (dbl),
  tBodyAccJerkMag-std() (dbl), tBodyGyroMag-mean() (dbl), tBodyGyroMag-std() (dbl), tBodyGyroJerkMag-mean() (dbl),
  tBodyGyroJerkMag-std() (dbl), fBodyAcc-mean()-X (dbl), fBodyAcc-mean()-Y (dbl), fBodyAcc-mean()-Z (dbl), fBodyAcc-std()-X
  (dbl), fBodyAcc-std()-Y (dbl), fBodyAcc-std()-Z (dbl), fBodyAcc-meanFreq()-X (dbl), fBodyAcc-meanFreq()-Y (dbl),
  fBodyAcc-meanFreq()-Z (dbl), fBodyAccJerk-mean()-X (dbl), fBodyAccJerk-mean()-Y (dbl), fBodyAccJerk-mean()-Z (dbl),
  fBodyAccJerk-std()-X (dbl), fBodyAccJerk-std()-Y (dbl), fBodyAccJerk-std()-Z (dbl), fBodyAccJerk-meanFreq()-X (dbl),
  fBodyAccJerk-meanFreq()-Y (dbl), fBodyAccJerk-meanFreq()-Z (dbl), fBodyGyro-mean()-X (dbl), fBodyGyro-mean()-Y (dbl),
  fBodyGyro-mean()-Z (dbl), fBodyGyro-std()-X (dbl), fBodyGyro-std()-Y (dbl), fBodyGyro-std()-Z (dbl), fBodyGyro-meanFreq()-X
  (dbl), fBodyGyro-meanFreq()-Y (dbl), fBodyGyro-meanFreq()-Z (dbl), fBodyAccMag-mean() (dbl), fBodyAccMag-std() (dbl),
  fBodyAccMag-meanFreq() (dbl), fBodyBodyAccJerkMag-mean() (dbl), fBodyBodyAccJerkMag-std() (dbl),
  fBodyBodyAccJerkMag-meanFreq() (dbl), fBodyBodyGyroMag-mean() (dbl), fBodyBodyGyroMag-std() (dbl),
  fBodyBodyGyroMag-meanFreq() (dbl), fBodyBodyGyroJerkMag-mean() (dbl), fBodyBodyGyroJerkMag-std() (dbl),
  fBodyBodyGyroJerkMag-meanFreq() (dbl), angle(tBodyAccMean,gravity) (dbl), angle(tBodyAccJerkMean),gravityMean) (dbl),
  angle(tBodyGyroMean,gravityMean) (dbl), angle(tBodyGyroJerkMean,gravityMean) (dbl), angle(X,gravityMean) (dbl),
  angle(Y,gravityMean) (dbl), angle(Z,gravityMean) (dbl)
