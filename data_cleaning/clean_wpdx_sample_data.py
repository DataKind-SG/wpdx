import csv
import pandas


def clean_columns(input_file, output_file):
    with open(input_file) as csvfile, open(output_file, 'wt') as writer:
        reader = csv.DictReader(csvfile)
        column_names = reader.fieldnames
        writer.write(','.join(column_names) + '\n')

        n_cols = len(column_names)

        custmethods = []
        [(k.startswith('clean_col_') and custmethods.append(k)) 
            for k in globals().keys()]
        dirty_col_list = [m.replace('clean_col_', '') for m in custmethods]

        for row in reader:
            cleaned_row = list()
            for i in range(n_cols):
                col_name = column_names[i]
                col_value = row[column_names[i]]

                if col_name in dirty_col_list:
                    col_value = globals()['clean_col_' + col_name](col_value)

                if "," in str(col_value):
                    col_value = '"' + str(col_value) + '"'

                cleaned_row.append(str(col_value))

            writer.write(','.join(cleaned_row) + '\n')


def clean_col_country_name(input_data):
    """
    Clean values in column: "country_name"
    Trello card: https://trello.com/c/HHzNs0hS/1-column-countryname
    """
    replacements = {
        'Swaziland': 'Eswatini', # country got renamed
        'Bolivia, Plurinational State of': 'Bolivia (Plurinational State of)',
        'Congo, The Democratic Republic of the': 'Congo (Democratic Republic of the)'
    }

    if input_data in replacements.keys():
        return replacements[input_data]

    return input_data


def clean_col_country_id(input_data):
    if input_data.isalpha():
        if len(input_data) == 2:
            input_data = input_data.upper()
            output = input_data
        else:
            output = 'None'
    else:
        output = 'None'

    return output


def clean_col_install_year(input_data):
    """
    Clean values in column: "install_year"
    Trello card: https://trello.com/c/KjLEFR24/8-column-installyear
    We need to produce a 4 digit integer. If year is string, casting it as
    integer still works.
    """
    if type(input_data) == str:
        input_data_length = min(4, len(input_data))
        if str.isdigit(input_data[:input_data_length]):
            integer_input_data = int(input_data[:input_data_length])
            output = integer_input_data
        else:
            output = 'None'
    else:
        integer_input_data = int(input_data)
        output = integer_input_data
    return output


def clean_col_fecal_coliform_presence(input_data):
    """
    Clean values in column: "fecal_coliform_presence"
    Trello card: https://trello.com/c/NCCXe8zG/13-column-fecalcoliformpresence
    Categorical value with levels ["Absence", "Presence"]
    """
    output = input_data

    if input_data not in ["Absence", "Presence"]:
        output = "NaN"

    return output


def clean_col_adm1(input_data):
    """
    Clean values in column: "adm1"
    Trello card: https://trello.com/c/HHzNs0hS/1-column-adm1
    """
    input_data = input_data.upper()
    input_data = input_data.strip()
    return input_data


def clean_col_lat_deg(input_data):
    """
    Clean values in column: "lat_deg"
    Trello card: https://trello.com/c/51qHGAyc/25-column-latdeg-londeg
    """
    output = input_data
    if(isinstance(output, int) or isinstance(output, float)):
        output=round(input_data,4)
    elif(isinstance(output, str)):
        output=round(float(input_data),4)
    return output


def clean_col_lon_deg(input_data):
    """
    Clean values in column: "lon_deg"
    Trello card: https://trello.com/c/51qHGAyc/25-column-latdeg-londeg
    """
    output = input_data
    if(isinstance(output, int) or isinstance(output, float)):
        output=round(input_data,4)
    elif(isinstance(output, str)):
        output=round(float(input_data),4)
    return output


def clean_col_management(input_data):
    """
    Clean values in column: "management"
    The code below cleans a particular value "Direct Government Operation" in the management column
    Trello card: https://trello.com/c/DYWGoDG5/5-column-management
    """

    if input_data in ['Direct Government Operation?,', 'management']:
        input_data = 'Direct Government Operation'
    return input_data


if __name__ == '__main__':
    clean_columns('wpdx_sample_data.csv', 'cleaned_wpdx_sample_data.csv')
