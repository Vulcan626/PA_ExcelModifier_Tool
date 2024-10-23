import os
import pandas as pd
from tkinter import Tk, Button, Label, filedialog, messagebox

# 定义处理Excel的函数
def process_excel(file_path):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path, header=None)
        
        # 检查H1单元格是否为 "副监考教师"
        if df.iloc[0, 7] == "副监考教师":
            # 修改为 "副监考教师1"
            df.iloc[0, 7] = "副监考教师1"
            
            # 获取原文件名
            base_name = os.path.basename(file_path)
            new_file_name = f"Modified_{base_name}"
            save_path = os.path.join(os.path.dirname(file_path), new_file_name)
            
            # 保存修改后的文件
            df.to_excel(save_path, index=False, header=False)
            messagebox.showinfo("成功", f"文件已成功修改并保存为: {new_file_name}")
        else:
            messagebox.showwarning("警告", "H1单元格内容不是 '副监考教师'")
    except Exception as e:
        messagebox.showerror("错误", f"处理文件时发生错误: {e}")

# 定义上传文件的函数
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        process_excel(file_path)

# 创建UI
def create_ui():
    root = Tk()
    root.title("监考信息表格处理工具")
    root.geometry("300x200")
    
    # 标题
    label_title = Label(root, text="监考信息表格处理工具", font=("Helvetica", 16))
    label_title.pack(pady=10)
    
    # 上传按钮
    button_upload = Button(root, text="上传文件", command=upload_file)
    button_upload.pack(pady=10)
    
    # 退出按钮
    button_exit = Button(root, text="退出", command=root.quit)
    button_exit.pack(pady=10)

    # 版本信息
    label_version = Label(root, text="Version: v1.0.1", font=("Helvetica", 10))
    label_version.pack(side="bottom", pady=1)

    # # 联系信息
    # label_contact = Label(root, text="Email: vulcan626@foxmail.com", font=("Helvetica", 10))
    # label_contact.pack(pady=1)
    
    root.mainloop()

# 启动应用
if __name__ == "__main__":
    create_ui()

