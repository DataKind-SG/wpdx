import csv
import pandas as pd
import sys


def clean_columns(input_file, output_file):
    with open(input_file) as csvfile, open(output_file, 'wt') as writer:
        reader = csv.DictReader(csvfile)
        column_names = reader.fieldnames
        writer.write(','.join(column_names) + '\n')

        n_cols = len(column_names)
        column_methods = [globals()['clean_col_' + str(i)] for i in range(n_cols)]

        for row in reader:
            cleaned_row = list()
            for i in range(n_cols):
                cleaned_row.append(column_methods[i](row[column_names[i]]))
            writer.write(','.join(cleaned_row) + '\n')


def clean_col_country_name(input_data):
    """
    Clean values in column: "country_name"
    Trello card: https://trello.com/c/HHzNs0hS/1-column-countryname
    """
    return input_data


def clean_col_management(in_file_path, out_file_path):
    """
    Clean values in column: "management"
    The code below cleans a particular value "Direct Government Operation" in the management column
    Trello card: https://trello.com/c/DYWGoDG5/5-column-management
    """

    data = pd.read_csv(in_file_path)
    data.loc[data['management'] == 'Direct Government Operation?,', 'management'] = 'Direct Government Operation'
    data.to_csv(out_file_path, index=False)
    return data

if __name__ == '__main__':
    ## Writing this so as to give a provision of providing file names at the command line.  
    ## Ex -> python clean_wpdx_sample_data.py water_point_dataset.csv cleaned_water_point_dataset.csv
    if len(sys.argv) == 3:
        in_file_path = sys.argv[1] #Input file name
        out_file_path = sys.argv[2] #Output file name
        clean_columns(in_file_path, out_file_path)
    else:
        clean_columns('wpdx_sample_data.csv', 'cleaned_wpdx_sample_data.csv')