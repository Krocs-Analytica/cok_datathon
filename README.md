# Click-On Kaduna Datathon

## KROCS ANALYTICA

### Theme: Data Transformation; From ETL to ELT of Building Data Pipelines.

### Topic: Building Error Workflow Models from ODK to Data Factory.

<img src=https://github.com/Krocs-Analytica/cok_datathon/blob/remodelling/ELT%20Architechture.PNG> 
		
#### ELT (Extract-Load-Transform) ARCHITECHTURE


This solution allows Data to be extracted from a variety of sources and converted to a dataframe using get_data.py.
The ingested data is saved as a csv or excel file using save_data.py.
The saved data is loaded and cleaned using data_validator.py.
The cleaned data is transformed and made available for reporting using transformer.py.
The notification.py file sends notification at the completion of each milestone.
The whole ELT process is triggered and completed by etl_processor.py.

### How to run the code
- Open your terminal or command prompt at any directory of your choice on your local machine and run the command one after the other in the order below.
 
  ```
  mkdir cok_dir
  cd cok_dir
  git clone https://github.com/Krocs-Analytica/cok_datathon.git
  cd cok_datathon
  python elt_processor.py
  
  ```
  
  ### Dependencies
  This code is dependent on the following.
  - Python 3.8+
  - Pandas
  - Numpy


