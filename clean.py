import os
import settings
import pandas as pd
import numpy as np

def int_rate2float(alldata):
    """ 
    Interest rate (int_rate) is supposed to be a numeric variable but 
    right now our DataFrame is reading it as a string. This function 
    strips the "%" and extra spaces from int_rate column and converts
    the remaining value to a float.
    """
    alldata["int_rate"] = alldata["int_rate"].astype("str").str.strip(" %").astype("float")
    alldata["revol_util"] = alldata["revol_util"].astype("str").str.strip(" %").astype("float")
    
def target2binary(alldata):
    """ 
    In logistic regression, the target variable is binary. This function 
    converts target variable loan_status into a binary variable using 
    the following map:
    
    Current, Fully Paid = "in good standing" --> True

    Charged Off, In Grace Period, 
    Late (16-30 days), Late (31-120 days), 
    Default, Charged Off = "not in good standing" --> False
    """
    searchfor = ['Fully Paid', 'Current']
    alldata.loan_status = alldata.loan_status.str.contains('|'.join(searchfor))


def categorical2numeric(alldata):
    """ 
    In order to use scikit learn's logistic regression method, we need
    categorical variables to be numeric. This function converts all our
    categorical variables from strings to numeric categorical codes.
    """
    for column in [
        "term",
        "sub_grade",
        "emp_length",
        "home_ownership",
        "verification_status",
        "purpose",
        "addr_state",
        "initial_list_status",
        "application_type",
        ]: 
        alldata[column] = alldata[column].astype('category').cat.codes


def clean_dates(alldata):
    """ 
    Splits dates into month and year column and deletes the 
    original date column. Function also eliminates loans that
    are less than 1.5 years old (see main.ipynb for complete reasoning)
    """
    def lookup(s):
        """
        This is an extremely fast approach to datetime parsing.
        For large data, the same dates are often repeated. Rather than
        re-parse these, we store all unique dates, parse them, and
        use a lookup to convert all dates.
        """
        dates = {date:pd.to_datetime(date) for date in s.unique()}
        return s.map(dates)
    

    for column in ["issue_d", "earliest_cr_line"]:
        # Convert date columns into datetime objects using the lookup function
        alldata[column] = lookup(alldata[column])
        
        # Create month and year columns for each date column and delete the original date column
        alldata["{}_year".format(column)] = pd.to_numeric(alldata[column].dt.year)
        alldata["{}_month".format(column)] = pd.to_numeric(alldata[column].dt.month)
        del alldata[column]

    # Keep only data that meets the minimum tracking quarters requirement (defined in settings.py)
    today = pd.to_datetime('today')
    curr_quart = (today.month-1)//3 + 1
    curr_year = today.year
    issue_quart = (alldata["issue_d_month"]-1)//3 + 1
    issue_year = alldata["issue_d_year"]
    alldata["tracked_quart"] = (curr_year - issue_year)*4 + (curr_quart - issue_quart) - 1

    alldata = alldata[alldata["tracked_quart"] > settings.MINIMUM_TRACKING_QUARTERS]

    # Finally, fill an NA values with -1
    alldata = alldata.fillna(-1).reset_index(drop=True)

    return alldata

if __name__ == "__main__":
    # Load in the DataFrame
    assembled = pd.read_pickle('processed/assembled.pkl')
    
    # Clean data by passing it through our functions
    int_rate2float(assembled)
    target2binary(assembled)
    categorical2numeric(assembled)
    cleaned = clean_dates(assembled)
    
    # Save cleaned DataFrame
    cleaned.to_pickle('processed/cleaned.pkl')
