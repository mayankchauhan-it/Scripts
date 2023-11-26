from openpyxl import Workbook
import pdfplumber
import re
import pandas as pd
import os
import shutil


def parse_pdf(pdf_file_path):
    text = ''
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Split medicine line into two parts:
def split_line_into_parts(line):
    # Define a regular expression pattern to match integers and decimal numbers
    integer_pattern = r'\d+\.\d+|\d+'

    # Find all matches of integers and decimal numbers in the line
    integers = re.findall(integer_pattern, line)

    # Remove the integers and decimal numbers from the line
    non_integers_part = re.sub(integer_pattern, '', line)

    return integers, non_integers_part.strip()


def replace_separator_lines(text):
    # Define a regular expression pattern to match lines containing only dashes and whitespace
    pattern = r'^[-\s]+$'

    # Use re.sub to replace all matching lines with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.MULTILINE)
    return cleaned_text


def extract_medicine_names(text):
    # Define keywords for medicines
    pattern = r'\b[A-Z][A-Z0-9\s\/\-]*(?:\s?(?:GM|G1|G2|ITRA|ML|TAB|CAP|CREAM|GEL|OINTMENT|DROPS|SOLUTION|POWDER|INJECTION|SPRAY|LOTION|SUPPOSITORY|INHALER|CHEWABLE|LOZENGE|SUSPENSION|ELIXIR|SUSTAINED RELEASE|EXTENDED RELEASE|FORTE|EXTRA|PLUS|JUNIOR|MAX|FORTIFIED|SR|XR|DS|HCL|CR|EC|LA|Rapid Release|MR|IR|XL|HD|LD|DF|PR|HR|BR|ER|F|F\/W|CRM|SHAMPOO|CREAM|PRO|FACE WASH))(?=\s|$)'

    medicine_names = re.findall(pattern, text)
    return medicine_names


def extract_medicine_lines(text):
    # Define a regular expression pattern for medicine names
    pattern = r'\b[A-Z][A-Z0-9\s\/\-]*(?:\s?(?:GM|[*]|CACHER|G1|G2|G2P|BIOKET|ITRA|60K|ITRA|ML|TAB|CAP|CREAM|GEL|OINTMENT|DROPS|SOLUTION|POWDER|INJECTION|SPRAY|LOTION|SUPPOSITORY|INHALER|CHEWABLE|LOZENGE|SUSPENSION|ELIXIR|SUSTAINED RELEASE|EXTENDED RELEASE|FORTE|EXTRA|PLUS|JUNIOR|MAX|FORTIFIED|SR|XR|DS|HCL|CR|EC|LA|Rapid Release|MR|IR|XL|HD|LD|DF|PR|HR|BR|ER|F|F\/W|CRM|SHAMPOO|CREAM|PRO|FACE WASH))(?=\s|$)'

    # Split the text into lines
    lines = text.split('\n')

    # Initialize a list to store lines containing medicine names
    medicine_lines = []

    # Iterate through the lines and check if each line contains a medicine name
    for line in lines:
        if re.search(pattern, line):
            medicine_lines.append(line)

    return medicine_lines


# def copy_file_with_unique_name(source, destination, file_name):
#     try:
#         if os.path.isfile(source):
#             file_name = file_name.replace(" ","_")
#             if not os.path.exists(destination):
#                 os.makedirs(destination)
#             # Generate a unique file name using the counter
#             destination_file = os.path.join(destination, f"{file_name}_{os.path.basename(source)}")
            
#             shutil.copy(source, destination_file)
#             print(f"File '{source}' copied to '{destination_file}' successfully.")
#         else:
#             print(f"Source '{source}' is not a valid file.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


