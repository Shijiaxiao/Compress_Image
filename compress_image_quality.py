from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):

    try:
        with Image.open(input_path) as img:
            # 如果输出路径的扩展名为.jpg，则保存为JPEG格式，否则保存为PNG格式
            if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
                img.save(output_path, "JPEG", quality=quality)
            else:
                img.save(output_path, "PNG", optimize=True, quality=quality)
    except Exception as e:
        print(f"压缩图像时发生错误：{str(e)}")

# 输入图像路径（HEIC或PNG格式）
input_image_path = "1.png"

# 输出图像路径（PNG或JPEG格式）
output_image_path = "output1.png"  # 或者设置为 "output.png"

input_image_path2 = "output1.png"
output_image_path2 = "output2.png"  # 或者设置为 "output.png"
# 调整quality参数来控制压缩质量
compress_image(input_image_path, output_image_path, quality=1)
# compress_image(input_image_path2, output_image_path2, quality=10)
