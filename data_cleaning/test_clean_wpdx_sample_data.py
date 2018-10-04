import pytest
import clean_wpdx_sample_data

# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_country_name('NA') == 'NA'

def test_clean_col_pay():
    """
    Test the cleaning for column: "pay"
    """
    assert clean_wpdx_sample_data.clean_col_pay('NA') == 'UNKNOWN'
    assert clean_wpdx_sample_data.clean_col_pay('') == 'UNKNOWN'
    assert clean_wpdx_sample_data.clean_col_pay('            ') == 'UNKNOWN'
    assert clean_wpdx_sample_data.clean_col_pay('yes') == 'YES'
    # assert clean_wpdx_sample_data.clean_col_pay('no, water is free') == 'NO'
    # assert clean_wpdx_sample_data.clean_col_pay('Is paid by someone else') == 'NO'
    # assert clean_wpdx_sample_data.clean_col_pay('$6.00  per jar') == '??'

