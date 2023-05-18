import pathlib


file_path = pathlib.Path.home()/"my_folder"/"myfile.txt"

if file_path.is_dir():
    print(f"{file_path} is an existing directory. ")
else:    
    print(f"Warning! {file_path} is not an existing directory. ")

print(f"The name of the file is: {file_path.name}")
print(f"The name of the parent directory is: {file_path.parents[1]}")

for i in file_path.parents:
    print(i)



