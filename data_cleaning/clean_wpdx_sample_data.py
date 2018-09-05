import csv
import pandas as pd
import numpy as np
from textblob import TextBlob

in_file_path = '/home/kevan/Desktop/wpdx/water_point_data_exchange_complete_dataset.csv'
out_file_path = '/home/kevan/Desktop/wpdx/cleaned_water_point_data_exchange_complete_dataset.csv'


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
    df = pd.read_csv(in_file_path)
    df_temp = df
    df_temp_30 = df_temp.sample(frac=0.3)
    cleaned_df = df_temp_30.head().apply(
        lambda row: TextBlob(row).correct().__str__())
    return cleaned_df


if __name__ == '__main__':
    clean_columns(in_file_path, out_file_path)
