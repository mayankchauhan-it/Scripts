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


def copy_script_to_directory(destination,file_name):
    try:
        # Get the path of the currently running script
        current_script_path = os.path.abspath(__file__)

        # Extract the script's filename without the full path
        script_filename = os.path.basename(current_script_path)

        # Generate the destination file path
        # Generate a unique file name using the counter
        destination_file = os.path.join(destination, f"{file_name}_1_{os.path.basename(current_script_path)}")

        # Check if the script file already exists in the destination
        if os.path.exists(destination_file):
            os.remove(destination_file)  # Remove the existing file

        shutil.copy(current_script_path, destination_file)  # Copy the script to the destination
        print(f"Script '{script_filename}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    folder_name = "RAJVEER PHARMA"
    file_name = "RAJVEER DERMA PARTYWISE JUNE23"


    pdf_file_path = 'Scrapped_data/JUNE/GUJARAT/' + folder_name + '/' + file_name + '.pdf'  # Replace with the actual path to your PDF file
    text = parse_pdf(pdf_file_path)
    pattern = r'(?:[A-Z\.]+ (?:MEDICAL|CLINIC|MEDICINCE|medical|Medicals|MEDICO|MEDICINS|DRUG|ESSENSE|ENTERPRISE|MEDICINE|SALES|TRUST|MEDICOS|JUNAGADH|ADIPUR|MEDICO\'S|PHRAMACY|CHEMIST|STORE|STORES|MED.STORE|MED.& GEN.STORE|MEDI&GEN|SURGICALS|WELLNESS BEAUTY HUB|HUB|DAVA|PHARMA|GEN|GENERAL|WELLNESS|HOSPITAL|AUSHADHI|VERAVAL|MED.|DOCTOR)|JETPUR|JAMJODHPUR|DWARKA|JAMNAGAR|JAM-JODHPUR|DHROL|DR|INDORE|MORBI|DR\..*)'
    
    lines = text.split('\n')

    data = []
    

    Stockiest_name = folder_name
    # Initialize T_medical_name with None
    T_medical_name = None
    
    counter = 0
    for line in lines:
        if re.findall(pattern, line):

            counter += 1
            try:
                t_match = line.split("-")

                if t_match[0] == "PARTY / ITEM WISE SALES SUMMARY FROM 01/06/2023" or t_match[0] == "RAJVEER PHARMA" or t_match[0] == "Company : BIOS DERMA(VISHWA),BIOS PHARMA":
                    continue

                if len(t_match) < 3:
                    T_medical_name = t_match[0]
                    print("Medical Name...:", T_medical_name, "\n")
                elif len(t_match) > 10:
                    T_medical_name = " ".join(t_match[-2:])
                    print("Medical Name...:", T_medical_name, "\n")
                elif len(t_match) < 5:
                    T_medical_name = " ".join(t_match[0:])
                    print("Medical Name...:", T_medical_name, "\n")

            except:
                pass

        else:
            t_line = line.split(' ')
            print("Line", t_line)

            print("length", len(t_line), "\n")

            if len(t_line) == 6:
                T_medicine_name = t_line[0]


                if T_medicine_name == "PARTY / ITEM WISE SALES SUMMARY FROM 01/06/2023" or T_medicine_name == "RAJVEER PHARMA" or T_medicine_name == "Phone" or T_medicine_name == "GRAND":
                    continue

                print(T_medicine_name)
                rate = t_line[-2]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-4]
                FreeStrip = t_line[-3]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])


            if len(t_line) == 7:
                T_medicine_name = " ".join(t_line[0:2]).strip()

                if '*' in T_medicine_name:  # Check for the asterisk
                    T_medicine_name = T_medicine_name[:-4]  # Remove the last 4 characters
                
                print(T_medicine_name, "\n")
                rate = t_line[-2]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-4]
                FreeStrip = t_line[-3]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])


            if len(t_line) == 8:
                T_medicine_name = " ".join(t_line[0:3]).strip()

                if 'SHOP' in T_medicine_name:  # Check for the asterisk
                    continue
                
                print("...........",T_medicine_name, "\n")
                rate = t_line[-2]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-4]
                FreeStrip = t_line[-3]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

    df = pd.DataFrame(data, columns=["StockistName", "ChemistName", "ProductName", "FreeSrip", "SELL STRIP", "ReturnQty", "ExpiredQty", "DamageQty", "Rate", "DivisionName"])
    df.to_excel(f"Scrapped_data/JUNE/GUJARAT/{folder_name}/{file_name}.xlsx", index=False)

    # Specify the destination directory where you want to copy the script
    # destination_directory = f"Scrapped_data/JUNE/MP/{folder_name}/"

    # copy_script_to_directory(destination_directory,file_name)


if __name__ == "__main__":
    main()
