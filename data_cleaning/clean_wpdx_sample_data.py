import csv


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

def clean_col_install_year(input_data):
    """
    Clean values in column: "install_year"
    Trello card: https://trello.com/c/KjLEFR24/8-column-installyear
    """
    return input_data


if __name__ == '__main__':
    clean_columns('wpdx_sample_data.csv', 'cleaned_wpdx_sample_data.csv')