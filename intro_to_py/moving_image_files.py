
from pathlib import Path

search_dir = Path.home()/"Documents"/"code"/"real_py"/"intro_to_py"/"practice_files"
destination_dir = search_dir/"images"
destination_dir.mkdir(exist_ok = True)

img_file_extensions = [".png", ".gif", ".jpg", ".jpeg"]

for file_ext in img_file_extensions:
    for path in search_dir.glob(f"**/*{file_ext}"):
            if path.is_file():
                #print(destination_dir/(str(path)).split('/')[-1])
                path.replace(destination_dir/(str(path)).split('/')[-1])

