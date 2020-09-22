from pathlib import Path

Path(r"C:\Program Files\Microsoft")
# The double backslash is an escape sequence so we oughta use raw string.
Path("usr/local/bin")
Path()  # This object represents cwd
Path("path1.py")
# we can cobine paths with paths and with strings as well
Path.home() / "mystuff" / "python/standard_libraries/pathlib" / Path("path1.py")
#--------------------------------------------------------------------------------
# Methods:
# -------------------------------------------------------------------------------
path = Path.home() / "mystuff" / "python/standard_libraries/pathlib" / Path("path1.py")
print(Path.home())
print(path.exists())   # Whether the path exists or not
print(path.is_file)
print(path.is_dir)
print(path.name)    # Filename + extension
print(path.stem)    # Filename
print(path.suffix)  # Extension
print(path.parent)
path = path.with_name("file.txt")   # We only created a file path object file is not created
print(path.absolute())
path = path.with_suffix(".py")  # To change the extension
#---------------------------------------------------------------------------------
path1 = Path("tutorial")
path1.exists()
path1.mkdir()
path1.rmdir()
path1.rename("tutorial2")
