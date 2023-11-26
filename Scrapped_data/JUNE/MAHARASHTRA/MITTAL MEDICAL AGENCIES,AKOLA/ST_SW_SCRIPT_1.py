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
    stockiest_name = folder_name

    file_name = "ST"


    pdf_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.pdf'  # Replace with the actual path to your PDF file
    text = parse_pdf(pdf_file_path)


    lines = text.strip().split('\n')
    # print(text)


    data = []  # List to store the data for Excel

    medicine_names = []
    
    # Iterate through the lines and split each line by spaces to extract the first part as the medicine name
    for line in lines:
        parts = line.split()
        # print(parts)
        # print("Before Line Length : ",len(parts), "\n")
        # print("Before Line Length : ",len(parts))

        # if len(parts) == 6:
        #     print(parts)

        #     # medicine_name = " ".join(parts[0:2])    # The first part is the medicine name
        #     medicine_name = parts[0]   # The first part is the medicine name

        #     if medicine_name == "ITEM" or medicine_name == "OPENING" or medicine_name == "Phone":
        #         continue
        #     elif "PRODUCT" in medicine_name:
        #         continue
        #     elif "Page" in medicine_name:
        #         continue

        #     freeStrip = "0"
        #     openingStrip = parts[-4] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-3] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-2] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-1] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        

        # if len(parts) == 7:
        #     print(parts)

        #     medicine_name = " ".join(parts[0:2])    # The first part is the medicine name


        #     if medicine_name == "GST NO. :" or medicine_name == "STOCK &":
        #         continue

        #     if '*' in medicine_name:
        #         medicine_name = medicine_name[:-4]
        #     elif "PRODUCT" in medicine_name:
        #         continue
        #     elif "Page" in medicine_name:
        #         continue
        #     freeStrip = "0"
        #     openingStrip = parts[-4] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-3] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-2] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-1] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        

        # if len(parts) == 8:
        #     print(parts)

        #     medicine_name = " ".join(parts[0:2])    # The first part is the medicine name

        #     if medicine_name == "GST NO. :" or medicine_name == "Phone":
        #         continue

        #     if '*' in medicine_name:
        #         medicine_name = medicine_name[:-4]
        #     elif "PRODUCT" in medicine_name:
        #         continue
        #     elif "Page" in medicine_name:
        #         continue
        #     freeStrip = "0"
        #     openingStrip = parts[-5] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-4] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-3] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-2] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) == 9:
        #     print(parts)

        #     medicine_name = " ".join(parts[0:2])    # The first part is the medicine name

        #     if '*' in medicine_name:
        #         medicine_name = medicine_name[:-4]
        #     elif "PRODUCT" in medicine_name:
        #         continue
        #     elif "Page" in medicine_name:
        #         continue
        #     freeStrip = "0"
        #     openingStrip = parts[-5] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-4] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-3] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-2] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])



        if len(parts) == 10:
            # print(parts)

            medicine_name = " ".join(parts[0:3])    # The first part is the medicine name


            if medicine_name == "GST NO. :" or medicine_name == "STOCK & SALES":
                continue

            if '*' in medicine_name:
                medicine_name = medicine_name[:-4]
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue

            freeStrip = "0"
            if not parts[-9].isnumeric():
                # print("if targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] ##Define Closing Qty Column Number if Formate Changes
            else:
                # print("else targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes

            # print("Medicine Name : ",medicine_name)
            # print("openingStrip : ",openingStrip)
            # print("purchaseQty : ",purchaseQty)
            # print("salesQty : ",salesQty)
            # print("closingQty : ",closingQty)
            # print(len(parts) , "\n")
            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])

        if len(parts) == 11:
            print(parts)

            # medicine_name = parts[0]    # The first part is the medicine name
            medicine_name = " ".join(parts[0:2])    # The first part is the medicine name
            if '*' in medicine_name:
                continue
            elif "Product" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            freeStrip = "0"

            if parts[-1] == "#":
                # print("IF targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            elif parts[-3] == "-":
                # print("ELIF targeted")
                openingStrip = parts[-8]
                purchaseQty = parts[-7] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-6] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-5]
            else:
                print("ELSE targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes

            print("Medicine Name : ",medicine_name)
            print("openingStrip : ",openingStrip)
            print("purchaseQty : ",purchaseQty)
            print("salesQty : ",salesQty)
            print("closingQty : ",closingQty)
            print(len(parts) , "\n")
            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        if len(parts) == 12:
            # print(parts)

            medicine_name = " ".join(parts[0:2])    # The first part is the medicine name
            
            if '*' in medicine_name:
                continue
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            elif "Value" in medicine_name:
                continue
            freeStrip = "0"

            if parts[-1] == "#":
                # print("IF targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            elif parts[-3] == "-":
                # print("ELIF targeted")
                openingStrip = parts[-8]
                purchaseQty = parts[-7] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-6] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-5] 
            else:
                # print("ELSE targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes


            # print("Medicine Name : ",medicine_name)
            # print("openingStrip : ",openingStrip)
            # print("purchaseQty : ",purchaseQty)
            # print("salesQty : ",salesQty)
            # print("closingQty : ",closingQty)
            # print(len(parts) , "\n")
            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        if len(parts) == 13:
            # print(parts)

            medicine_name = " ".join(parts[0:2])
            if '*' in medicine_name:
                medicine_name = medicine_name[:-4]
            elif "PRODUCT" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            freeStrip = "0"

            if parts[-1] == "#" or parts[-1] == "/":
                # print("IF targeted")
                openingStrip = parts[-8]
                purchaseQty = parts[-7] 
                salesQty = parts[-6] 
                closingQty = parts[-5] 

            if parts[-1] == "#":
                # print("IF targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            elif parts[-3] == "-":
                # print("ELIF targeted")
                openingStrip = parts[-8]
                purchaseQty = parts[-7] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-6] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-5] 
            else:
                # print("ELSE targeted")
                openingStrip = parts[-7]
                purchaseQty = parts[-6] #Define Purchase Qty Column Number if Formate Changes
                salesQty = parts[-5] #Define Sales Qty Column Number if Formate Changes
                closingQty = parts[-4] #
            date = "01/06/2023"
            division_name = "BIOS General" #Define division name if have any Changes


            # print("Medicine Name : ",medicine_name)
            # print("openingStrip : ",openingStrip)
            # print("purchaseQty : ",purchaseQty)
            # print("salesQty : ",salesQty)
            # print("closingQty : ",closingQty)
            # print(len(parts) , "\n")
            data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) == 14:
        #     # print(parts)

        #     medicine_name = " ".join(parts[0:2]).replace("-", "")    # The first part is the medicine name
            
        #     if len(medicine_name) < 2:

        #         medicine_name = ' '

        #     if '*' in medicine_name:
        #         medicine_name = medicine_name[:-4]          
        #     elif "S T" in medicine_name:
        #         continue
        #     elif "Page" in medicine_name:
        #         continue
        #     freeStrip = "0"


        #     if parts[-1] == "#" or parts[-1] == "/":
        #         # print("IF targeted")
        #         openingStrip = parts[-8]
        #         purchaseQty = parts[-7] 
        #         salesQty = parts[-6] 
        #         closingQty = parts[-5] 

        #     if len(parts[-7]) > 3 or len(parts[-6]) > 3:
        #         # print("IF 1 targeted")
        #         openingStrip = parts[-10] 

        #         if not openingStrip.isdigit():
        #             openingStrip = parts[-9]
        #             purchaseQty = parts[-8]
        #             salesQty = parts[-7]
        #             closingQty = parts[-4]
        #         else:
        #             openingStrip = parts[-10]
        #             purchaseQty = parts[-9]
        #             salesQty = parts[-8] 
        #             closingQty = parts[-5]

        #     elif parts[-8].isnumeric() or parts[-8] == "-":
        #         # print("ELIF targeted")
        #         openingStrip = parts[-8] 
        #         purchaseQty = parts[-7] 
        #         salesQty = parts[-6] 
        #         closingQty = parts[-3] 
        #     else:
        #         # print("ELSE targeted")
        #         openingStrip = parts[-8]
        #         purchaseQty = parts[-7] 
        #         salesQty = parts[-6] 
        #         closingQty = parts[-5] 
            
            
        #     date = "01/06/2023"
        #     division_name = "BIOS General" 

        #     # print("Medicine Name : ",medicine_name)
        #     # print("openingStrip : ",openingStrip)
        #     # print("purchaseQty : ",purchaseQty)
        #     # print("salesQty : ",salesQty)
        #     # print("closingQty : ",closingQty)
        #     # print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) == 15:
        #     # print(parts)

        #     medicine_name = " ".join(parts[0:3])    # The first part is the medicine name
        #     if '*' in medicine_name:
        #         medicine_name = medicine_name[:-4]
        #     elif "PRODUCT" in medicine_name:
        #         continue
        #     elif "Page" in medicine_name:
        #         continue

        #     freeStrip = "0"

        #     if parts[-1] == "#" or parts[-1] == "/":
        #         # print("IF targeted")
        #         openingStrip = parts[-8]
        #         purchaseQty = parts[-7] 
        #         salesQty = parts[-6] 
        #         closingQty = parts[-5] 

        #     if len(parts[-8]) > 3 or len(parts[-7]) > 3:
        #         # print("IF 1 targeted")
        #         openingStrip = parts[-11] 

        #         if openingStrip.isdigit():
        #             openingStrip = parts[-11]
        #             purchaseQty = parts[-10]
        #             salesQty = parts[-9]
        #             closingQty = parts[-6]
        #         else:
        #             openingStrip = parts[-10]
        #             purchaseQty = parts[-9]
        #             salesQty = parts[-8] 
        #             closingQty = parts[-5]

        #     elif parts[-8].isnumeric() or parts[-8] == "-":
        #         # print("ELIF targeted")
        #         openingStrip = parts[-8] 
        #         purchaseQty = parts[-7] 
        #         salesQty = parts[-6] 
        #         closingQty = parts[-3] 
        #     else:
        #         # print("ELSE targeted")
        #         openingStrip = parts[-8]
        #         purchaseQty = parts[-7] 
        #         salesQty = parts[-6] 
        #         closingQty = parts[-5] 

        #     # print("Medicine Name : ",medicine_name)
        #     # print("openingStrip : ",openingStrip)
        #     # print("purchaseQty : ",purchaseQty)
        #     # print("salesQty : ",salesQty)
        #     # print("closingQty : ",closingQty)
        #     # print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) == 16:
        #         print(parts)

        #         medicine_name = parts[0]   # The first part is the medicine name
        #         # medicine_name = " ".join(parts[0:3])    # The first part is the medicine name
        #         # if '*' in medicine_name:
        #         #     medicine_name = medicine_name[:-4]
        #         # elif "PRODUCT" in medicine_name:
        #         #     continue
        #         # elif "Page" in medicine_name:
        #         #     continue
        #         freeStrip = parts[-6]
        #         openingStrip = parts[-14] #Define Opening Strip Column Number if Formate Changes
        #         purchaseQty = parts[-13] #Define Purchase Qty Column Number if Formate Changes
        #         salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
        #         closingQty = parts[-1] #Define Closing Qty Column Number if Formate Changes
        #         date = "01/06/2023"
        #         division_name = "BIOS Darma" #Define division name if have any Changes

        #         print("Medicine Name : ",medicine_name)
        #         print(len(parts) , "\n")
        #         data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) == 17:
        #         print(parts)

        #         medicine_name = " ".join(parts[0:3])    # The first part is the medicine name
        #         if '*' in medicine_name:
        #             medicine_name = medicine_name[:-4]
        #         elif "PRODUCT" in medicine_name:
        #             continue
        #         elif "Page" in medicine_name:
        #             continue
        #         freeStrip = parts[-6]
        #         openingStrip = parts[-14] #Define Opening Strip Column Number if Formate Changes
        #         purchaseQty = parts[-13] #Define Purchase Qty Column Number if Formate Changes
        #         salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
        #         closingQty = parts[-1] #Define Closing Qty Column Number if Formate Changes
        #         date = "01/06/2023"
        #         division_name = "BIOS Darma" #Define division name if have any Changes

        #         print("Medicine Name : ",medicine_name)
        #         print(len(parts) , "\n")
        #         data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) == 18:
        #         print(parts)

        #         medicine_name = " ".join(parts[0:3])    # The first part is the medicine name
        #         if '*' in medicine_name:
        #             medicine_name = medicine_name[:-4]
        #         elif "PRODUCT" in medicine_name:
        #             continue
        #         elif "Page" in medicine_name:
        #             continue
        #         freeStrip = parts[-6]
        #         openingStrip = parts[-14] #Define Opening Strip Column Number if Formate Changes
        #         purchaseQty = parts[-13] #Define Purchase Qty Column Number if Formate Changes
        #         salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
        #         closingQty = parts[-1] #Define Closing Qty Column Number if Formate Changes
        #         date = "01/06/2023"
        #         division_name = "BIOS Darma" #Define division name if have any Changes

        #         print("Medicine Name : ",medicine_name)
        #         print(len(parts) , "\n")
        #         data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        # if len(parts) >= 19:
        #         print(parts)

        #         medicine_name = " ".join(parts[0:3])    # The first part is the medicine name
        #         if '*' in medicine_name:
        #             medicine_name = medicine_name[:-4]
        #         elif "PRODUCT" in medicine_name:
        #             continue
        #         elif "Page" in medicine_name:
        #             continue
        #         freeStrip = parts[-6]
        #         openingStrip = parts[-14] #Define Opening Strip Column Number if Formate Changes
        #         purchaseQty = parts[-13] #Define Purchase Qty Column Number if Formate Changes
        #         salesQty = parts[-7] #Define Sales Qty Column Number if Formate Changes
        #         closingQty = parts[-1] #Define Closing Qty Column Number if Formate Changes
        #         date = "01/06/2023"
        #         division_name = "BIOS Darma" #Define division name if have any Changes

        #         print("Medicine Name : ",medicine_name)
        #         print(len(parts) , "\n")
        #         data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])



        # if len(parts) == 20:
        #     print(parts)

        #     medicine_name = " ".join(parts[1:5])    # The first part is the medicine name
        #     freeStrip = "0"
        #     openingStrip = parts[-13] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-12] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-8] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-3] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])


        # if len(parts) == 21:
        #     print(parts)

        #     medicine_name = " ".join(parts[1:5])    # The first part is the medicine name
        #     freeStrip = "0"
        #     openingStrip = parts[-13] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-12] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-8] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-3] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])


        # if len(parts) == 22:
        #     print(parts)

        #     medicine_name = " ".join(parts[1:5])    # The first part is the medicine name
        #     freeStrip = "0"
        #     openingStrip = parts[-13] #Define Opening Strip Column Number if Formate Changes
        #     purchaseQty = parts[-12] #Define Purchase Qty Column Number if Formate Changes
        #     salesQty = parts[-8] #Define Sales Qty Column Number if Formate Changes
        #     closingQty = parts[-3] #Define Closing Qty Column Number if Formate Changes
        #     date = "01/06/2023"
        #     division_name = "BIOS General" #Define division name if have any Changes

        #     print("Medicine Name : ",medicine_name)
        #     print(len(parts) , "\n")
        #     data.append([stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])

        # print("\n")
    print("Total Medicines Name : ", len(data))



    # print("length of extracted medicine lines",len(extract_medicine_lines_list))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["StockistName","ProductName","FreeSrip", "OpeningQty","PurchaseQty", "SalesQty", "ClosingQty", "Date", "DivisionName"])

    # Export the DataFrame to an Excel file
    df.to_excel(f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/{file_name}.xlsx", index=False) #Provide Excel file name Here


    # print(extracted_medicines)
    # print("length of extracted medicines: ", len(extracted_medicines))


     # Specify the destination directory where you want to copy the script
    destination_directory = f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/"

    copy_script_to_directory(destination_directory,file_name)


if __name__ == "__main__":
    main()
