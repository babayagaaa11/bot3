import sys, os, marshal

# PyInstaller frozen environment
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Load and run the main obfuscated module
pyc_path = os.path.join(base_dir, 'kT2QOz8H8O.pyc')
with open(pyc_path, 'rb') as f:
    header = f.read(16)  # skip Python 3.9 magic header
    code = marshal.loads(f.read())
exec(code)
