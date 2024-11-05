# Windows版本打包说明
要将此应用打包为 Windows 版本的 .exe 可执行文件，请按照以下步骤操作。确保您已在 Windows 环境中进行打包（Windows 系统下运行 PyInstaller）。

Windows 打包准备

	1.	进入 Windows 环境：确保在 Windows 系统中操作，因为 .exe 文件只能在 Windows 系统中生成。
	2.	安装 Python 及所需依赖：
	•	确保安装了与 Mac 版本相同的 Python 版本（例如 3.9）。
	•	使用 venv 创建一个独立的 Python 环境并激活。
	•	安装所需的依赖库：

python -m venv pa_tool_env
pa_tool_env\Scripts\activate  # 激活环境
pip install -r requirements.txt  # 安装依赖


	3.	安装 PyInstaller：

pip install pyinstaller



打包步骤

	1.	调整 Spec 文件：
	•	打开 ProctorAsst_ExcelModifier.spec 文件。
	•	修改图标路径，以适应 Windows 版本的图标（例如 .ico 格式的图标）：

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ProctorAsst_ExcelModifier',
    debug=False,
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
    icon='Asset/icon/myicon.ico',  # 修改为适用于 Windows 的 .ico 图标
)


	•	保存 .spec 文件。

	2.	使用 PyInstaller 打包：
	•	打开命令行，进入包含 ProctorAsst_ExcelModifier.spec 文件的目录。
	•	运行以下命令进行打包：

pyinstaller --clean --noconfirm ProctorAsst_ExcelModifier.spec


	3.	检查生成的文件：
	•	打包成功后，生成的 .exe 文件会出现在 dist 文件夹中，例如 dist/ProctorAsst_ExcelModifier.exe。
	4.	测试应用：
	•	双击生成的 .exe 文件，确保应用可以在 Windows 上正常运行。如果启动较慢，提醒用户等待。
	5.	发布：
	•	将 Windows 版本的 .exe 文件上传到 GitHub Releases 中，与 Mac 版本一同发布，并注明是 Windows 版本。

说明文件更新

在 README 中增加 Windows 版本的下载说明和使用步骤，并提醒用户在 Windows 系统下运行 .exe 文件。

这样操作后，您就完成了 Windows 版本的打包和发布。