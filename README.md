# CouchDB
ELT(EXTRACT LOAD TRANSFORM) PIPELINE

 

Technologies: Python, Couchdb , MySql , Fast API , Docker  


Project Summary:  

This ELT Pipeline refers to the process of extracting data from source database, loading it into a Data Warehouse environment or destination database, using python and tornado api where asynchronous programming is being used along with Multiprocessing for faster Read/Write operation. The source database used here is CouchDb:V3.2.1 and the destination database is MySQL. The pipeline is dockerized using docker containers and Using this pipeline we can read and extract data from the source database (CouchDb) and load it into the destination database (MySql). The advantage of this pipeline is to transfer the data from source database to destination database in a very short time without any data leakage. 

