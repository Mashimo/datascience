  ## Goal: prepare tidy data that can be used for later analysis about wearables.
  #
  # Steps: 
  # 1. Merges the training and the test sets to create one data set.
  # 2. Extracts only the measurements on the mean and standard deviation for each measurement. 
  # 3. Uses descriptive activity names to name the activities in the data set
  # 4. Appropriately labels the data set with descriptive variable names. 
  # 5. From the data set in step 4, *creates a second, independent tidy data set 
  #    with the average of each variable for each activity and each subject.*
  #
  ## Submit:
  # tidy data set created in step 5 as txt file 
  
  library (dplyr)
  
    # 0. Read all the files into appropriate data frames
  
    ## set the working directory (assume the folder with the data sets is in the same directory as this script)
  setwd("./UCI HAR Dataset")
  
    ## check if file exists (ignore the inertial folders)
  if (!file.exists("activity_labels.txt") | !file.exists("features.txt")) {
    stop("invalid directory")
  }
  
    ## read files and load datasets
  act  <- read.table("activity_labels.txt")
      ### act has 6 obs. of 2 variables (1...6 as code and its label)
  features  <- read.table("features.txt", col.names=c("ID","name"))
      ### features has 561 obs. of 2 variables (1...n and its label)
  
  setwd("./test")
  testSub <- read.table("subject_test.txt")
     ### Sub has 2947 obs. of 1 variable (=int 1...30)
  testX <- read.table("X_test.txt")
     ### testX has 2947 obs. of 561 variables (see features above)
  testY <- read.table("y_test.txt")
     ### testY has 2947 obs. of 1 variable (the activity label)
  
  setwd("../train")
  trainSub <- read.table("subject_train.txt")
     ### trainSub has 7352 obs of 1 variable
  trainX <- read.table("X_train.txt")
     ### trainX has 7352 obs. of 561 variables
  trainY <- read.table("y_train.txt")
     ### trainY has 7352 obs. of 1 variable
  
  # 1. Merge the training and the test sets to create one data set.
  allX <- merge(testX, trainX, all=TRUE)
  allSub <- merge(testSub, trainSub, all=TRUE)
  allY <- rbind(testY, trainY) # alternative merge using rbind()
  
  # 2. Uses descriptive activity names to name the activities in the data set
   ## first extract the column names from file features.txt
  #featuresNames <- as.vector(features[["name"]])
   ## then change the column names of the X data set
  colnames(allX) <- as.vector(features[["name"]])
  # now keep only columns where the name has mean or std inside (use regex)

  # 3. Extracts only the measurements on the mean and standard deviation for each measurement. 
  allX <- allX[, grepl("mean|Mean|std", names(allX))]
  
  # 4. Appropriately labels the data set with descriptive variable names. 
   ## features have already correct name
  
   ## change variable name of unique column of data frame allSub into "Subject"
  colnames(allSub) <- c("Subject")
   ## and add it the main data frame
  allX <- cbind(allX, allSub)
   ## same for allY: add it to main data frame as extra column but first map activity label to activity code
  Activity <- act$V2[match(allY$V1, act$V1)]
  allX <- cbind(allX, Activity)
  
  # 5. From the data set in step 4, *creates a second, independent tidy data set 
  #    with the average of each variable for each activity and each subject.*
   ## 30 subjects * 6 activities = 180 observations (lines)
   ## Subject + Activity + 86 features = 88 variables (columns) 
  
   ## group by Subject and Activity; then calculate the mean for each group resulted. new data set = tidy 
  tidy <- allX %>% group_by(Subject, Activity) %>% summarise_each(funs(mean))
  
  # 6. Last, create the final tidy data set to be uploaded
  setwd("../..")
  fileName = "tiny_data.txt"
  write.table(tidy, fileName, row.name=FALSE)