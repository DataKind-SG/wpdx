import pytest
import clean_wpdx_sample_data as cwsd
import pandas


# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert cwsd.clean_col_country_name('Swaziland') == 'Eswatini'
    assert cwsd.clean_col_country_name('Bolivia, Plurinational State of') == 'Bolivia (Plurinational State of)'
    assert cwsd.clean_col_country_name('Congo, The Democratic Republic of the') == 'Congo (Democratic Republic of the)'


def test_clean_col_country_id():
    """
    Test the cleaning for column: "country_name"
    """
    assert cwsd.clean_col_country_id('ph') == 'PH'
    assert cwsd.clean_col_country_id('P2') == 'None'


def test_clean_col_install_year():
    """
    Test the cleaning for column: "install_year"
    """
    assert cwsd.clean_col_install_year('2001.') == 2001


def test_clean_col_fecal_coliform_presence():
    """
    Test the cleaning for column: "fecal_coliform_presence"
    """
    assert cwsd.clean_col_fecal_coliform_presence('junk') == 'NaN'
    assert cwsd.clean_col_fecal_coliform_presence('Presence') == 'Presence'
    assert cwsd.clean_col_fecal_coliform_presence('Absence') == 'Absence'


def test_clean_col_adm1():
    """
    Test the cleaning for column: "adm1"
    """
    assert cwsd.clean_col_adm1('singapore') == 'SINGAPORE'
    assert cwsd.clean_col_adm1(' Singapore ') == 'SINGAPORE'

    
def test_clean_col_lat_deg():
    """
    Test the cleaning for column: "lat_deg"
    """
    assert cwsd.clean_col_lat_deg(34.123123) == 34.1231

    
def test_clean_col_lon_deg():
    """
    Test the cleaning for column: "lon_deg"
    """
    assert cwsd.clean_col_lon_deg(34.123123) == 34.1231


def test_clean_col_management():
    """
    Test the cleaning for column: "management"
    """
    assert cwsd.clean_col_management('Direct Government Operation?,') == 'Direct Government Operation'
    assert cwsd.clean_col_management('management') == 'Direct Government Operation'

def test_clean_col_status():
    """
    Testing the clean values in column: "status"
    Trello card: https://trello.com/c/S4FjIDgo"
    """
    assert cwsd.clean_col_status('Partly Damaged') == 'Partially Functional with Damages'
    assert cwsd.clean_col_status('absoLUte no daMAge') == 'Functional'
    assert cwsd.clean_col_status('fOUND in BAD state') == 'Not Functional'
    assert cwsd.clean_col_status('ok oPERatIOnal') == 'Functional'
    assert cwsd.clean_col_status("ok") == "Functional"
    assert cwsd.clean_col_status("Not Functional") == "Not Functional"
