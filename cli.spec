# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['cli.py'],
             pathex=[],
             binaries=[],
             datas=[('scrpt/*.py', 'scrpt'), ('installation_file_TEST.bat', '.'), ('installation_file.bat', '.'), ('log.txt', '.'), 
                    ('Camcorder_Pro_icon-icons.com_54204.ico', '.'), ('application_information.JSON', '.'), ('SQLQueries.sql', '.'),
                    ('pyinstaller_text.txt', '.'), ('update_version_log_in_db.py', '.'), ('requirements.txt', '.'), ('imageio', 'imageio')],
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
          name='Video_Renaming_Tool_V1.4',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='Camcorder_Pro_icon-icons.com_54204.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Video_Renaming_Tool_V1.4')
