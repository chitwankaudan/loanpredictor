import os
import settings
import datetime
import pandas as pd
import numpy as np

# lists all revelant columns
SELECT = [
"id",
"loan_amnt",
"term",
"int_rate",
"installment",
"grade",
"sub_grade",
"emp_length",
"home_ownership",
"annual_inc",
"verification_status",
"issue_d",
"purpose",
"addr_state",
"dti",
"earliest_cr_line",
"open_acc",
"pub_rec",
"total_acc",
"initial_list_status",
"application_type"
]

type_dict = {
"id": "object",
"loan_amnt": "object",
"term": "object",
"int_rate": "object",
"installment": "float64",
"grade": "object",
"sub_grade": "object",
"emp_title": "object",
"emp_length": "object",
"home_ownership": "object",
"annual_inc": "float64",
"verification_status": "object",
"issue_d": "object",
"purpose": "object",
"addr_state": "object",
"dti": "float64",
"earliest_cr_line": "object",
"open_acc": "float64",
"pub_rec": "float64",
"total_acc": "float64",
"initial_list_status": "object",
"application_type": "object"
}


def concatenate():
  files = os.listdir(settings.DATA_DIR)
  alldata = []
  
  # keeps the header of the first file
  first = pd.read_csv(os.path.join(settings.DATA_DIR, files[0]), header = 1, index_col=False, dtype = type_dict, na_values = [""])
  first = first[SELECT]
  alldata.append(first)
  
  # drops the header in the rest of the files
  files = files[1:]
  for f in files:
    data = pd.read_csv(os.path.join(settings.DATA_DIR, f), header = 1, index_col=False)
    data = data[SELECT] # trims dataframe to only included "selected" columns
    data.drop(0, inplace = True)  # drops header
    alldata.append(data)
  
  # concatenates all data into one file
  alldata = pd.concat(alldata, axis=0) # merges all dataframes
  # alldata[id] = range(1, (alldata.shape[0]-5)  # adds a unique id
  alldata.to_csv(os.path.join(settings.PROCESSED_DIR, "alldata.txt"), sep = ",", header = SELECT, index = False)  #write data to alldata.txt
             
    
# runs concatenate only if assemble.py called from the command line
if __name__ == "__main__" :
  concatenate()
  
  
 
