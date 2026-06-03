import sys, os

# Mimic PyInstaller frozen environment
sys.frozen = True
sys._MEIPASS = os.path.dirname(os.path.abspath(__file__))

# PyInstaller's bootstrap: load crypto key and archive
from pyimod00_crypto_key import key
from pyimod01_archive import ArchiveReadError, Cipher, ZlibArchiveReader

try:
    cipher = Cipher(key)
except Exception:
    cipher = None

# Load PYZ-00.pyz as the frozen module archive
sys.path.insert(0, sys._MEIPASS)

# Execute PyInstaller bootstrap
import pyiboot01_bootstrap

# Now run the main module
import marshal
data = open(os.path.join(sys._MEIPASS, 'kT2QOz8H8O.pyc'), 'rb').read()
code = marshal.loads(data[16:])
exec(code)
