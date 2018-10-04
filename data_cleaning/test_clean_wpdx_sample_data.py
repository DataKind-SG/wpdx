import pytest
import clean_wpdx_sample_data

# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_country_name('NA') == 'NA'
    
    
def test_clean_col_count():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_count('hello') == None
    

