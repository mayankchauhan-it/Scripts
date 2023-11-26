import os
import shutil

def copy_file_with_unique_name(source, destination, counter):
    try:
        if os.path.isfile(source):
            if not os.path.exists(destination):
                os.makedirs(destination)

            # Generate a unique file name using the counter
            destination_file = os.path.join(destination, f"type {counter}_{os.path.basename(source)}")
            
            shutil.copy(source, destination_file)
            print(f"File '{source}' copied to '{destination_file}' successfully.")
        else:
            print(f"Source '{source}' is not a valid file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the source file and destination directory
source_file = 'C:\\Users\\Mayank\\Desktop\\Python Script\\copy_script.py'
destination_directory = 'C:\\Users\\Mayank\\Desktop\\Python Script\\copied'  # Use double backslashes for Windows paths

# You can specify the initial counter value
initial_counter = 1

# Find the current highest counter value in the destination directory
existing_files = os.listdir(destination_directory)
existing_counters = [int(file.split('_')[0].split()[-1]) for file in existing_files if file.startswith('type ')]
if existing_counters:
    initial_counter = max(existing_counters) + 1

copy_file_with_unique_name(source_file, destination_directory, initial_counter)
