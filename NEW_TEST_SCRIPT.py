from openpyxl import Workbook
import pdfplumber
import pandas as pd
import os
import shutil

class PDFParser:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.text = self.parse_pdf()

    def parse_pdf(self):
        text = ''
        with pdfplumber.open(self.pdf_file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text

class DataProcessor:
    def __init__(self, folder_name, stockiest_name, file_name, text):
        self.folder_name = folder_name
        self.stockiest_name = stockiest_name
        self.file_name = file_name
        self.text = text
        self.data = []

    def process_data(self):
        lines = self.text.strip().split('\n')
        for line in lines:
            parts = line.split()
            # print(len(parts))
            if 11 <= len(parts) <= 15:
                print(parts)    
                medicine_name = " ".join(parts[0:2]) if len(parts) == 11 else " ".join(parts[0:2])
                if '*' in medicine_name:
                    medicine_name = medicine_name[:-4]
                elif "PRODUCT" in medicine_name or "Page" in medicine_name or "Product Pack" in medicine_name:
                    continue

                free_strip = "0"
                opening_strip = parts[-10] if len(parts) > 12 and len(parts) <= 14 else parts[-9]
                purchase_qty = parts[-3]
                sales_qty = parts[-2]
                closing_qty = parts[-4]
                date = "01/06/2023"
                division_name = "BIOS General"

                print("Medicine Name:", medicine_name)
                print("opening_strip", opening_strip)
                print("purchase_qty", purchase_qty)
                print("sales_qty", sales_qty)
                print("closing_qty", closing_qty)
                print("len ",len(parts), "\n")

                self.data.append([self.stockiest_name, medicine_name, free_strip, opening_strip, purchase_qty,
                                  sales_qty, closing_qty, date, division_name])

        print("Total Medicines Name:", len(self.data))

    def save_to_excel(self):
        df = pd.DataFrame(self.data, columns=["StockistName", "ProductName", "FreeStrip", "OpeningQty", "PurchaseQty",
                                               "SalesQty", "ClosingQty", "Date", "DivisionName"])

        excel_file_path = f"Scrapped_data/JUNE/MAHARASHTRA/{self.folder_name}/{self.file_name}.xlsx"
        df.to_excel(excel_file_path, index=False)
        print(f"Data saved to {excel_file_path} successfully.")

    def copy_script_to_directory(self, destination_directory):
        try:
            current_script_path = os.path.abspath(__file__)
            script_filename = os.path.basename(current_script_path)
            destination_file = os.path.join(destination_directory, f"{self.file_name}_{script_filename}")

            if os.path.exists(destination_file):
                os.remove(destination_file)

            shutil.copy(current_script_path, destination_file)
            print(f"Script '{script_filename}' copied to '{destination_file}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    folder_name = "SENIOR AGENCY"
    stockiest_name = folder_name
    file_name = "stk&sl"
    pdf_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.pdf'

    pdf_parser = PDFParser(pdf_file_path)
    text = pdf_parser.text

    data_processor = DataProcessor(folder_name, stockiest_name, file_name, text)
    data_processor.process_data()
    data_processor.save_to_excel()

    destination_directory = f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/"
    data_processor.copy_script_to_directory(destination_directory)

if __name__ == "__main__":
    main()
