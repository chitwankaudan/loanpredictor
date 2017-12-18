import os
import settings
import datetime
import pandas as pd
import numpy as np

# lists all revelant columns
SELECT = [
"loan_amnt",
"term",
"int_rate",
"installment",
"grade",
"sub_grade",
"emp_title",
"emp_length",
"home_ownership",
"annual_inc",
"verification_status",
"issue_d",
"loan_status",
"purpose",
"addr_state",
"dti",
"earliest_cr_line",
"open_acc",
"pub_rec",
"revol_util",
"total_acc",
"initial_list_status",
"application_type"
]

dt = {
"loan_amnt": float,
"term": object,
"int_rate": object,
"installment": float,
"grade": object,
"sub_grade": object,
"emp_title": object,
"emp_length": object,
"home_ownership": object,
"annual_inc": float,
"verification_status": object,
"issue_d": object,
"loan_status": object,
"purpose": object,
"addr_state": object,
"dti": float,
"earliest_cr_line": object,
"open_acc": float,
"pub_rec": float,
"revol_util": object,
"total_acc": float,
"initial_list_status": object,
"application_type": object
}


def concatenate():
  alldata = []
  files = []
  for item in os.listdir(settings.DATA_DIR):
    if item.endswith(".csv"):
        files.append(item)
  
  # keeps the header of the first file
  first = pd.read_csv(os.path.join(settings.DATA_DIR, files[0]), header = 1, 
    usecols = SELECT, dtype = dt, index_col=False, na_values = [''])
  first.drop(first.tail(3).index, inplace = True) #delete comments at the end of the data file

  alldata.append(first)
  
  # drops the header in the rest of the files
  files = files[1:]
  for f in files:
    data = pd.read_csv(os.path.join(settings.DATA_DIR, f), header = 1, 
      usecols = SELECT, dtype = dt, index_col=False, na_values = [''])
    data.drop(0, inplace = True) # drops header

    data.drop(data.tail(3).index, inplace = True) #trim comments out of df
    
    alldata.append(data)
  
  # concatenates all data into one file
  alldata = pd.concat(alldata, axis=0) # merges all dataframes
  # alldata[id] = range(1, (alldata.shape[0]-5)  # adds a unique id
  alldata.to_csv(os.path.join(settings.PROCESSED_DIR, "alldata.csv"), sep = ",", header = SELECT, index = False)  #write data to alldata.txt         
    
# runs concatenate only if assemble.py called from the command line
if __name__ == "__main__" :
  concatenate()
  
  
 
