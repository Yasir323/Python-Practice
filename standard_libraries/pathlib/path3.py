from pathlib import Path
from time import ctime
import shutil

path = Path("pathlib/path1.py")
# print(path.exists())
# path.rename("path.py")
# path.unlink()   # To delete
# print(path.stat())
print(ctime(path.stat().st_ctime))  # Creation time of the file
# print(path.read_bytes())   # read the binary data from the file
# path.read_text()    # Read the text data
# path.write_bytes()
# path.write_text()
# ------------------------------------------------------------------
# Copying a file
# ------------------------------------------------------------------
source = Path("pathlib/path1.py")
target = Path("path.py")
# target.write_text(source.read_text())
# OR
# shutil.copy(source, target)
