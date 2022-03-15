#Click-On Kaduna Datathon
KROCS ANALYTICA

Theme: Data Transformation; From ETL to ELT of
Building Data Pipelines.

Topic: Building Error Workflow Models from ODK to
Data Factory.

<img src=https://github.com/Krocs-Analytica/cok_datathon/blob/remodelling/ELT%20Architechture.PNG> 
ELT (Extract-Load-Transform) ARCHITECHTURE


Data is extracted from a variety of sources and converted to a dataframe using get_data.py 
The extracted data is saved as a csv or excel file using save_data.py
The saved data is loaded and cleaned using data_validator.py
Cleaned data is transformed and made available for reporting using transformer.py, and saved using save_data.py
The notification.py file sends notification at the completion of each milestone
The whole ETL process is triggered and completed by etl_processor.py