def copy_script_to_directory(destination,file_name):
    try:
        # Get the path of the currently running script
        current_script_path = os.path.abspath(__file__)

        # Extract the script's filename without the full path
        script_filename = os.path.basename(current_script_path)

        # Generate the destination file path
        # Generate a unique file name using the counter
        destination_file = os.path.join(destination, f"{file_name}_{os.path.basename(current_script_path)}")

        # Check if the script file already exists in the destination
        if os.path.exists(destination_file):
            os.remove(destination_file)  # Remove the existing file

        shutil.copy(current_script_path, destination_file)  # Copy the script to the destination
        print(f"Script '{script_filename}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    folder_name = "AMIT PHARMA"
    file_name = "PW"


    pdf_file_path = 'Scrapped_data/JUNE/MP/' + folder_name + '/' + file_name + '.pdf'  # Replace with the actual path to your PDF file
    text = parse_pdf(pdf_file_path)
    medical_name_list = []  # List of medical_name_list
    pattern = r'(?:[A-Z\.]+ (?:MEDICAL|CLINIC|MORBI|MEDICINCE|medical|Medicals|MEDICO|MEDICINS|DRUG|ESSENSE|ENTERPRISE|MEDICINE|SALES|TRUST|MEDICOS|JUNAGADH|ADIPUR|MEDICO\'S|PHRAMACY|CHEMIST|STORE|STORES|MED.STORE|MED.& GEN.STORE|MEDI&GEN|SURGICALS|WELLNESS BEAUTY HUB|HUB|DAVA|PHARMA|GEN|GENERAL|WELLNESS|HOSPITAL|AUSHADHI|VERAVAL|DOCTOR)|JETPUR|JAMJODHPUR|DWARKA|JAMNAGAR|JAM-JODHPUR|DHROL|DR\..*)'
    
    lines = text.split('\n')


    # print(lines)
    
    Stockiest_name = folder_name #same as folder_name
    data = []
    
    # Initialize T_medical_name with None
    T_medical_name = None
    
    counter = 0
    for line in lines:
        # print(line)
        if re.findall(pattern, line):
            counter += 1
            try:
                t_match = line.split(" ")
                # print(t_match)
                # print(len(t_match))
                if len(t_match):
                    T_medical_name = " ".join(t_match[0:])
                    print("Medical Name...:", T_medical_name)
            except:
                pass

        else:
            t_line = line.split(' ')
            print("Line", t_line)
            # print(line)

            print("length", len(t_line), "\n")
            # print("length", len(t_line))
            # if len(t_line) == 6:
            #     T_medicine_name = " ".join(t_line[0:2]).strip()
            #     print(T_medicine_name)
            #     rate = t_line[-1]
            #     ExpQty = t_line[-2]
            #     ReturnQty = "0"
            #     SalesQty = t_line[-3]
            #     FreeStrip = t_line[-4]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])


            if len(t_line) == 7:
                # T_medicine_name = " ".join(t_line[0]).strip()
                T_medicine_name = t_line[0]

                # if '*' in T_medicine_name:  # Check for the asterisk
                #     T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
                
                print(T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
                # print([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName], "\n")


            if len(t_line) == 8:
                T_medicine_name = " ".join(t_line[0:1]).strip()

                if '*' in T_medicine_name:  # Check for the asterisk
                    T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
                
                print("...........",T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
                # print([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName], "\n")

            if len(t_line) == 9:
                T_medicine_name = " ".join(t_line[0:2]).strip()

                if '*' in T_medicine_name:  # Check for the asterisk
                    T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
                
                print("...........",T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
                # print([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName], "\n")

            # if len(t_line) == 10:
            #     T_medicine_name = " ".join(t_line[2:3]).strip()
            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-2]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-3]
            #     FreeStrip = "0"
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"

            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) >= 11:
                T_medicine_name = " ".join(t_line[0:3]).strip()
                print("...........",T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"

                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            # if len(t_line) == 12:
            #     T_medicine_name = " ".join(t_line[2:4]).strip()
            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-2]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-3]
            #     FreeStrip = "0"
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"

            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            # if len(t_line) == 13:
            #     T_medicine_name = " ".join(t_line[2:5]).strip()

            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-2]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-4]
            #     FreeStrip = t_line[-3]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

    df = pd.DataFrame(data, columns=["StockistName", "ChemistName", "ProductName", "FreeSrip", "SELL STRIP", "ReturnQty", "ExpiredQty", "DamageQty", "Rate", "DivisionName"])
    df.to_excel(f"Scrapped_data/JUNE/MP/{folder_name}/{file_name}.xlsx", index=False)


    # # Specify the source file and destination directory
    # source_file = 'C:\\Users\\Mayank\\Desktop\\Python Script\\BIOS_PARTY_WISE.PY'
    # destination_directory = f"Scrapped_data/JUNE/UP/{folder_name}/"  # Use double backslashes for Windows paths


    # # UNCOMMENT THIS LINE ONCE EXCEL IS DONE AND WANTS TO CREATE PYTHON FILE FOR SELECTED PDF FILE...........!
    # copy_file_with_unique_name(source_file, destination_directory, file_name)


    # Specify the destination directory where you want to copy the script
    destination_directory = f"Scrapped_data/JUNE/MP/{folder_name}/"

    copy_script_to_directory(destination_directory,file_name)


if __name__ == "__main__":
    main()
