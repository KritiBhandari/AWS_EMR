AWS Elastic Map Reduce
=======================

Aim:
----
This project finds out the 20 most voted movies with the worst rating (Rating: 1.0) given in the file 'movies.csv'
Uses AWS Elastic Map Reduce 

Steps: 
------
###S3 Bucket Creation
(1) Create an AWS S3 bucket with the following folder: code, input, logs
(2) Upload 'movies.csv' in the 'input' folder 
(3) Upload the 'Mapper_code.py' and 'Reducer_Code.py' in the 'code' folder


###EMR Creation
(1) In the Advanced Settings, select the 'streaming step' and add the required files from the S3 bucket. Manually type the name 'output' to create an output folder in your S3 bucket 
(2) Add the 'Arguments' = '-jobconf mapred.reduce.tasks=1', so that we get only one file as output. For all mappers on one reducer runs and gives a consolidated output from all three machines. 
(3) Machine types: m1.medium, 1 Master, 2 Cores, 0 Task
(4) Select the locations for the logs in the S3 bucket
(5) The steps complete in 1 minute and the output is obtained in the 'Output' folder in the S3 bucker
	