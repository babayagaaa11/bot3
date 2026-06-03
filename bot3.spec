# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

# Get all files in current dir that need to be bundled
root = Path('.').absolute()
binaries = []
datas = []
hiddenimports = []

# Collect all pyc files
for f in sorted(root.glob('*.pyc')):
    datas.append((str(f.relative_to(root)), '.'))

# Collect all pyd files
for f in sorted(root.glob('*.pyd')):
    binaries.append((str(f.relative_to(root)), '.'))

# Collect all pyz files
for f in sorted(root.glob('*.pyz')):
    datas.append((str(f.relative_to(root)), '.'))

# Collect all dll files
for f in sorted(root.glob('*.dll')):
    binaries.append((str(f.relative_to(root)), '.'))

# Collect all zip files
for f in sorted(root.glob('*.zip')):
    datas.append((str(f.relative_to(root)), '.'))

# Collect directory packages
for d in ['PyQt5', 'PySide2', 'cv2', 'Crypto', 'numpy', 'PIL', 'frida', 'capstone',
          'certifi', 'cryptography', 'psutil', 'aiohttp', 'yaml', 'yarl', 'zope',
          'win32com', 'frozenlist', 'multidict', 'propcache', 'setuptools', 'wheel',
          'pywin32_system32', 'shiboken2', 'tk', 'tcl', 'tcl8',
          'importlib_metadata-4.11.4.dist-info', 'attrs-25.3.0.dist-info',
          'cryptography-42.0.5.dist-info', 'setuptools-69.2.0.dist-info',
          'wheel-0.43.0.dist-info', 'pyinjector']:
    p = root / d
    if p.exists():
        datas.append((str(p.relative_to(root)), d))

a = Analysis(
    ['kT2QOz8H8O.pyc'],
    pathex=[str(root)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='godkiss1_patched',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlement_file=None,
)
