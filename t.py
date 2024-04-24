import tkinter as tk
from tkinter import filedialog
from PIL import Image
import io

def convert_jpg_to_bytearray():
    """将选中的JPG图片转换成Bytearray并显示出来。"""
    # 选择图片文件
    img_path = filedialog.askopenfilename(title="选择图片", filetypes=[("JPG图片", "*.jpg")])
    if not img_path:
        return

    # 读取图片并转换为灰度图
    try:
        img = Image.open(img_path).convert('1')
    except Exception as e:
        error_label.config(text=f"错误：{e}")
        return

    # 获取图片尺寸并缩放到指定大小
    x, y = 40, 40
    img_resize = img.resize((x, y))

    # 将图片数据保存到字节流中
    buf = io.BytesIO()
    img_resize.save(buf, 'ppm')
    byte_im = buf.getvalue()

    # 获取Bytearray数据
    temp = len(str(x) + ' ' + str(y)) + 4
    bytearray_data = byte_im[temp::]

    # 更新文本框内容
    try:
        bytearray_text_box.delete(1.0, tk.END)
        bytearray_text_box.insert(tk.END, bytearray_data.decode('gb2312'))
    except UnicodeDecodeError:
        # Handle the decoding error (e.g., display a message)
        error_label.config(text="解码错误！请尝试其他图片。")  # Example error message in Chinese

# 创建主窗口
root = tk.Tk()
root.title("JPG转Bytearray")

# 选择图片按钮
select_button = tk.Button(root, text="选择图片", command=convert_jpg_to_bytearray)
select_button.pack(pady=10)

# 错误信息标签
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=5)

# Bytearray数据文本框
bytearray_text_box = tk.Text(root, width=40, height=10)
bytearray_text_box.pack(pady=5)

# 运行主窗口
root.mainloop()
