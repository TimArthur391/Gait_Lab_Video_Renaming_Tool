# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['cli.py'],
             pathex=[],
             binaries=[],
             datas=[('scrpt/*.py', 'scrpt'), ('helpers/*.*','helpers'), ('helpers/imageio', 'imageio'), ('requirements.txt', '.'), ('LICENSE', '.')],
             hiddenimports=['PIL', 'mysql-connector-python', 'imageio_ffmpeg', 'tk', 'tkinter', 'tkinter.filedialog'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Video_Renaming_Tool_V1.5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='helpers/Camcorder_Pro_icon-icons.com_54204.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Video_Renaming_Tool_V1.5')
