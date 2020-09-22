from pathlib import Path
from zipfile import ZipFile

#---------------------------------------------------------------
# Creating a zip file:
#---------------------------------------------------------------
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("pathlib").rglob("*.*"):
#         zip.write(path)
# The above statements create a zip file named files.zip
# in cwd and add all the files in the pathlib directory to that
# zip file
#---------------------------------------------------------------
# Reading a zip file
#---------------------------------------------------------------
with ZipFile("files.zip") as zip:
    print(zip.namelist())   # List all the files inside the zip file
    info = zip.getinfo("pathlib/path2.py")
    # The above statement creates an info object with has all the
    # information about the named file
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract_directory")
    # This line extracts the files.zip into the a new directory
    # whose name is specified in the argument
