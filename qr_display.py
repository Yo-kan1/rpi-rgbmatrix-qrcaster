import os
import time
import qrcode
from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from dotenv import load_dotenv

def generate_qr_for_matrix(url, matrix_size=64, scale=2):
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=1, border=0)
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="white", back_color="black").convert('RGB')
    qr_w, qr_h = img_qr.size
    scaled_w, scaled_h = qr_w * scale, qr_h * scale
    img_qr_scaled = img_qr.resize((scaled_w, scaled_h), resample=Image.NEAREST)
    canvas = Image.new('RGB', (matrix_size, matrix_size), (0, 0, 0))
    offset_x = (matrix_size - scaled_w) // 2
    offset_y = (matrix_size - scaled_h) // 2
    canvas.paste(img_qr_scaled, (offset_x, offset_y))
    return canvas

def main():
    # .env ファイルを読み込む
    load_dotenv()
    
    TARGET_URL = os.getenv("TARGET_URL", "https://example.com")

    # --- LEDマトリクスの設定 ---
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    options.brightness = 7
    options.gpio_slowdown = 9
    options.drop_privileges = False
    
    matrix = RGBMatrix(options=options)

    print(f"Generating QR Code for: {TARGET_URL}")
    image_to_display = generate_qr_for_matrix(TARGET_URL)
    matrix.SetImage(image_to_display)

    print("QR Code is now displayed. Press CTRL-C to exit.")

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
