import sys, os, marshal, traceback

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, base_dir)
sys._MEIPASS = base_dir

print(f"[run.py] base_dir={base_dir}")

try:
    # Step 1: Run PyInstaller bootstrap to set up frozen import system
    # This installs FrozenImporter for PYZ-00.pyz modules (PyQt5, numpy, etc.)
    with open(os.path.join(base_dir, 'pyiboot01_bootstrap.pyc'), 'rb') as f:
        bootstrap = marshal.loads(f.read()[16:])
    exec(bootstrap)

    # Step 2: Load and run the main obfuscated module
    pyc_path = os.path.join(base_dir, 'kT2QOz8H8O.pyc')
    print(f"[run.py] Loading {pyc_path} ...")
    with open(pyc_path, 'rb') as f:
        code = marshal.loads(f.read()[16:])

    main_mod = sys.modules['__main__']
    main_mod.__dict__['__file__'] = pyc_path

    print(f"[run.py] Executing main module ...")
    exec(code, main_mod.__dict__)
except Exception as e:
    print(f"\n[FATAL] {type(e).__name__}: {e}")
    traceback.print_exc()
    input("\nPress Enter to exit...")
