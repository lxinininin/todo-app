filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentations.txt"]

for filename in filenames:
    # we can not use the filename[1] = '-' directly, because filename is a String which is immutable
    # if we use filename = filename.replace('.', '-')
    # filename will be "1- Raw Data-txt", all the '.' will be replaced in '-'
    filename = filename.replace('.', '-', 1)
    print(filename)