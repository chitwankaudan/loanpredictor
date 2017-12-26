import os
import settings
import pandas as pd
import numpy as np

# select is a list of all columns relevant to our analysis
SELECT = [
"loan_amnt",
"term",
"int_rate",
"installment",
"sub_grade",
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
"initial_list_status",
"application_type",
"tot_cur_bal",
"tot_hi_cred_lim",
]

# dt is a dictionary that informs the pd.read_csv funciton what datatype each column is
# explicitly stating the datatype is amore efficient way to load in our large datasets
dt = {
"loan_amnt": float,
"term": object,
"int_rate": object,
"installment": float,
"sub_grade": object,
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
"initial_list_status": object,
"application_type": object,
"tot_cur_bal": float,
"tot_hi_cred_lim": float,
}

def concatenate():
      """ Strings all the csv's with training data into one large csv called alltext.csv """
      alldata = []
      files = []
      for item in os.listdir(settings.DATA_DIR):
        if item.endswith(".csv"):
            files.append(item)
      
      # keep the header of the first file
      first = pd.read_csv(os.path.join(settings.DATA_DIR, files[0]), header = 1, 
        usecols = SELECT, dtype = dt, index_col=False, na_values = [''])
      first.drop(first.tail(3).index, inplace = True) #delete comments at the end of the data file

      alldata.append(first)
      
      # drop the header in the rest of the files
      files = files[1:]
      for f in files:
        data = pd.read_csv(os.path.join(settings.DATA_DIR, f), header = 1, 
          usecols = SELECT, dtype = dt, index_col=False, na_values = [''])
        data.drop(0, inplace = True) # drops header

        data.drop(data.tail(3).index, inplace = True) #trim comments out of df
        
        alldata.append(data)
      
      # concatenate all data into one file and resets index
      alldata = pd.concat(alldata, axis=0).reset_index(drop=True)
      
      # Saving the pandas dataframe 
      alldata.to_pickle('processed/assembled.pkl')
      

# runs concatenate only if assemble.py called from the command line
if __name__ == "__main__" :
  concatenate()
  
  
 
