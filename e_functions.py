import shutil
import os



date_format = '26/03/23'


keywords = [
        r'MEDICAL|CLINIC|MEDICINCE|MED|medical|Medicals|MEDICO|MEDICINS|DRUG|ESSENSE|ENTERPRISE|MEDICINE|SALES|TRUST|RAJURA|MEDICOS|JUNAGADH|ADIPUR|MEDICO\'S|PHRAMACY|CHEMIST|STORE|STORES|MED.STORE|MED.& GEN.STORE|MEDI&GEN|SURGICALS|WELLNESS BEAUTY HUB|HUB|DAVA|PHARMA|GEN|GENERAL|WELLNESS|HOSPITAL|AUSHADHI|VERAVAL|MED.|DR\..*',
        # r'JETPUR|JAMJODHPUR|DWARKA|JAMNAGAR|JAM-JODHPUR|DHROL|DR|INDORE|MORBI|BRAMHAPURI|MUL|GADCHANDUR|RAJURA|CHIMUR|DHULE|DR\..*'
    ]


def parse_text_file(txt_file_path):
    text = ''

    try:
        with open(txt_file_path, 'r') as file:
            # Read all lines from the file and join them into a single string
            text = ''.join(file.readlines())
            return text
    except FileNotFoundError:
        print(f"Error: File not found at {txt_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



def find_index_by_date(date_format, my_list):
    for index, item in enumerate(my_list):
        if any(part.isdigit() and len(part) == 2 and part.startswith('0') for part in item.split('/')):
            return index
    return -1 

def find_reverse_index_by_date(date_format, my_list):
    for index in range(len(my_list) - 1, -1, -1):
        item = my_list[-index]
        if any(part.isdigit() and len(part) == 2 and part.startswith('0') for part in item.split('/')):
            return index 
    return -1  

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

