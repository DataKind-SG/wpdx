
# coding: utf-8

# In[7]:


import clean_col_status_helper
import csv

def clean_col_status(input_data):
    
    """
    Clean values in column: "status"
    Trello card: https://trello.com/c/S4FjIDgo"
    """
    cleaned_data = input_data
    
    # Preprocessing clean up
    # Remove all NaNs by converting into string text "Not Available"
    cleaned_data = "Not Available" if isinstance(cleaned_data, float) else cleaned_data

    # Convert to lower character
    cleaned_data = cleaned_data.lower()
    
    # Apply UDF from clean_col_status_helper
    cleaned_data = clean_col_status_helper.udf_status(cleaned_data)
    
    return(cleaned_data)


# In[1]:


get_ipython().system('jupyter nbconvert --to script clean_wpdx_sample_data_STATUS.ipynb')

