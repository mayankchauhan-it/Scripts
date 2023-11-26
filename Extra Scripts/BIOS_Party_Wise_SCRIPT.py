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


def main():
    pdf_file_path = 'Scrapped_data/JUNE/UP/PW.pdf'  # Replace with the actual path to your PDF file
    text = parse_pdf(pdf_file_path)

    # Remove separator lines
    text = replace_separator_lines(text)

    medical_keywords = ["MEDICAL", "PHARMACY", "CLINIC", "HEALTHCARE",
                        "HOSPITAL", "SHOP", "-BHOPAL", "DR.", " AGENCY "]  # Add more keywords as needed

    text_splited = text.split('\n')  # Split
    medical_name_list = []  # List of medical_name_list
    found_medical_name = False

    for i in text_splited:
        j = i.replace(
            '--------------------------------------------------------', "")
        for keyword in medical_keywords:
            if keyword in j and not found_medical_name:
                medical_name_list.append(j)
                found_medical_name = True

        # Reset the flag for the next line
        found_medical_name = False


    # Extract and print medicine names
    medicine_names = extract_medicine_names(text)
    extracted_medicines = []
    for name in medicine_names:
        splited = name.split("\n")

        if len(splited) > 1:
            extracted_medicines.append(splited[1])

        else:
            extracted_medicines.append(splited[0])


    extract_medicine_lines_list = []
    # Extract and print medicine names and their lines
    medicine_data = extract_medicine_lines(text)

    print("Medicine Name...........:", len(medicine_data),)

    # Print the extracted medicine lines
    for line in medicine_data:
        # print("Medicine Name...........:", line, "\n")

        extract_medicine_lines_list.append(line)

    data = []  # List to store the data for Excel

    for line in range(len(extract_medicine_lines_list)):
        lines = extract_medicine_lines_list[line].strip().split('\n')


        f_medicine_name = extracted_medicines[line]

        for line in lines:
            integers, non_integers_part = split_line_into_parts(line)
            rate = None
            FreeStrip = None
            SellStrip = None
            try:
                # Extract rate and qty from integers list
                rate = integers[-3]  # Rate is the third-to-last element
                FreeStrip_t = non_integers_part[-1]   # Qty is the fifth-to-last element

                if FreeStrip_t == "-":
                    FreeStrip = "0"
                    SellStrip = integers[-4]   # Qty is the fifth-to-last element

                else:
                    FreeStrip = integers[-4]
                    SellStrip = integers[-5]   # Qty is the fifth-to-last element


                
                # print(rate)
                # print(qty)
            except:
                pass

            try:
                sp = non_integers_part.split(" ")
                # print(sp)
            except:
                pass
            
            ExpiredQty = "0"
            ReturnQty = "0"
            DamagedQty = "0"
            DivisionName = "BIOS DERMA"

            StockistName = "AMIT PHARMA"
            ChemistName = " "
        
        
        data.append([StockistName,f_medicine_name,ChemistName, FreeStrip, SellStrip,ExpiredQty,ReturnQty,DamagedQty,rate, DivisionName])

    print("length of extracted medicine lines",len(extract_medicine_lines_list))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["StockistName","ProductName","ChemistName","FreeSrip", "SELL STRIP","ExpiredQty", "ReturnQty", "DamageQty", "Rate", "DivisionName"])

    # Export the DataFrame to an Excel file
    df.to_excel("Scrapped_data/Excel/Party Wise/MP/AMIT_PHARMA/PW.xlsx", index=False) #Provide Excel file name Here


    # print(extracted_medicines)
    # print("length of extracted medicines: ", len(extracted_medicines))


if __name__ == "__main__":
    main()
