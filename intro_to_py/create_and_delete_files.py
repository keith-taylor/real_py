from pathlib import Path

notes_2 = Path.home()/"notes_2"
flicker_dir = notes_2/"project_one"/"here_and_gone"
flicker_file_name = flicker_dir/"now_you_see_me_now_you_dont.txt"
flicker_dir.mkdir(parents=True, exist_ok=True)

def scan_and_print(file_name, file_dir):
    file_found = ()
    print(f"Scanning '{(str(file_dir)).split('/')[-1]}' folder for '{(str(file_name)).split('/')[-1]}'. ")
    if (file_dir/file_name).is_file(): # to stop it printing directories 
        print(f"Found it!")
        file_found = True      
    else:
        print("Nothing found!")
        file_found = False
    return file_found
    
if scan_and_print(flicker_file_name, flicker_dir) == True:
    print("Removing the file!")
    (flicker_dir/flicker_file_name).unlink(missing_ok=True)
    print("Re-scanning.")
    scan_and_print(flicker_file_name, flicker_dir)
else:
    print("Creating the file!")
    (flicker_dir/flicker_file_name).touch()
    print("Re-scanning.")
    scan_and_print(flicker_file_name, flicker_dir)

