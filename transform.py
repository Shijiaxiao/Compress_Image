# from PIL import Image

# def convert_heic_to_png(input_path, output_path):
#     """
#     将HEIC格式的照片转换为PNG格式。

#     参数：
#     input_path (str): 输入HEIC图像文件的路径。
#     output_path (str): 输出PNG图像的路径。
#     """
#     try:
#         with Image.open(input_path) as img:
#             img.save(output_path, "PNG")
#         print(f"{input_path} 已成功转换为 {output_path}")
#     except Exception as e:
#         print(f"转换图像时发生错误：{str(e)}")

# # 输入HEIC图像路径
# input_image_path = "images/1.heic"
# # 输出PNG图像路径
# output_image_path = "images/output.png"
# # 调用转换函数
# convert_heic_to_png(input_image_path, output_image_path)



import cv2

def convert_heic_to_png(input_path, output_path):
    """
    将HEIC格式的照片转换为PNG格式。

    参数：
    input_path (str): 输入HEIC图像文件的路径。
    output_path (str): 输出PNG图像的路径。
    """
    try:
        # 使用OpenCV读取HEIC图像
        img = cv2.imread(input_path)
        # 使用OpenCV保存为PNG图像
        cv2.imwrite(output_path, img)
        print(f"{input_path} 已成功转换为 {output_path}")
    except Exception as e:
        print(f"转换图像时发生错误：{str(e)}")

# 输入HEIC图像路径
input_image_path = "images/1.heic"
# 输出PNG图像路径
output_image_path = "images/output.png"
# 调用转换函数
convert_heic_to_png(input_image_path, output_image_path)
