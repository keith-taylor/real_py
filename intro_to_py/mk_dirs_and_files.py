from pathlib import Path

dirs_to_make = {}

notes_2 = Path.home()/"notes_2"
meetings_dir = notes_2/"project_one"/"meetings_notes"
reports_dir = notes_2/"project_one"/"reporting"

dirs_to_make["notes_2"] = notes_2
dirs_to_make["meetings_notes"] = meetings_dir
dirs_to_make["reporting"] = reports_dir

# directory creation
for key, value in dirs_to_make.items():
    value.mkdir(parents=True, exist_ok=True)
    # check directories were created
    print(f"Checking '{key}' is an existing directory: {value.exists()}")

    