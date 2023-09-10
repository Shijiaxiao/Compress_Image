from PIL import Image
import os

def compress_image(input_path, output_path, target_size_kb):
    try:
        with Image.open(input_path) as img:
            quality = 85  # 初始压缩质量
            while os.path.getsize(output_path) > target_size_kb * 1024 and quality > 10:
                # 逐渐降低压缩质量，直到文件大小小于目标大小
                img.save(output_path, "PNG", optimize=True, quality=quality)
                quality -= 5
    except Exception as e:
        print(f"压缩图像时发生错误：{str(e)}")

# 输入图像路径（HEIC或PNG格式）
input_image_path = "1.png"
# 输出图像路径（PNG或JPEG格式）
output_image_path = "/Users/shijiaxiao/Desktop/compress_image/2.png"  # 或者设置为 "output.png"
# 目标文件大小（以KB为单位）
target_size_kb = 800
# 调整quality参数以控制压缩质量
compress_image(input_image_path, output_image_path, target_size_kb)
