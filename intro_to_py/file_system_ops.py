import pathlib

pathlib.Path("/home/keith/Documents/Code/path_test.txt")

my_home = (pathlib.Path.home())

# print(pathlib.Path.cwd())

paths_to_check = {}
files_to_check = {}

paths_to_check['check_path_1'] = my_home/"Documents"/"code"/"real_py"
paths_to_check['check_path_2'] = my_home/"Documents"/"code"/"real_python"

files_to_check['check_file_1'] = pathlib.Path.home()/"Documents"/"code"/"path_test.txt"
files_to_check['check_file_2'] = pathlib.Path.home()/"Documents"/"code"/"silvia_path_test.txt" 


for key, value in paths_to_check.items():
    print (f"Checking {key}: {value} is a valid directory: {value.is_dir()}")

for key, value in files_to_check.items():
    print (f"Checking {key}: {value} is a valid file: {value.is_file()}")
    
f = pathlib.Path.home()/"hello.txt"
print(f"f is: {f})")
print(f"f.parent is: {f.parent})")
for i in f.parents:
    print([i])

print(f"File name: {f.name}")
print(f"File stem: {f.stem}")
print(f"File suffix: {f.suffix}")