# Data Extraction
Extracting or ingecting data files from multiple sources and load into local repositary

**pre-requesites**
python
pandas
basic SQL
basic streamlit 





**installation and setup**

**pre-installation**
download python : **link :  https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe**

# after installing python, go to the directary where you want to work on the new project

step-1

clone the github repository:
# $ git clone [RepoUrl](https://github.com/yourusername/yourproject.git)

step-2

navigate to the project directory
# $ cd project

step-3

you will find a requirement.txt file in the present directary

# $ pip install -r requirement.txt


**if you complete till here you are done with project setup now lets see how to use the project**

# Let's know the project folder purposes.

Folder PATH listing for volume Windows-SSD
Volume serial number is F0EA-D856
C:.
├───Config_files ==> in this there is a csv file named config. we have to give input information like input path ,file format, name.
├───Credentials ==> we hava to store remote credentials in json format for databases and clouds services.
├───Data_files ==> here we can store the extracted files from different locations.
├───Data_Ingestion  ==> here we have code related to reading, writing, and profiling
│   └───__pycache__
├───Docs  ==> in this we stored the visual screenshots of a ui, to undestand better
│   └───visual_guide
├───main ==> in this there is main function we need to execte this code to open the ui and start the project
├───source_files  ==> in this folder we have to store files to extracted from different format like json,parquet,excel.
└───tests ==> in this, we test the code when adding new features we make it more raw to make it real.









