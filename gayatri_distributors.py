import pandas as pd
import re
from common import extract_text, remove_unnecessary_space, ss_pdf_columns, pw_pdf_columns
import pathlib
import time


class GayatriDistributors:

    def __init__(self, file: str, date: str, stockie_Name: str):
        self.file = file
        self.date = date
        self.stockie_name = stockie_Name

        self.text = ''
        self.file_name = ''
        self.file_type = ''
        self.lines = []
        self.data = []
        self.chemist_names = []
        self.main()

    def main(self):
        extract_text(self)
        remove_unnecessary_space(self)
        self.fetch_file_type_name()
        self.extract_medicine_line()
        self.detect_functions()
        self.create_excel()

    def fetch_file_type_name(self):
        self.file_name = pathlib.Path(self.file).stem

        if "stock" in self.file_name.lower():
            self.file_type = "SS"
        else:
            self.file_type = "PW"

    def detect_functions(self):
        if "stock general" in self.file_name.lower():
            self.stock_general()
        elif "stock derma" in self.file_name.lower():
            self.stock_derma()
        elif "party general" in self.file_name.lower():
            self.party_general()
        elif "party derma" in self.file_name.lower():
            self.party_derma()

    def extract_chemist_names(self):
        # Skipped first two rows
        self.chemist_names = re.findall('(?:[A-Z])+(?:\s)(?:.*?)\,(?:.*)(?:[A-Z])\n', self.text)

    def extract_medicine_line(self):
        self.lines = re.findall('(?:[A-Z]+)(?:.*?)(?:\d+|-)\n', self.text)

    @staticmethod
    def extract_medicine_name(text):
        try:
            name = re.findall('(?:[A-Z]+)(?:.*[A-Z])(?:.*?)(?:(?:.*?)%\)|\s(?:.*?\%|)|(?:.*)[A-Z]|\.)', text)[0]
        except:
            name = ''
        return name

    def stock_general(self):
        free_strips = 0
        division_name = "BIOS GENERAL"

        for line in self.lines:

            data = re.findall('\d+\/\d+\/\d{4}|Total', line)

            if len(data) == 0:
                line = line.replace("\n", "").strip()
                product_name = self.extract_medicine_name(line)
                content = line.replace(product_name, "").strip().split()

                if len(content) > 2:
                    try:
                        if len(content) == 10 or len(content) == 9:
                            opening_qty = content[0].strip()
                            purchase_qty = content[1].strip()
                            sales_qty = content[2].strip()
                            closing_qty = content[4].strip()
                        elif len(content) == 11:
                            opening_qty = content[1].strip()
                            purchase_qty = content[2].strip()
                            sales_qty = content[3].strip()
                            closing_qty = content[5].strip()
                        else:
                            raise Exception("Length")

                        self.data.append([division_name, self.stockie_name, product_name, free_strips, opening_qty,
                                          purchase_qty, sales_qty, closing_qty, self.date])
                    except:
                        print(f"Error in line = {line}, ctx = {content}")

    def stock_derma(self):
        free_strips = 0
        division_name = "BIOS DERMA"

        for line in self.lines:

            data = re.findall('\d+\/\d+\/\d{4}|Total', line)

            if len(data) == 0:
                line = line.replace("\n", "").strip()
                product_name = self.extract_medicine_name(line)
                content = line.replace(product_name, "").strip().split()

                if len(content) > 2:
                    try:
                        if len(content) == 10 or len(content) == 9:
                            opening_qty = content[0].strip()
                            purchase_qty = content[1].strip()
                            sales_qty = content[2].strip()
                            closing_qty = content[4].strip()
                        elif len(content) == 11:
                            opening_qty = content[1].strip()
                            purchase_qty = content[2].strip()
                            sales_qty = content[3].strip()
                            closing_qty = content[5].strip()
                        else:
                            raise Exception("Length")

                        self.data.append([division_name, self.stockie_name, product_name, free_strips, opening_qty,
                                          purchase_qty, sales_qty, closing_qty, self.date])
                    except:
                        print(f"Error in line = {line}, ctx = {content}")

    def party_general(self):

        division_name = "BIOS GENERAL"

        title = ""
        medicine = ""
        medicineIndex = 0
        chemist_index = 0

        self.extract_chemist_names()

        for eachLine in self.text.split("\n"):

            for cIndex in range(chemist_index, len(self.chemist_names)):
                medical_name = self.chemist_names[cIndex].replace("GENERAL\n", "").replace("\n", "").strip()
                if "BIOS" in medical_name or self.stockie_name.lower() in medical_name.lower():
                    continue

                if medical_name in eachLine:
                    title = medical_name
                    chemist_index = cIndex
                    break

            if not title:
                continue

            for index in range(medicineIndex, len(self.lines)):
                line = self.lines[index].replace("\n", "").strip()
                if line in eachLine and "party total" not in line.lower():
                    medicine = line
                    medicineIndex = index

                    line = self.lines[medicineIndex].replace("\n", "").strip()

                    data = re.findall('Total|From|Mob|NR.', line)

                    if len(data) == 0:
                        product_name = self.extract_medicine_name(line)
                        chemist_name = title
                        content = re.findall('\d{1,2}\-\d{1,2}\-\d{4}(?:.*)', line)

                        if len(content) == 1:
                            content = content[0].split()
                            try:
                                product_name = re.findall('(?:.*)(?:10TAB|TAB|GM|ML|MG|(?:\d+[M|C|T|G]))', product_name)[0]
                            except:
                                print("Error Product name = ", product_name)

                            try:
                                free_strips = float(content[4].strip())
                                sale_strip = float(content[3].strip())
                                exp_qty = 0
                                return_qty = 0
                                damage_qty = 0
                                rate = float(content[5].strip())

                                self.data.append(
                                    [division_name, self.stockie_name, chemist_name, product_name, free_strips,
                                     sale_strip,
                                     exp_qty, return_qty, damage_qty, rate, self.date])
                            except:
                                print(f"Error in line = {line}, ctx = {content}")
                                pass
                        else:
                            print(f"Error in line = {line}, ctx = {content}")

                    break

    def party_derma(self):

        division_name = "BIOS DERMA"

        title = ""
        medicine = ""
        medicineIndex = 0
        chemist_index = 0

        self.extract_chemist_names()

        for eachLine in self.text.split("\n"):

            for cIndex in range(chemist_index, len(self.chemist_names)):
                medical_name = self.chemist_names[cIndex].replace("GENERAL\n", "").replace("\n", "").strip()
                if "BIOS" in medical_name or self.stockie_name.lower() in medical_name.lower():
                    continue

                if medical_name in eachLine:
                    title = medical_name
                    chemist_index = cIndex
                    break

            if not title:
                continue

            for index in range(medicineIndex, len(self.lines)):
                line = self.lines[index].replace("\n", "").strip()
                if line in eachLine and "party total" not in line.lower():
                    medicine = line
                    medicineIndex = index

                    line = self.lines[medicineIndex].replace("\n", "").strip()

                    data = re.findall('Total|From|Mob|NR.', line)

                    if len(data) == 0:
                        product_name = self.extract_medicine_name(line)
                        chemist_name = title
                        content = re.findall('\d{1,2}\-\d{1,2}\-\d{4}(?:.*)', line)

                        if len(content) == 1:
                            content = content[0].split()
                            try:
                                product_name = re.findall('(?:.*)(?:10TAB|TAB|GM|ML|MG|(?:\d+[M|C|T|G]))', product_name)[0]
                            except:
                                print("Error Product name = ", product_name)

                            try:
                                free_strips = float(content[4].strip())
                                sale_strip = float(content[3].strip())
                                exp_qty = 0
                                return_qty = 0
                                damage_qty = 0
                                rate = float(content[5].strip())

                                self.data.append(
                                    [division_name, self.stockie_name, chemist_name, product_name, free_strips,
                                     sale_strip,
                                     exp_qty, return_qty, damage_qty, rate, self.date])
                            except:
                                print(f"Error in line = {line}, ctx = {content}")
                                pass
                        else:
                            print(f"Error in line = {line}, ctx = {content}")

                    break

    def create_excel(self):
        if self.data:
            op_file_name = f"Scrapped_data/JUNE/GUJARAT/GAYATRI DISTRIBUTORS/general Gayatri jun23.xlsx"
            df = pd.DataFrame(self.data,
                              columns=ss_pdf_columns if self.file_type == "SS" else pw_pdf_columns)

            df.to_excel(op_file_name, index=False)
            print(f"Extraction Completed at : {op_file_name}")

    def method_to_measure(self):
        # The method you want to measure
        pass

if __name__ == "__main__":
    # Record start time
    start_time = time.time()

    pdf_path = "Scrapped_data/JUNE/GUJARAT/GAYATRI DISTRIBUTORS/general Gayatri jun23.pdf"
    Date = "2023-05-01"
    stockieName = "GAYATRI DISTRIBUTORS"

    obj = GayatriDistributors(pdf_path, Date, stockieName)



    # Execute the main method
    obj.main()

    # Record end time
    end_time = time.time()
    
    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time} seconds")