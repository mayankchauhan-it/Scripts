from openpyxl import Workbook
import pdfplumber
import re
import pandas as pd


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
    pattern = r'\b[A-Z][A-Z0-9\s\/\-]*(?:\s?(?:GM|ACCUTHRO |G1|G2|ITRA|ML|TAB|CAP|CREAM|GEL|OINTMENT|DROPS|SOLUTION|POWDER|INJECTION|SPRAY|LOTION|SUPPOSITORY|INHALER|CHEWABLE|LOZENGE|SUSPENSION|ELIXIR|SUSTAINED RELEASE|EXTENDED RELEASE|FORTE|EXTRA|PLUS|JUNIOR|MAX|FORTIFIED|SR|XR|DS|HCL|CR|EC|LA|Rapid Release|MR|IR|XL|HD|LD|DF|PR|HR|BR|ER|F|F\/W|CRM|SHAMPOO|CREAM|PRO|FACE WASH))(?=\s|$)'

    medicine_names = re.findall(pattern, text)
    return medicine_names


def extract_medicine_lines(text):
    # Define a regular expression pattern for medicine names
    pattern = r'\b[A-Z][A-Z0-9\s\/\-]*(?:\s?(?:GM|ACCUTHRO |[*]|CACHER|G1|G2|G2P|BIOKET|ITRA|60K|ITRA|ML|TAB|CAP|CREAM|GEL|OINTMENT|DROPS|SOLUTION|POWDER|INJECTION|SPRAY|LOTION|SUPPOSITORY|INHALER|CHEWABLE|LOZENGE|SUSPENSION|ELIXIR|SUSTAINED RELEASE|EXTENDED RELEASE|FORTE|EXTRA|PLUS|JUNIOR|MAX|FORTIFIED|SR|XR|DS|HCL|CR|EC|LA|Rapid Release|MR|IR|XL|HD|LD|DF|PR|HR|BR|ER|F|F\/W|CRM|SHAMPOO|CREAM|PRO|FACE WASH))(?=\s|$)'

    # Split the text into lines
    lines = text.split('\n')

    # Initialize a list to store lines containing medicine names
    medicine_lines = []

    # Iterate through the lines and check if each line contains a medicine name
    for line in lines:
        if re.search(pattern, line):
            medicine_lines.append(line)

    return medicine_lines


def main():
    pdf_file_path = 'Scrapped_data/PDF/GUJARAT/CRITIVAC CARE UNIT/GENERAL ST.pdf'  # Replace with the actual path to your PDF file
    stockiest_name = "CRITIVAC CARE UNIT" #Modify the name of the stockiest
    text = parse_pdf(pdf_file_path)


    lines = text.strip().split('\n')
    # print(text)


    data = []  # List to store the data for Excel

    medicine_names = []
    
    # Iterate through the lines and split each line by spaces to extract the first part as the medicine name
    for line in lines:
        parts = line.split()
        # print(parts)
        # print("Before Line Length : ",len(parts) )

        # if len(parts) > 11 and len(parts) < 13:
        # # if len(parts) > 9 and len(parts) < 11:
        # # # if len(parts) > 9 and len(parts) < 11:
        # if len(parts) > 14 and len(parts) < 16:
        if len(parts) > 16 and len(parts) < 18: #17 length

            medicine_name = parts[1] + " " + parts[2] + " " + parts[3] + " " + parts[4]
            freeStrip = parts[-6] #Define Opening Strip Column Number if Formate Changes
            openingStrip = parts[-10] #Define Opening Strip Column Number if Formate Changes
            purchaseQty = parts[-9] #Define Purchase Qty Column Number if Formate Changes
            salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
            closingQty = parts[-4] #Define Closing Qty Column Number if Formate Changes
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes



            print("Medicine Name : ",medicine_name)
            print("Free Strip : ",freeStrip)
            print ("Opening strip:", openingStrip)
            print ("purchaseQty:", purchaseQty)
            print ("salesQty:", salesQty)
            print ("closingQty:", closingQty)
            print("Line Length : ", len(parts) , "\n")

            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])

        if len(parts) > 15 and len(parts) < 17: #16 length

            medicine_name = parts[1] + " " + parts[2] + " " + parts[3] 
            freeStrip = parts[-7] #Define Opening Strip Column Number if Formate Changes
            openingStrip = parts[-11]#Define Opening Strip Column Number if Formate Changes
            purchaseQty = parts[-10] #Define Purchase Qty Column Number if Formate Changes
            salesQty = parts[-8] #Define Sales Qty Column Number if Formate Changes
            closingQty = parts[-6] #Define Closing Qty Column Number if Formate Changes
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes



            print("Medicine Name : ",medicine_name)
            print("Free Strip : ",freeStrip)
            print ("Opening strip:", openingStrip)
            print ("purchaseQty:", purchaseQty)
            print ("salesQty:", salesQty)
            print ("closingQty:", closingQty)
            print("Line Length : ", len(parts) , "\n")

            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])


        # # # if len(parts) > 10 and len(parts) < 12:
        # # # # # if len(parts) > 13 and len(parts) < 15:
        if len(parts) > 14 and len(parts) < 16: #15 length

            medicine_name = parts[1] + " " + parts[2] + " " + parts[3] # The first part is the medicine name
            freeStrip = parts[-7]
            openingStrip = parts[-11] #Define Opening Strip Column Number if Formate Changes
            purchaseQty = parts[-9] #Define Purchase Qty Column Number if Formate Changes
            salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
            closingQty = parts[-5] #Define Closing Qty Column Number if Formate Changes
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes

            
            
            print("Medicine Name : ",medicine_name)
            print("Free Strip : ",freeStrip)
            print ("Opening strip:", openingStrip)
            print ("purchaseQty:", purchaseQty)
            print ("salesQty:", salesQty)
            print ("closingQty:", closingQty)
            print("Line Length : ", len(parts) , "\n")


            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])

        
        # # # if len(parts) > 9 and len(parts) < 11:
        # # # # # if len(parts) > 7 and len(parts) < 9:
        if len(parts) > 13 and len(parts) < 15:  #14 length

            medicine_name = parts[1] + " " + parts[2]    # The first part is the medicine name
            freeStrip = parts[-6]
            openingStrip = parts[-10] #Define Opening Strip Column Number if Formate Changes
            purchaseQty = parts[-9]#Define Purchase Qty Column Number if Formate Changes
            salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
            closingQty = parts[-4] #Define Closing Qty Column Number if Formate Changes


            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes

            print("Medicine Name : ",medicine_name)
            print("Free Strip : ",freeStrip)
            print ("Opening strip:", openingStrip)
            print ("purchaseQty:", purchaseQty)
            print ("salesQty:", salesQty)
            print ("closingQty:", closingQty)
            print ("Date:", date)
            print ("Division Name:", division_name)
            print(len(parts) , "\n")
            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
    

    print("Total Medicines Name : ", len(data))



    # print("length of extracted medicine lines",len(extract_medicine_lines_list))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["StockistName","ProductName","FreeSrip", "OpeningQty","PurchaseQty", "SalesQty", "ClosingQty", "Date", "DivisionName"])

    # Export the DataFrame to an Excel file
    df.to_excel("Scrapped_data/Excel/Stock Wise/Gujarat/CRITIVAC CARE UNIT/GENERAL ST.xlsx", index=False) #Provide Excel file name Here


    # print(extracted_medicines)
    # print("length of extracted medicines: ", len(extracted_medicines))


if __name__ == "__main__":
    main()
