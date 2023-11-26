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

def find_index_by_date(date_format, my_list):
    for index, item in enumerate(my_list):
        if any(part.isdigit() and len(part) == 2 and part.startswith('0') for part in item.split('/')):
            return index
    return -1 

def find_reverse_index_by_date(date_format, my_list):
    for index in range(len(my_list) - 1, -1, -1):
        item = my_list[-index]
        if any(part.isdigit() and len(part) == 2 and part.startswith('0') for part in item.split('/')):
            return index 
    return -1  

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
    folder_name = "MITTAL MEDICAL AGENCIES,AKOLA"
    file_name = "PW"
    date_format = '26/03/23'

    pdf_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.pdf'  
    text = parse_pdf(pdf_file_path)
    medical_name_list = []  
    pattern = r'(?:[A-Z\.]+ (?:MEDICAL|CLINIC|MEDICINCE|MED|medical|Medicals|MEDICO|MEDICINS|DRUG|ESSENSE|ENTERPRISE|MEDICINE|SALES|TRUST|RAJURA|MEDICOS|JUNAGADH|ADIPUR|MEDICO\'S|PHRAMACY|CHEMIST|STORE|STORES|MED.STORE|MED.& GEN.STORE|MEDI&GEN|SURGICALS|WELLNESS BEAUTY HUB|HUB|DAVA|PHARMA|GEN|GENERAL|WELLNESS|HOSPITAL|AUSHADHI|VERAVAL|MED.|DOCTOR)|JETPUR|JAMJODHPUR|DWARKA|JAMNAGAR|JAM-JODHPUR|DHROL|DR|INDORE|MORBI|DR\..*)'
    
    lines = text.split('\n')


    # print(lines)
    
    Stockiest_name = folder_name 
    data = []
    
    T_medical_name = None
    
    counter = 0
    for line in lines:
        # print(line)
        if re.findall(pattern, line):

            # print(line)
            counter += 1

            try:
                t_match = line.split(", ")
                # print(t_match)
                # print(len(t_match))

                if t_match[0] == "PARTY / ITEM WISE SALES SUMMARY FROM 01/06/2023" or  "TAB" in t_match or t_match[0] == "B.M.A. ENTERPRISE":
                    continue

                if len(t_match) == 2 or len(t_match) == 3:
                    # print(len(t_match))
                    T_medical_name = " ".join(t_match[0].split(' ')[2:])
                    print("Medical Name...:", T_medical_name, "\n")
                elif len(t_match) > 10:
                    # print(len(t_match))
                    T_medical_name = " ".join(t_match[-2:])
                    print("Medical Name...:", T_medical_name, "\n")
                elif len(t_match) == 5:
                    # print(len(t_match))
                    T_medical_name = " ".join(t_match[0:])
                    print("Medical Name...:", T_medical_name, "\n")
            except:
                pass

        else:
            t_line = line.split(' ')
            # print("Line", t_line)
            # print(line)

            # print("length", len(t_line), "\n")
            # print("length", len(t_line))
            # if len(t_line) == 6:
            #     T_medicine_name = t_line[0]


            #     if T_medicine_name == "PARTY / ITEM WISE SALES SUMMARY FROM 01/06/2023" or T_medicine_name == "RAJVEER PHARMA" or T_medicine_name == "Phone" or T_medicine_name == "GRAND":
            #         continue

            #     print(T_medicine_name)
            #     rate = t_line[-2]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-4]
            #     FreeStrip = t_line[-3]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])


            # if len(t_line) == 7:
            #     T_medicine_name = " ".join(t_line[0:2]).strip()
            #     # T_medicine_name = t_line[0]

            #     if '*' in T_medicine_name:  # Check for the asterisk
            #         T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
                
            #     print(T_medicine_name, "\n")
            #     rate = t_line[-2]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-4]
            #     FreeStrip = t_line[-3]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
            #     # print([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName], "\n")


            # if len(t_line) == 8:
            #     T_medicine_name = " ".join(t_line[0:2]).strip()

            #     if 'SHOP' in T_medicine_name:  # Check for the asterisk
            #         # T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
            #         continue
                
            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-3]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-5]
            #     FreeStrip = t_line[-4]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
            #     # print([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName], "\n")

            # if len(t_line) == 9:
            #     T_medicine_name = " ".join(t_line[0:2]).strip()

            #     if '*' in T_medicine_name:  # Check for the asterisk
            #         T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
            #         # continue
                
            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-3]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-5]
            #     FreeStrip = t_line[-4]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
            #     # print([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName], "\n")

            # if len(t_line) == 10:
            #     T_medicine_name = " ".join(t_line[0:3]).strip()
            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-3]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-5]
            #     FreeStrip = t_line[-4]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"

            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 11:
                T_medicine_name = " ".join(t_line[1:2]).strip()
                # print("...........",T_medicine_name, "\n")

                rate = t_line[-3]
                SalesQty = t_line[-4]
                ExpQty = "0"
                ReturnQty = "0"
                FreeStrip = "0"
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"


                # print("Line : ",t_line)
                # print("Medicine Name : ",T_medicine_name)
                # print("SalesQty : ",SalesQty)
                # print("FreeStrip : ",FreeStrip)
                # print("rate : ",rate)
                # print(len(t_line) , "\n")
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 12:
                T_medicine_name = " ".join(t_line[1:3]).strip()

                if t_line[1] == "Sales":
                    continue
                elif t_line[1] == "Customer-Wise":
                    continue
                elif t_line[1] == "Product-Wise":
                    continue
                elif t_line[1] == "Name":
                    continue

                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"

                date_index = find_reverse_index_by_date(date_format, t_line)

                # print(f"Index in reverse: {-date_index}")

                if date_index == 6:
                    SalesQty = t_line[-4]
                    FreeStrip = " "

                else:
                    SalesQty = t_line[-5]
                    FreeStrip = t_line[-4]

                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                # print("Line : ",t_line)
                # print("Medicine Name : ",T_medicine_name)
                # print("SalesQty : ",SalesQty)
                # print("FreeStrip : ",FreeStrip)
                # print("rate : ",rate)
                # print(len(t_line) , "\n")
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 13:
                T_medicine_name = " ".join(t_line[1:3]).strip()

                if t_line[1] == "Sales":
                    continue
                elif t_line[1] == "Customer-Wise":
                    continue
                elif t_line[1] == "Product-Wise":
                    continue
                elif t_line[1] == "Name":
                    continue

                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"

                date_index = find_reverse_index_by_date(date_format, t_line)

                # print(f"Index in reverse: {-date_index}")

                if date_index == 6:
                    SalesQty = t_line[-4]
                    FreeStrip = " "

                else:
                    SalesQty = t_line[-5]
                    FreeStrip = t_line[-4]

                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                # print("Line : ",t_line)
                # print("Medicine Name : ",T_medicine_name)

                # print("SalesQty : ",SalesQty)
                # print("FreeStrip : ",FreeStrip)
                # print("rate : ",rate)
                # print(len(t_line) , "\n")
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
            
            if len(t_line) == 14:
                T_medicine_name = " ".join(t_line[1:3]).strip()
                if t_line[1] == "Sales":
                    continue
                elif t_line[1] == "Customer-Wise":
                    continue
                elif t_line[1] == "Product-Wise":
                    continue
                elif t_line[1] == "Name":
                    continue

                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"

                date_index = find_reverse_index_by_date(date_format, t_line)

                # print(f"Index in reverse: {-date_index}")

                if date_index == 6:
                    SalesQty = t_line[-4]
                    FreeStrip = " "

                else:
                    SalesQty = t_line[-5]
                    FreeStrip = t_line[-4]

                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                # print("Line : ",t_line)
                # print("Medicine Name : ",T_medicine_name)

                # print("SalesQty : ",SalesQty)
                # print("FreeStrip : ",FreeStrip)
                # print("rate : ",rate)
                # print(len(t_line) , "\n")
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
            

    df = pd.DataFrame(data, columns=["StockistName", "ChemistName", "ProductName", "FreeSrip", "SELL STRIP", "ReturnQty", "ExpiredQty", "DamageQty", "Rate", "DivisionName"])
    df.to_excel(f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/{file_name}.xlsx", index=False)


    # # Specify the source file and destination directory
    # source_file = 'C:\\Users\\Mayank\\Desktop\\Python Script\\BIOS_PARTY_WISE.PY'
    # destination_directory = f"Scrapped_data/JUNE/UP/{folder_name}/"  # Use double backslashes for Windows paths


    # # UNCOMMENT THIS LINE ONCE EXCEL IS DONE AND WANTS TO CREATE PYTHON FILE FOR SELECTED PDF FILE...........!
    # copy_file_with_unique_name(source_file, destination_directory, file_name)


    # Specify the destination directory where you want to copy the script
    destination_directory = f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/"

    copy_script_to_directory(destination_directory,file_name)


if __name__ == "__main__":
    main()
