
# coding: utf-8

# In[ ]:


import pytest
import clean_wpdx_sample_data_STATUS as cleaning

# @pytest.mark.skip
def test_clean_col_status():
    
    """
    Testing the clean values in column: "status"
    Trello card: https://trello.com/c/S4FjIDgo"
    """
    
    assert cleaning.clean_col_status('Partly Damaged') == 'Partially Functional with Damages'
    assert cleaning.clean_col_status('absoLUte no daMAge') == 'Functional'
    assert cleaning.clean_col_status('fOUND in BAD state') == 'Not Functional'
    assert cleaning.clean_col_status('ok oPERatIOnal') == 'Functional'


# In[1]:


get_ipython().system('jupyter nbconvert --to script test_clean_wpdx_sample_data_STATUS.ipynb')

