import pytest
import clean_wpdx_sample_data

# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_country_name('NA') == 'NA'

def test_clean_col_install_year():
    """
    Test the cleaning for column: "install_year"
    s"""
    assert clean_wpdx_sample_data.clean_col_install_year('2012') == 2012
    assert clean_wpdx_sample_data.clean_col_install_year(2012.32) == 2012
    assert clean_wpdx_sample_data.clean_col_install_year('2020') == 2020
    