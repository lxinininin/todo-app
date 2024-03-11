import glob

# it will grab all the files which in ../files directory and put their names in a List
myfiles = glob.glob("../files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())