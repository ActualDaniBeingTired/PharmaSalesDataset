This project was made by Daniel Satrio Pamungkas as a Personal Project to learn more about how to use PostGreSQL, PowerBI, Docker, and Airflow. 
The dataset was taken from Kaggle from this link : https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data? made by Milan Zdravković. 

With a total of 2106 data from 2014-2019. It include sales of various Drug type such as : 
- M01AB     : Anti-inflammatory and antirheumatic products, non-steroids, Acetic acid derivatives and related substances
- M01AE     : Anti-inflammatory and antirheumatic products, non-steroids, Propionic acid derivatives
- N02BA     : Other analgesics and antipyretics, Salicylic acid and derivatives
- N02BE/B   : Other analgesics and antipyretics, Pyrazolones and Anilides
- N05B      : Psycholeptics drugs, Anxiolytic drugs
- N05C      : Psycholeptics drugs, Hypnotics and sedatives drugs
- R03       : Drugs for obstructive airway diseases
- R06       : Antihistamines for systemic use

Inside the src file, there's 6 Python files. Those are : 
1. DataExploration.py   : Functions as the first step towards knowing what's the data about. In here we check the data types, shapes, and the quality of the data to ensure is it safe enough to process or not. 
2. Extract.py           : grabs the data from Airflow Environtment and check the number of rows and columns.
3. Transform.py         : Transform the data that we just extracted from Extract.py. Transformation includes changing the datatype of "datum", identifying the drug columns, melting the data columns so it will be easier for analytical use, renamings of certain columns, removing duplications and sorting the data.
4. Validate.py          : Rechecks the data via validation as an extra measure to check that the transformation is correct.
5. Load.py              : Loads the data into the database that's located in PostGreSQL. Using queries to build the staging table, then proceed to create the fact and dimension tables.
6. ETL.py               : Functions as a merger for Extract.py, Load.py, Validate.py, and Transform.py. This is used for automation that's executed by Airflow. 

In the Airflow, there's 1 Python file called PharmaSalesETL.py. 
It's used to set how the DAG works. It's set to run on 1st of January 2026, will run daily, and only run once. It tells the ETL.py and calls the run_pipeline function that will trigger the ETL.

Inside the Docker directory, there's 1 yml file called Docker-compose. It's a list of configuration to containerized the whole file.

After that, I used the file and used it to learn how to visualize the Dashboard using Power BI.

There's also a bunch of SQL's query to play around with the data. 

