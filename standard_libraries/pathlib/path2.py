from pathlib import Path
path = Path.home() / "mystuff/python/standard_libraries"
print(path.exists())
print(path.iterdir())   # Generator object, so we can iterate over it
# for p in path.iterdir():
#     print(p)
paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(py_files)
# To search recursively:
# py_files = [p for p in path.glob("**/*.py")]
# OR
# py_files = [p for p in path.rglob("*.py")]
