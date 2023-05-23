from pathlib import Path

dirs_to_make = {}

notes_2 = Path.home()/"notes_2"
meetings_dir = notes_2/"project_one"/"meetings_notes"
fin_reports_dir = notes_2/"project_one"/"financial_reporting"

dirs_to_make["notes_2"] = notes_2
dirs_to_make["meetings_notes"] = meetings_dir
dirs_to_make["financial_reporting"] = fin_reports_dir

# directory creation
for key, value in dirs_to_make.items():
    value.mkdir(parents=True, exist_ok=True) 
    # parents=True ensures any not yet existing parts of the directory structure get created
    # exist_ok=True ensure no error if directory already exists
    
    # check directories were created
    print(f"Checking '{key}' exists: {value.exists()}")


# creating the files for Q1
Q1 = ["Jan", "Feb", "Mar"]

for month in Q1: 
    fin_report = f"{month}_financials_report.xls"
    meeting_notes = f"{month}_meeting_notes.doc"
    fin_path = fin_reports_dir/fin_report
    meet_path = meetings_dir/meeting_notes
    fin_path.touch(), meet_path.touch() 

# iterate over contents of a directory using the directories stored in the mapping dictionary 
for key, value in dirs_to_make.items():
    for item in value.iterdir():
        print(f"{item}")

# searching using Globs and `**/` for recusrion
print("\nSearching for all Word documents.")
for path in notes_2.glob("**/*.doc"):
    if path.is_file(): # to stop it printing directories 
        print(path)
    
# more searching using Globs for multiple search terms 
print("\nSearching for all Excel documents.")
excel_file_extensions = ["*xls", "*xlxs", "*xlsm", "*xltx", "*xltm"]
for ext in excel_file_extensions:
    for path in notes_2.glob(f"**/*.{ext}"):
        if path.is_file(): # to stop it printing directories 
            print(path)
        
# searching using glob and wildcards
search_pattern = "?e*"
print(f"\nSearching for {search_pattern} matching documents.")
for path in notes_2.glob(f"**/{search_pattern}"):
    if path.is_file(): # to stop it printing directories 
        print((str(path)).split('/')[-1]) # just the file names (no paths)
