import os
import settings
import datetime
importa pandas as pd

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
  file = os.listdir(settings.DATA_DIR)
  alldata = []
  for f in files:
    data = pd.read_csv(os.path.join(settings.DATA_DIR, f), header = 1, index_col=False)
    data = data[SELECT]
    alldata.append(data)
    
  alldata = pd.concat(all_data, axis=0)
  alldata.to_csv(os.path.join(PROCESSED_DIR, "alldata.text"), sep = ",", header = SELECT, index = False)
  
 
