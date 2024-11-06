# Proctor Assistant Excel Modifier

**README Last Updated**: 2024-11-06

**Developer**: Vulcan626

---

**[English Version](#application-overview)** | **[中文说明](#应用概述)**

---

## Application Overview

**Proctor Assistant Excel Modifier** is a tool designed for exam proctors to modify specific content in Excel files. Its primary function is to automatically replace the content in the **H1 cell** from "副监考教师" to "副监考教师1". This tool provides an intuitive and easy-to-use interface for users to upload, process, and download modified Excel files efficiently. Available for both macOS and Windows.

---

## Features

- Automatically detects and modifies "副监考教师" in cell H1 to "副监考教师1".
- Supports Excel file upload, content processing, and file download in one workflow.
- Saves the modified file as `Modified_<OriginalFileName>.xlsx`.
- Compatible with both macOS and Windows, featuring a user-friendly interface.

---

## How to Use

### macOS

1. **Download and Extract**:
   - Download the macOS version from the [GitHub Releases](https://github.com/your-repo-url/releases).
   - Unzip the downloaded file `ProctorAsst_ExcelModifier_v1.0.1_Mac.zip` to access the `.app` file.

2. **Run the Application**:
   - **Double-click** the `ProctorAsst_ExcelModifier.app` file to open the application.
   - If the app doesn’t open directly, you may need to open it via Terminal:
     1. Open Terminal.
     2. Use the `cd` command to navigate to the directory containing `ProctorAsst_ExcelModifier.app`:
        ```bash
        cd /path/to/your/app/folder
        ```
     3. Run the following command to start the app:
        ```bash
        ./ProctorAsst_ExcelModifier.app/Contents/MacOS/ProctorAsst_ExcelModifier
        ```

3. **Be Patient**:
   - **Note**: The app may take a few seconds to launch. Please wait patiently after running the command.

### Windows

1. **Download and Extract**:
   - Download the Windows version from the [GitHub Releases](https://github.com/your-repo-url/releases).
   - Unzip the downloaded file `ProctorAsst_ExcelModifier_v1.0.1_Windows.zip` to access the `.exe` file.

2. **Run the Application**:
   - **Double-click** the `ProctorAsst_ExcelModifier.exe` file to open the application.
   - If the app doesn’t open or you encounter warnings:
     - Right-click `ProctorAsst_ExcelModifier.exe` and select **Run as Administrator**.
     - Alternatively, open Command Prompt, navigate to the directory, and run:
       ```cmd
       ProctorAsst_ExcelModifier.exe
       ```

3. **Be Patient**:
   - **Note**: The app may take a few seconds to initialize. Please wait patiently.

---

## Download

- The latest version of the application can be found in the [Releases](https://github.com/Vulcan626/PA_ExcelModifier_Tool/releases/tag/v1.0.1).
- Download the file labeled `ProctorAsst_ExcelModifier_v1.0.1_Mac.zip` for macOS and `ProctorAsst_ExcelModifier_v1.0.1_Windows.zip` for Windows.

---

## Contact

For any questions or support, please reach out to the developer at **vulcan626@foxmail.com**.

---

## Version Timeline

| Version | Release Date   | Notes                                                   |
| ------- | -------------- | ------------------------------------------------------- |
| v1.0.0  | 2024-10-10     | Initial release for macOS.                              |
| v1.0.1  | 2024-10-24     | Added macOS terminal instructions and improved stability.|
| v1.0.1  | 2024-11-06     | Synchronized macOS and Windows release.                 |

---

## License

This project is licensed under the **MIT License**. For more details, refer to the `LICENSE` file or the following:

```text
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

---

# Proctor Assistant Excel Modifier

---

## 应用概述

**Proctor Assistant Excel Modifier** 是为监考人员设计的工具，用于修改 Excel 文件中的特定内容。该工具的主要功能是自动将 **H1 单元格**中的“副监考教师”替换为“副监考教师1”。它适用于 macOS 和 Windows，为用户提供了上传、处理和下载修改后 Excel 文件的简便接口。

---

## 功能特点

- 自动检测并将 H1 单元格中的“副监考教师”修改为“副监考教师1”。
- 支持 Excel 文件上传、内容处理和文件下载一体化流程。
- 修改后的文件将保存为 `Modified_<原文件名>.xlsx`。
- 支持 macOS 和 Windows 系统，提供简洁友好的用户界面。

---

## 使用说明

### macOS

1. **下载与解压**：
   - 从 [GitHub Releases](https://github.com/Vulcan626/PA_ExcelModifier_Tool/releases) 页面下载 macOS 版本。
   - 解压 `ProctorAsst_ExcelModifier_v1.0.1_Mac.zip`，获得 `.app` 文件。

2. **运行应用**：
   - **双击** `ProctorAsst_ExcelModifier.app` 文件以打开应用。
   - 如果无法直接打开应用，请通过终端运行：
     1. 打开终端。
     2. 使用 `cd` 命令进入包含 `ProctorAsst_ExcelModifier.app` 的目录，例如：
        ```bash
        cd /path/to/your/app/folder
        ```
     3. 运行以下命令启动应用：
        ```bash
        ./ProctorAsst_ExcelModifier.app/Contents/MacOS/ProctorAsst_ExcelModifier
        ```

3. **耐心等待**：
   - **提示**：应用启动可能需要几秒钟，请耐心等待。

### Windows

1. **下载与解压**：
   - 从 [GitHub Releases](https://github.com/Vulcan626/PA_ExcelModifier_Tool/releases) 页面下载 Windows 版本。
   - 解压 `ProctorAsst_ExcelModifier_v1.0.1_Windows.zip`，获得 `.exe` 文件。

2. **运行应用**：
   - **双击** `ProctorAsst_ExcelModifier.exe` 文件以打开应用。
   - 如果无法打开应用或遇到警告，请尝试以下方法：
     - 右键点击 `ProctorAsst_ExcelModifier.exe` 并选择 **以管理员身份运行**。
     - 或者，打开命令提示符，进入包含 `ProctorAsst_ExcelModifier.exe` 的文件夹，输入：
       ```cmd
       ProctorAsst_ExcelModifier.exe
       ```

3. **耐心等待**：
   - **提示**：应用启动可能需要几秒钟，请耐心等待。

---

## 下载

- 应用的最新版本可以在 [Releases](https://github.com/Vulcan626/PA_ExcelModifier_Tool/releases/tag/v1.0.1) 页面找到。
- 请确保下载 `ProctorAsst_ExcelModifier_v1.0.1_Mac.zip` 适用于 macOS 或 `ProctorAsst_ExcelModifier_v1.0.1_Windows.zip` 适用于 Windows 系统。

---

## 联系方式

如有任何问题或需要支持，请联系开发者：**vulcan626@foxmail.com**

---

## 版本时间线

| 版本    | 发布日期         | 更新说明                                      |
| ------- | ---------------- | --------------------------------------------- |
| v1.0.0  | 2024-10-10       | （macOS）首次发布版本。                       |
| v1.0.1  | 2024-10-24       | （macOS）新增了终端运行说明并提升稳定性。      |
| v1.0.1  | 2024-11-06       | 同步发布 Windows 版本，更新 macOS 版本。      |

---

## 许可证

本项目采用 **MIT License** 许可。有关更多信息，请参阅 `LICENSE` 文件

或以下内容：

```text
MIT License

特此授予获得本软件及相关文档文件（“软件”）的任何人无限制处理软件的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件的副本，并允许软件所属人这样做，条件是上述版权声明和本许可声明应包含在软件的所有副本或主要部分中。

该软件按“现有”的基础提供，没有任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、适用于特定用途和不侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权行为或其他方面，均因本软件或使用或其他交易中的软件的相关内容而产生。
```