import sys, os, marshal, traceback

# PyInstaller frozen environment
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"[run.py] base_dir={base_dir}")
print(f"[run.py] sys.path[0]={sys.path[0] if sys.path else '?'}")
print(f"[run.py] frozen={getattr(sys, 'frozen', False)}")

try:
    # Load and run the main obfuscated module
    pyc_path = os.path.join(base_dir, 'kT2QOz8H8O.pyc')
    print(f"[run.py] Loading {pyc_path} ({os.path.getsize(pyc_path)} bytes) ...")
    with open(pyc_path, 'rb') as f:
        header = f.read(16)
        code = marshal.loads(f.read())
    print(f"[run.py] Executing main module ...")
    # PyArmor needs __file__ set to the real module path to find obfuscated files
    # Save original, set to pyc path, exec, then restore
    _orig_file = globals().get('__file__')
    globals()['__file__'] = pyc_path
    exec(code)
    if _orig_file:
        globals()['__file__'] = _orig_file
except Exception as e:
    print(f"\n[FATAL] {type(e).__name__}: {e}")
    traceback.print_exc()
    input("\nPress Enter to exit...")
