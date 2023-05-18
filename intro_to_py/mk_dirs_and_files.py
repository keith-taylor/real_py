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
