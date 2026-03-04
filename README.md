# RPi Matrix QR Display
[![English](https://img.shields.io/badge/Language-English-blue)](#english) [![日本語](https://img.shields.io/badge/Language-日本語-red)](#japanese)

![Demo](docs/demo.gif) ---

<a id="english"></a>
## 🇬🇧 English

A Python script to dynamically generate and display QR codes on a 64x64 RGB LED matrix using a Raspberry Pi. 

### 🌟 Features
- Dynamically generates QR codes from any URL or text.
- Optimized display for 64x64 LED matrices (2x2 pixel scaling for precise readability).
- External configuration via `.env` to keep URLs and sensitive data secure.

### 🛠 Hardware Requirements
- Raspberry Pi (e.g., Raspberry Pi 3/4)
- 64x64 RGB LED Matrix Panel
- Adafruit RGB Matrix Bonnet for Raspberry Pi

### 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install qrcode Pillow python-dotenv
   ```
   *(Note: Ensure the `rpi-rgb-led-matrix` library bindings are also installed/configured in your environment).*

### 💡 Usage
Create a `.env` file in the project root and add your target URL:
```text
TARGET_URL="[https://your-url-here.com](https://your-url-here.com)"
```

Run the script using `sudo` with the virtual environment's Python:
```bash
sudo venv/bin/python qr_display.py
```

### 🔍 Troubleshooting & Ingenuity
- **Flicker & Glare Mitigation:** Direct scanning via smartphone cameras was initially difficult due to severe LED flicker and glare. By extensively tuning the software parameters to `gpio_slowdown = 9` and `brightness = 7`, I found the optimal sweet spot to minimize visual noise.
- **Operational Workaround:** Since real-time scanning was limited by hardware PWM constraints, I established a reliable workflow: taking a still photo of the LED matrix with a smartphone and scanning the QR code from the captured image.

### 🚧 Future Challenges (Next Steps)
- **Achieving Direct Real-time Scanning:** To completely eliminate flickering and allow direct scanning with a QR reader app, I plan to perform the "Hardware PWM Mod" on the Adafruit Bonnet (soldering GPIO 4 to 18). Once modified, updating the software to utilize `options.parallel = 1` and `adafruit-hat-pwm` mapping should resolve the issue entirely.

---

<a id="japanese"></a>
## 🇯🇵 日本語

Raspberry Piを使用して、64x64のRGB LEDマトリクスにQRコードを動的に生成・表示するPythonスクリプトです。

### 🌟 特徴
- 任意のURLやテキストから動的にQRコードを生成。
- 64x64のLEDマトリクスに最適化された表示（読み取り精度を上げるための2x2ピクセルスケーリング）。
- 環境変数（`.env`）による設定の外部化に対応。URLなどの機密情報を安全に管理。

### 🛠 必要なハードウェア
- Raspberry Pi (例: Raspberry Pi 3/4)
- 64x64 RGB LEDマトリクスパネル
- Adafruit RGB Matrix Bonnet for Raspberry Pi

### 🚀 インストールとセットアップ

1. **リポジトリをクローン:**
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name
   ```

2. **仮想環境（venv）の作成と有効化:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **依存ライブラリのインストール:**
   ```bash
   pip install qrcode Pillow python-dotenv
   ```
   *(注: 環境に合わせて `rpi-rgb-led-matrix` ライブラリのバインディングもセットアップしてください)*

### 💡 使い方
プロジェクトのルートに `.env` ファイルを作成し、表示したいURLを記述します。
```text
TARGET_URL="[https://your-url-here.com](https://your-url-here.com)"
```

GPIO経由でLEDマトリクスを制御するため、`sudo` と共に仮想環境内のPythonを指定して実行します。
```bash
sudo venv/bin/python qr_display.py
```

### 🔍 工夫した点（トラブルシューティング）
- **白飛びとフリッカー対策:** スマホでの直接読み取りを試みた際、LEDのPWM制御とカメラのシャッタースピードが干渉し、強烈なシマシマ模様（フリッカー）が発生しました。ソフトウェア側で `gpio_slowdown = 9`, `brightness = 7` と極限までパラメータをチューニングし、最もノイズの少ないスイートスポットを発見しました。
- **運用による確実な読み取り:** 動画モード（QRリーダー）での直接スキャンは現状のハードウェア制約上困難だったため、「一度スマホのカメラで静止画として撮影し、その写真からQRコードを読み取る」という運用フローを確立。これにより、安定したスキャンが可能になりました。

### 🚧 今後の課題（Next Steps）
- **リアルタイムの直接スキャンの実現:** Adafruit Bonnetの基板裏面にあるGPIO 4と18をショートさせる「PWM mod（ハードウェアPWM化）」を施すことが今後の目標です。この物理的なハックと、ソフトウェア側の `options.parallel = 1` などを組み合わせることでフリッカーを完全に除去し、カメラ越しのリアルタイム読み取りを実現したいと考えています。

---
## 📄 License
This project is licensed under the MIT License.