import shutil

# it will zip all the files which included in ../files directory
shutil.make_archive("output", "zip", "../files")