from e_functions import *
import re


def main():
    folder_name = "UNITED ENTERPRISE,DHULE"
    file_name = "PW"

    text_file_path = 'Scrapped_data/JUNE/MAHARASHTRA/' + folder_name + '/' + file_name + '.txt'

    text = parse_text_file(text_file_path)
    pattern = re.compile(r'^\s*Customer: \[.*\] (.+),.*$', re.MULTILINE)


    lines = text.split('\n')

    for line in lines:
        match = re.search(pattern, line)

        if match:
            print("Medical Name: ",match.group(1), "\n")
        
        else:
            t_line = re.sub(r'\s+', ' ', line).split()[1:]
            
            if len(t_line) > 1:
                # print("Line", t_line)
                print("length", len(t_line), "\n")


                # if len(t_line) == 10:
            #     T_medicine_name = " ".join(t_line[0:3]).strip()
            #     print("...........",T_medicine_name, "\n")
            #     rate = t_line[-3]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     SalesQty = t_line[-5]
            #     FreeStrip = t_line[-4]
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"

            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            # if len(t_line) == 11:
            #     T_medicine_name = " ".join(t_line[1:2]).strip()
            #     # print("...........",T_medicine_name, "\n")

            #     rate = t_line[-3]
            #     SalesQty = t_line[-4]
            #     ExpQty = "0"
            #     ReturnQty = "0"
            #     FreeStrip = "0"
            #     DamageQty = "0"
            #     DivisionName = "BIOS GENERAL"


            #     # print("Line : ",t_line)
            #     # print("Medicine Name : ",T_medicine_name)
            #     # print("SalesQty : ",SalesQty)
            #     # print("FreeStrip : ",FreeStrip)
            #     # print("rate : ",rate)
            #     # print(len(t_line) , "\n")
            #     data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 12:
                T_medicine_name = " ".join(t_line[1:3]).strip()

                if t_line[1] == "Sales":
                    continue
                elif t_line[1] == "Customer-Wise":
                    continue
                elif t_line[1] == "Product-Wise":
                    continue
                elif t_line[1] == "Name":
                    continue

                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"

                date_index = find_reverse_index_by_date(date_format, t_line)

                # print(f"Index in reverse: {-date_index}")

                if date_index == 6:
                    SalesQty = t_line[-4]
                    FreeStrip = "0"

                else:
                    SalesQty = t_line[-5]
                    FreeStrip = t_line[-4]

                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                # print("Line : ",t_line)
                # print("Medicine Name : ",T_medicine_name)
                # print("SalesQty : ",SalesQty)
                # print("FreeStrip : ",FreeStrip)
                # print("rate : ",rate)
                # print(len(t_line) , "\n")
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])

            if len(t_line) == 13:
                T_medicine_name = " ".join(t_line[1:3]).strip()

                if t_line[1] == "Sales":
                    continue
                elif t_line[1] == "Customer-Wise":
                    continue
                elif t_line[1] == "Product-Wise":
                    continue
                elif t_line[1] == "Name":
                    continue

                rate = t_line[-3]
                ExpQty = "0"
                ReturnQty = "0"

                # date_index = find_reverse_index_by_date(date_format, t_line)

                # print(f"Index in reverse: {-date_index}")

                if date_index == 6:
                    SalesQty = t_line[-4]
                    FreeStrip = "0"

                else:
                    SalesQty = t_line[-5]
                    FreeStrip = t_line[-4]

                DamageQty = "0"
                DivisionName = "BIOS GENERAL"
                # print("Line : ",t_line)
                # print("Medicine Name : ",T_medicine_name)
                # print("SalesQty : ",SalesQty)
                # print("FreeStrip : ",FreeStrip)
                # print("rate : ",rate)
                # print(len(t_line) , "\n")
                data.append([Stockiest_name, T_medical_name, T_medicine_name, FreeStrip, SalesQty, ReturnQty, ExpQty, DamageQty, rate, DivisionName])
            




            else:
               continue


if __name__ == "__main__":
    main()