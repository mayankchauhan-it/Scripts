from e_functions import *
import re
import pandas as pd



def main():
    folder_name = "JAIN DISTRIBUTORS,JALGAON"
    file_name = "st"
    Stockiest_name = folder_name
    text_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.txt'

    text = parse_text_file(text_file_path)
    lines = text.strip().split('\n')

    data = []

    for line in lines:
        parts = line.split()
        if len(parts) == 9:

            medicine_name = " ".join(parts[0:2])    
            
            if '*'  in medicine_name:
                continue
            elif "ITEM" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            elif "Value" in medicine_name:
                continue
            elif "Near" in medicine_name:
                continue
            
            freeStrip = "0"

            openingStrip, purchaseQty, salesQty, closingQty = parts[-5], parts[-4], parts[-2], parts[-1]
            date = "01/06/2023"
            division_name = "BIOS General"

            data.append([Stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])

        if len(parts) == 10:

            medicine_name = " ".join(parts[0:2])    
            
            if '*'  in medicine_name:
                continue
            elif "ITEM" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            elif "Value" in medicine_name:
                continue
            elif "Near" in medicine_name:
                continue
            
            freeStrip = "0"
            date = "01/06/2023"
            division_name = "BIOS General"

            openingStrip, purchaseQty, salesQty, closingQty = parts[-5], parts[-4], parts[-2], parts[-1]

            data.append([Stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])
        
        if len(parts) == 11:
            print(parts)

            medicine_name = " ".join(parts[0:2]) 
            
            if '*'  in medicine_name:
                continue
            elif "ITEM" in medicine_name:
                continue
            elif "Page" in medicine_name:
                continue
            elif "Value" in medicine_name:
                continue
            elif "Near" in medicine_name:
                continue
            
            freeStrip = "0"

            openingStrip, purchaseQty, salesQty, closingQty = parts[-5], parts[-4], parts[-2], parts[-1]

            date = "01/06/2023"
            division_name = "BIOS General"

            data.append([Stockiest_name,medicine_name,freeStrip, openingStrip, purchaseQty,salesQty,closingQty,date, division_name])

    print("Total Medicines Name : ", len(data))

    df = pd.DataFrame(data, columns=["StockistName","ProductName","FreeSrip", "OpeningQty","PurchaseQty", "SalesQty", "ClosingQty", "Date", "DivisionName"])

    df.to_excel(f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/{file_name}.xlsx", index=False)



    current_script_path = os.path.abspath(__file__)
    destination_directory = f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/"

    copy_script_to_directory(current_script_path, destination_directory,file_name)


if __name__ == "__main__":
    main()