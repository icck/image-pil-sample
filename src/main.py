import os
from datetime import datetime

from PIL import Image, ImageEnhance, ImageFilter

# 入力ファイルDIRと出力ファイルDIRを設定
input_dir = 'src/in'
output_dir = 'src/out'

# 入力ディレクトリが存在しない場合は作成
if not os.path.exists(input_dir):
    os.makedirs(input_dir)

# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_filename(base_filename: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_filename}_{timestamp}.png"

def save_image(image: Image.Image, directory: str, base_filename: str):
    filename = generate_filename(base_filename)
    filepath = f"{directory}/{filename}"
    image.save(filepath)
    print(f"Image saved as {filepath}")

def enhance_image_for_ocr(input_path):
    # 画像を開く
    image = Image.open(input_path)

    # 画像をグレースケールに変換
    image = image.convert('L')

    # 画像のコントラストを強調
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    # 画像をシャープ化
    image = image.filter(ImageFilter.SHARPEN)

    # 画像を保存
    save_image(image, output_dir, os.path.splitext(os.path.basename(input_path))[0])

# 入力ディレクトリ内のすべての画像を処理
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        input_path = os.path.join(input_dir, filename)
        enhance_image_for_ocr(input_path)
