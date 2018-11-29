import pytest
import clean_wpdx_sample_data
import pandas
"""Import helper file for STATUS Col cleaning """
import clean_col_status_helper

# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_country_name('NA') == 'NA'

def test_clean_col_install_year():
    """
    Test the cleaning for column: "install_year"
    """
    assert clean_wpdx_sample_data.clean_col_install_year('2001.') == 2001
    

def test_clean_col_fecal_coliform_presence():
    """
    Test the cleaning for column: "fecal_coliform_presence"
    """
    assert pandas.isna(clean_wpdx_sample_data.clean_col_fecal_coliform_presence('junk'))
    assert clean_wpdx_sample_data.clean_col_fecal_coliform_presence('Presence') == 'Presence'
    assert clean_wpdx_sample_data.clean_col_fecal_coliform_presence('Absence') == 'Absence'

def test_clean_col_adm1():
    """
    Test the cleaning for column: "adm1"
    """
    assert clean_wpdx_sample_data.clean_col_adm1('singapore') == 'SINGAPORE'
    assert clean_wpdx_sample_data.clean_col_adm1(' Singapore ') == 'SINGAPORE'


def test_clean_col_status():
    """
    Testing the clean values in column: "status"
    Trello card: https://trello.com/c/S4FjIDgo"
    """
    assert cleaning.clean_col_status('Partly Damaged') == 'Partially Functional with Damages'
    assert cleaning.clean_col_status('absoLUte no daMAge') == 'Functional'
    assert cleaning.clean_col_status('fOUND in BAD state') == 'Not Functional'
    assert cleaning.clean_col_status('ok oPERatIOnal') == 'Functional'
    assert cleaning.clean_col_status("ok") == "Functional"
    assert cleaning.clean_col_status("Not Functional") == "Not Functional"
