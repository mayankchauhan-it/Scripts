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
        current_script_path = os.path.abspath(__file__)

        script_filename = os.path.basename(current_script_path)

        destination_file = os.path.join(destination, f"{file_name}_{os.path.basename(current_script_path)}")
        if os.path.exists(destination_file):
            os.remove(destination_file)  

        shutil.copy(current_script_path, destination_file)  
        print(f"Script '{script_filename}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    folder_name = "MEDICINE POINT"
    file_name = "PW"


    pdf_file_path = 'Scrapped_data/JUNE/RAJASTHAN/' + folder_name + '/' + file_name + '.pdf'  
    text = parse_pdf(pdf_file_path)
    pattern = r'(?:[A-Z\.]+ (?:MEDICAL|CLINIC|MORBI|MEDICINCE|medical|Medicals|MEDICO|MEDICINS|DRUG|ESSENSE|ENTERPRISE|MEDICINE|SALES|TRUST|MEDICOS|JUNAGADH|ADIPUR|MEDICO\'S|PHRAMACY|CHEMIST|STORE|STORES|MED.STORE|MED.& GEN.STORE|MEDI&GEN|SURGICALS|WELLNESS BEAUTY HUB|HUB|DAVA|PHARMA|GEN|GENERAL|WELLNESS|HOSPITAL|AUSHADHI|VERAVAL|DOCTOR)|JETPUR|JAMJODHPUR|DWARKA|JAMNAGAR|JAM-JODHPUR|DHROL|DR\..*)'
    
    lines = text.split('\n')
    
    Stockiest_name = folder_name 
    data = []
    
    T_medical_name = None
    
    counter = 0
    for line in lines:
        if re.findall(pattern, line):
            counter += 1
            try:
                t_match = line.split(" ")
                if len(t_match):
                    T_medical_name = " ".join(t_match[0:])
                    print("Medical Name...:", T_medical_name)
            except:
                pass

        else:
            t_line = line.split(' ')
            print("length", len(t_line))
            if len(t_line) == 6:
                T_medicine_name = " ".join(t_line[0:2]).strip()
                print(T_medicine_name)
                rate = t_line[-1]
                ExpQty = t_line[-2]
                ReturnQty = "0"
                SalesQty = t_line[-3]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])


            if len(t_line) == 7:
                T_medicine_name = t_line[0]

               
                print(T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])


            if len(t_line) == 8:
                T_medicine_name = " ".join(t_line[0:2]).strip()

                if '*' in T_medicine_name:  
                    T_medicine_name = T_medicine_name[:-4]  
                print(T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 9:
                T_medicine_name = " ".join(t_line[0:3]).strip()

                if '*' in T_medicine_name:  
                    T_medicine_name = T_medicine_name[:-4]  
                
                print(T_medicine_name, "\n")
                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-5]
                FreeStrip = t_line[-4]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 10:
                T_medicine_name = " ".join(t_line[2:3]).strip()
                print("...........",T_medicine_name, "\n")
                rate = t_line[-2]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-3]
                FreeStrip = "0"
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"

                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 11:
                T_medicine_name = " ".join(t_line[2:4]).strip()
                print("...........",T_medicine_name, "\n")
                rate = t_line[-2]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-3]
                FreeStrip = t_line[-3]
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"

                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 12:
                T_medicine_name = " ".join(t_line[2:4]).strip()
                print("...........",T_medicine_name, "\n")
                rate = t_line[-2]
                ExpQty = "0"
                ReturnQty = "0"
                SalesQty = t_line[-3]
                FreeStrip = "0"
                DamageQty = "0"
                DivisionName = "BIOS GENERAL"

                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 13:
                T_medicine_name = " ".join(t_line[2:5]).strip()

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
    df.to_excel(f"Scrapped_data/JUNE/RAJASTHAN/{folder_name}/{file_name}.xlsx", index=False)

    destination_directory = f"Scrapped_data/JUNE/RAJASTHAN/{folder_name}/"

    copy_script_to_directory(destination_directory,file_name)


if __name__ == "__main__":
    main()
