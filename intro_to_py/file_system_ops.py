import pathlib

pathlib.Path("/home/keith/Documents/Code/path_test.txt")

my_home = (pathlib.Path.home())
print(my_home)

print(pathlib.Path.cwd())