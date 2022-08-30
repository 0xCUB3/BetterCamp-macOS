# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['BetterCamp_Assistant.command'],
             pathex=['src'],
             binaries=[],
             datas=[('resources', 'resources')],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='BetterCamp Assistant',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
app = BUNDLE(exe,
         name='BetterCamp Assistant.app',
         icon="resources/Bootcamp_Assistant.icns",
         bundle_identifier="ga.0xCUBE.bettercamp_assistant",
         info_plist={
             "CFBundleShortVersionString": "0.0.1",
             "CFBundleExecutable": "MacOS/Terminal",
             "NSHumanReadableCopyright": "Copyright © 2022 0xCUBE",
         })