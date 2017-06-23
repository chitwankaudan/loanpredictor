import os
import settings
import datetime
import pandas as pd

# lists all revelant columns
SELECT = [
"id",
"loan_amnt",
"funded_amnt",
"funded_amnt_inv",
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

def concatenate():
  files = os.listdir(settings.DATA_DIR)
  alldata = []
  
  # keeps the header of the first file
  first = pd.read_csv(os.path.join(settings.DARA_DIR, files[0]), header = 1, index_col=False)
  first = first[SELECTED]
  alldata.append(first)
  
  # drops the header in the rest of the files
  files = files[1:]
  for f in files:
    data = pd.read_csv(os.path.join(settings.DATA_DIR, f), header = 1, index_col=False)
    data = data[SELECT] # trims dataframe to only included "selected" columns
    data.drop(0, inplace = True)  # drops header
    alldata.append(data)
  
  # concatenates all data into one file
  alldata = pd.concat(all_data, axis=0) # merges all dataframes
  alldata[id] = range(1, alldata.shape[0])  # adds a unique id
  alldata.to_csv(os.path.join(PROCESSED_DIR, "alldata.text"), sep = ",", header = SELECT, index = False)  #write data to alldata.txt
             
    
# runs concatenate only if assemble.py called from the command line
if _name_ == "_main_" :
  concatenate()
  
  
 
