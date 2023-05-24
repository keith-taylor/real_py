from pathlib import Path
import shutil

top_level_path = Path.home()/"notes_2"/"project_one"
directory_to_toggle = top_level_path/"toggled_directory"

def print_scan_of_dir(dir_to_scan):
    print(f"\nThe '{(str(dir_to_scan)).split('/')[-1]}' directory contains the following sub-directories: ")
    for path in dir_to_scan.glob("*"):
            if path.is_dir(): # to stop it printing files 
                print(path)

def create_or_delete_directory(directory_to_toggle):
    print_scan_of_dir(top_level_path)
    if directory_to_toggle.is_dir():
        print(f"\nThe directory '{(str(directory_to_toggle)).split('/')[-1]}' exists but will now, sadly, be deleted.")
        # directory_to_toggle.rmdir() 
        shutil.rmtree(directory_to_toggle)  
    else:
        print(f"\nThe directory '{(str(directory_to_toggle)).split('/')[-1]}' does not currently exist but will now be created.")
        directory_to_toggle.mkdir()
    print_scan_of_dir(top_level_path)


create_or_delete_directory(directory_to_toggle)

# print({(str(path)).split('/')[-1]})

