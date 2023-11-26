from openpyxl import Workbook
import pdfplumber
import pandas as pd
import os
import shutil
import re

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
    def __init__(self, folder_name, file_name, text):
        self.folder_name = folder_name
        self.file_name = file_name
        self.text = text
        self.data = []

    def process_data(self):
        lines = self.text.split('\n')
        stockiest_name = self.folder_name
        T_medical_name = None

        pattern = r'(?:[A-Z\.]+ (?:MEDICAL|CLINIC|MORBI|MEDICINCE|medical|Medicals|MEDICO|MEDICINS|DRUG|ESSENSE|ENTERPRISE|MEDICINE|SALES|TRUST|MEDICOS|JUNAGADH|ADIPUR|MEDICO\'S|PHRAMACY|CHEMIST|STORE|STORES|MED.STORE|MED.& GEN.STORE|MEDI&GEN|SURGICALS|WELLNESS BEAUTY HUB|HUB|DAVA|PHARMA|GEN|GENERAL|WELLNESS|HOSPITAL|AUSHADHI|VERAVAL|DOCTOR)|JETPUR|JAMJODHPUR|DWARKA|JAMNAGAR|JAM-JODHPUR|DHROL|DR\..*)'

        for line in lines:
            if re.findall(pattern, line):
                try:
                    t_match = line.split("-")
                    if len(t_match):
                        new_t_match = (" ".join(t_match[0:])).strip().split(" ")

                        T_medical_name = " ".join(new_t_match[1:])
                        print("Medical Name...:", T_medical_name)
                except:
                    pass
            else:
                t_line = line.split(' ')
                print("length", len(t_line))
                
                if 8 <= len(t_line) <= 13:
                    T_medicine_name = " ".join(t_line[0:3]).strip() if len(t_line) >= 13 else " ".join(t_line[0:3]).strip()
                    print("...........", T_medicine_name, "\n")
                    
                    rate = t_line[-2]
                    ExpQty = "0"
                    ReturnQty = "0"
                    SalesQty = t_line[-5] if len(t_line) != 10 else t_line[-4]
                    FreeStrip = t_line[-3] if len(t_line) == 11 else t_line[-4]
                    DamageQty = "0"
                    DivisionName = "BIOS GENERAL"

                    self.data.append([stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

    def save_to_excel(self):
        df = pd.DataFrame(self.data, columns=["StockistName", "ChemistName", "ProductName", "FreeSrip", "SELL STRIP", "ReturnQty", "ExpiredQty", "DamageQty", "Rate", "DivisionName"])
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
    folder_name = "SHAHU MEDICAL AGENCIES"
    file_name = "PW"
    pdf_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.pdf'

    pdf_parser = PDFParser(pdf_file_path)
    text = pdf_parser.text

    data_processor = DataProcessor(folder_name, file_name, text)
    data_processor.process_data()
    data_processor.save_to_excel()

    destination_directory = f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/"
    data_processor.copy_script_to_directory(destination_directory)

if __name__ == "__main__":
    main()
