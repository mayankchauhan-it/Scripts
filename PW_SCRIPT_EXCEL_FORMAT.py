from e_functions import *
import re
import pandas as pd

def read_excel_rows(file_path, sheet_name='Sheet1'):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        data = []
        # Initialize variables before the loop
        # medical_name = " "
        # medicine_name = " "
        # Print all rows
        for index, row in df.iterrows():
            print(f"Row {index + 1}:")
            # print(row)

            product_column = row['PAVAN MEDICO']
            column1 = row['Unnamed: 1']
            column2 = row['Unnamed: 2']
            column3 = row['Unnamed: 3']
            column4 = row['Unnamed: 4']
            
            medical_name = " "
            medicine_name = " "

            # Positive condition: All columns from 1 to 4 are NaN
            if all(pd.isna(x) for x in [column1, column2, column3, column4]):
                if ":" in product_column  or "Sales" in product_column or "Report" in product_column or "*" in product_column:
                    continue
                medical_name = product_column

            # Negative condition: Any column from 1 to 4 is not NaN
            if any(not pd.isna(x) for x in [column1, column2, column3, column4]) and product_column != medical_name:
                if product_column == "GRAND TOTAL" or product_column == "Product Name" :
                    continue

                if product_column == medical_name:
                    continue

                medicine_name = product_column


            data.append([medical_name, medicine_name])
            print(medical_name)
            print(medicine_name)
            # print(column1)
            # print(column2)
            # print(column3)
            # print(column4)

            print()
        # print(data)

    except Exception as e:
        print(f"Error reading Excel file: {e}")

def main():
    folder_name = "PAVAN MEDICO"
    file_name = "PW"
    Stockiest_name = folder_name
    excel_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.xlsx'

    # data = parse_excel(excel_file_path, sheet_name='Sheet1')
    data = read_excel_rows(excel_file_path, sheet_name='Sheet1')

    # print("data", type(data))

    # print(data)

    if data is not None:
        # Iterate over rows and print all values
        print("All Values:")
        for index, row in data.iterrows():
            print(f"\nRow {index + 1}:")
            # print(f"\nRow {row}:")
            # for column_name, value in row.items():
                # print(column_name)
                # print(value)
                


if __name__ == "__main__":  
    main()