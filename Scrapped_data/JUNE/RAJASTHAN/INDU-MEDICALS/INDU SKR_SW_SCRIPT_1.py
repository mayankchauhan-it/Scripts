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
    folder_name = "INDU-MEDICALS"
    stockiest_name = folder_name

    file_name = "INDU SKR"

    pdf_file_path = 'Scrapped_data/JUNE/RAJASTHAN/' + folder_name + '/' + file_name + '.pdf'  
    text = parse_pdf(pdf_file_path)


    lines = text.strip().split('\n')


    data = [] 
    for line in lines:
        parts = line.split()

        if len(parts) == 7:

            medicine_name = " ".join(parts[0])

            if '*' in medicine_name:
                medicine_name = medicine_name[:-4]
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            freeStrip = "0"
            openingStrip = parts[-5] 
            purchaseQty = parts[-4] 
            salesQty = parts[-2] 
            closingQty = parts[-1] 
            date = "01/06/2023"
            division_name = "BIOS General" 
            
            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        

        if len(parts) == 8:
            

            medicine_name = " ".join(parts[0:2])    

            if '*' in medicine_name:
                medicine_name = medicine_name[:-4]
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            freeStrip = "0"
            openingStrip = parts[-5] 
            purchaseQty = parts[-4] 
            salesQty = parts[-2] 
            closingQty = parts[-1] 
            date = "01/06/2023"
            division_name = "BIOS General" 

            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        if len(parts) == 9:

            medicine_name = " ".join(parts[0:2])

            if '*' in medicine_name:
                medicine_name = medicine_name[:-4]
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            freeStrip = "0"
            openingStrip = parts[-5] 
            purchaseQty = parts[-4] 
            salesQty = parts[-2] 
            closingQty = parts[-1] 
            date = "01/06/2023"
            division_name = "BIOS General" 

            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])


        if len(parts) == 10:

            medicine_name = " ".join(parts[0:2])

            if '*' in medicine_name:
                medicine_name = medicine_name[:-4]
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue

            freeStrip = "0"
            openingStrip = parts[-5] 
            purchaseQty = parts[-4] 
            salesQty = parts[-2] 
            closingQty = parts[-1] 
            date = "01/06/2023"
            division_name = "BIOS General" 

            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])


    df = pd.DataFrame(data, columns=["StockistName","ProductName","FreeSrip", "OpeningQty","PurchaseQty", "SalesQty", "ClosingQty", "Date", "DivisionName"])

    df.to_excel(f"Scrapped_data/JUNE/RAJASTHAN/{folder_name}/{file_name}.xlsx", index=False) #Provide Excel file name Here

    destination_directory = f"Scrapped_data/JUNE/RAJASTHAN/{folder_name}/"

    copy_script_to_directory(destination_directory,file_name)


if __name__ == "__main__":
    main()
