from pathlib import Path

notes_2 = Path.home()/"notes_2"
# move dir
source_dir = notes_2/"project_one"/"POs"
destination_dir = notes_2/"project_one"/"financial_reporting/POs" # NB: You need to include 'POs' in the destination

file_name = "purchase_orders.xlsm"

first_file_path = notes_2/"project_one"/"financial_reporting"
second_file_path = notes_2/"project_one"/"financial_reporting/POs"

def switch_file_folder(file_name, first_dir, second_dir):
    # loop-de-loop, AKA the old switcharoony
    def switch(source_path, destination_path):
        source_path.replace(destination_path)
        print(f"File '{file_name}' moved from {(str(source_path)).split('/')[-2:-1]} to {(str(destination_path)).split('/')[-2:-1]}.")
        
    if (first_dir/file_name).is_file():
        source_path = first_dir/file_name
        destination_path = second_dir/file_name
        switch(source_path, destination_path)
    elif (second_dir/file_name).is_file():
        source_path = second_dir/file_name
        destination_path = first_dir/file_name
        switch(source_path, destination_path)
    else:
        print(f"File '{file_name}' not found in either '{(str(first_dir)).split('/')[-1]}' or '{(str(second_dir)).split('/')[-1]}' directories. ")

switch_file_folder(file_name, first_file_path, second_file_path)   

