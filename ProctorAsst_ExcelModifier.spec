# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['MacOS/excel_modifier_tool.py'],
    pathex=['/path/to/PA_EXCELMODIFIER_TOOL'],  # 项目根目录路径
    binaries=[],
    datas=[('Asset/icon/myicon.icns', 'icon/myicon.icns')],  # 图标文件
    hiddenimports=['pandas', 'openpyxl'],  # 添加动态导入的模块
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ProctorAsst_ExcelModifier',
    debug=True,  # 启用调试模式
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Asset/icon/myicon.icns',
)
app = BUNDLE(
    exe,
    name='ProctorAsst_ExcelModifier.app',
    icon='Asset/icon/myicon.icns',
    bundle_identifier="vulcan626@foxmail.com",  # 唯一的标识符
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'CFBundleExecutable': 'ProctorAsst_ExcelModifier'
    }
)

