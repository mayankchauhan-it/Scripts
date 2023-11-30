from e_functions import *
import re
import pandas as pd



def main():
    folder_name = "AMAR ENTERPRISES"
    file_name = "PW"
    Stockiest_name = folder_name
    text_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.txt'

    text = parse_text_file(text_file_path)
    pattern = re.compile(r'^\s*Customer: \[.*\] (.+),.*$', re.MULTILINE)
    pattern2 = re.compile(r'^\s*Customer\s*:\s*\d+\s*(.+?),.*$', re.MULTILINE)

    m_pattern = r'(?:[A-Z\.]+(?: MEDICAL| MEDICO| CLINIC| MEDICINCE| MED| medical| Medicals| MEDICINS| DRUG| ESSENSE| ENTERPRISE| MEDICINE| SALES| TRUST| RAJURA| MEDICOS| JUNAGADH| ADIPUR| MEDICO\'S| PHRAMACY| CHEMIST| STORE| STORES| MED.STORE| MED.& GEN.STORE| MEDI&GEN| SURGICALS| WELLNESS BEAUTY HUB| HUB| DAVA| PHARMA| GEN| GENERAL| WELLNESS| HOSPITAL| AUSHADHI| VERAVAL| MED.| DOCTOR)| JETPUR| JAMJODHPUR| DWARKA| JAMNAGAR| JAM-JODHPUR| DHROL| DR| INDORE| MORBI| BRAMHAPURI| MUL| GADCHANDUR| RAJURA| HEALTHCARE| CHIMUR|\[.*\]| DR\..*)'

    medi_pattern = re.compile(m_pattern, re.MULTILINE)

    # medi_pattern = re.compile(m_pattern, re.MULTILINE)
    


    lines = text.split('\n')

    data = []

    for line in lines:
        match = re.findall(medi_pattern, line)

        if folder_name in line:
            continue
        elif match:
            T_medical_name = line
            print("Medical Name: ", T_medical_name, "\n")
        
        else:
            t_line = re.sub(r'\s+', ' ', line).split()


            # print(t_line)
            
            if len(t_line) > 1:
                # print("Line", t_line)
                # print("length", len(t_line), "\n")


                # if len(t_line) == 10:
                #     T_medicine_name = " ".join(t_line[0:3]).strip()
                #     rate = t_line[-2]
                #     ExpQty = "0"
                #     ReturnQty = "0"
                #     SalesQty = t_line[-3]
                #     FreeStrip ="0"
                #     DamageQty = "0"
                #     DivisionName = "BIOS GENERAL"

                #     # print("Line : ",t_line)
                #     print("Medicine Name : ",T_medicine_name)
                #     # print("SalesQty : ",SalesQty)
                #     # print("FreeStrip : ",FreeStrip)
                #     # print("rate : ",rate)
                #     print(len(t_line) , "\n")

                #     # data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

                if len(t_line) == 11:
                    T_medicine_name = " ".join(t_line[0:2]).strip()

                    if "Name" in T_medicine_name:
                        continue

                    rate = t_line[-2]
                    ExpQty = "0"
                    ReturnQty = "0"
                    DamageQty = "0"
                    DivisionName = "BIOS GENERAL"

                    date_index = find_reverse_index_by_date(date_format, t_line)

                    if date_index == 9:
                        FreeStrip = "0"
                        SalesQty = t_line[-3]
                    else:
                        FreeStrip = t_line[-3]
                        SalesQty = t_line[-4]

                    # print("date_index", date_index)
                    # print("Line : ",t_line)
                    # print("Medicine Name : ",T_medicine_name)
                    # print("SalesQty : ",SalesQty)
                    # print("FreeStrip : ",FreeStrip)
                    # print("rate : ",rate)
                    # print(len(t_line) , "\n")
                    # data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

                if len(t_line) == 12:
                    T_medicine_name = " ".join(t_line[0:2]).strip()

                    if "Name" in T_medicine_name:
                        continue
                    elif  "Customer-Wise" in T_medicine_name:
                        continue
                    elif  "Product-Wise" in T_medicine_name:
                        continue
                    elif  "Product-Wise" in T_medicine_name:
                        continue
                    

                    rate = t_line[-2]
                    ExpQty = "0"
                    ReturnQty = "0"
                    DamageQty = "0"
                    DivisionName = "BIOS GENERAL"

                    date_index = find_reverse_index_by_date(date_format, t_line)

                    if date_index == 5:
                        FreeStrip = "0"
                        SalesQty = t_line[-3]
                    else:
                        FreeStrip = t_line[-3]
                        SalesQty = t_line[-4]

                    # print("date_index", date_index)
                    # print("Line : ",t_line)
                    # print("Medicine Name : ",T_medicine_name)
                    # print("SalesQty : ",SalesQty)
                    # print("FreeStrip : ",FreeStrip)
                    # print("rate : ",rate)
                    # print(len(t_line) , "\n")
                    # data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

                if len(t_line) == 13:
                    T_medicine_name = " ".join(t_line[0:3]).strip()

                    if "Name" in T_medicine_name:
                        continue
                    elif  "Customer-Wise" in T_medicine_name:
                        continue
                    elif  "Product-Wise" in T_medicine_name:
                        continue
                    elif  "Product-Wise" in T_medicine_name:
                        continue
                    

                    rate = t_line[-3]
                    ExpQty = "0"
                    ReturnQty = "0"
                    DamageQty = "0"
                    DivisionName = "BIOS GENERAL"

                    date_index = find_reverse_index_by_date(date_format, t_line)


                    if date_index == 6:
                        FreeStrip = "0"
                        SalesQty = t_line[-4]
                    else:
                        FreeStrip = t_line[-4]
                        SalesQty = t_line[-5]

                    # print("date_index", date_index)
                    # print("Line : ",t_line)
                    # print("Medicine Name : ",T_medicine_name)
                    # print("SalesQty : ",SalesQty)
                    # print("FreeStrip : ",FreeStrip)
                    # print("rate : ",rate)
                    # print(len(t_line) , "\n")
                    # data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
                
                if len(t_line) == 14:
                    T_medicine_name = " ".join(t_line[0:3]).strip()

                    if "Name" in T_medicine_name:
                        continue
                    elif  "Customer-Wise" in T_medicine_name:
                        continue
                    elif  "Product-Wise" in T_medicine_name:
                        continue
                    elif  "Product-Wise" in T_medicine_name:
                        continue
                    

                    rate = t_line[-3]
                    ExpQty = "0"
                    ReturnQty = "0"
                    DamageQty = "0"
                    DivisionName = "BIOS GENERAL"

                    date_index = find_reverse_index_by_date(date_format, t_line)


                    if date_index == 6:
                        FreeStrip = "0"
                        SalesQty = t_line[-4]
                    else:
                        FreeStrip = t_line[-4]
                        SalesQty = t_line[-5]

                    # print("date_index : ",date_index)
                    # print("Line : ",t_line)
                    # print("Medicine Name : ",T_medicine_name)
                    # print("SalesQty : ",SalesQty)
                    # print("FreeStrip : ",FreeStrip)
                    # print("rate : ",rate)
                    # print(len(t_line) , "\n")
                    # data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            # else:
            #    continue
    

    df = pd.DataFrame(data, columns=["StockistName", "ChemistName", "ProductName", "FreeSrip", "SELL STRIP", "ReturnQty", "ExpiredQty", "DamageQty", "Rate", "DivisionName"])
    df.to_excel(f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/{file_name}.xlsx", index=False)



    current_script_path = os.path.abspath(__file__)
    destination_directory = f"Scrapped_data/JUNE/MAHARASHTRA/{folder_name}/"

    copy_script_to_directory(current_script_path, destination_directory,file_name)



if __name__ == "__main__":
    main()