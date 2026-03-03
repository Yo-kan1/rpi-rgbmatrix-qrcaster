# RPi Matrix QR Display
[![English](https://img.shields.io/badge/Language-English-blue)](#english) [![日本語](https://img.shields.io/badge/Language-日本語-red)](#japanese)

![Demo](docs/demo.gif) ---

<a id="english"></a>
## 🇬🇧 English

A Python script to dynamically generate and display QR codes on a 64x64 RGB LED matrix using a Raspberry Pi. 

### 🌟 Features
- Dynamically generates QR codes from any URL or text.
- Optimized display for 64x64 LED matrices (e.g., 2x2 pixel scaling for precise readability).
- Adjustable brightness to prevent camera glare and ensure reliable scanning.

### 🛠 Hardware Requirements
- Raspberry Pi (e.g., Raspberry Pi 3/4)
- 64x64 RGB LED Matrix Panel
- Adafruit RGB Matrix Bonnet for Raspberry Pi

### 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install qrcode Pillow
   ```
   *(Note: Ensure the `rpi-rgb-led-matrix` library bindings are also installed/configured in your environment).*

### 💡 Usage

Run the script. Since driving the LED matrix via GPIO requires root privileges, use the Python executable inside your virtual environment with `sudo`:

```bash
sudo venv/bin/python qr_display.py
```

### 🔍 Troubleshooting & Optimization
- **Scanning Issues (Glare):** LED matrices are extremely bright. To prevent whiteout on smartphone cameras, the script lowers the brightness (e.g., 20-30%).
- **Scaling:** A standard URL generates a Version 3 QR code (29x29 cells). Scaling each cell to 2x2 pixels results in a 58x58 pixel image, perfectly centering on the 64x64 matrix with a scannable 3-pixel margin.

---

<a id="japanese"></a>
## 🇯🇵 日本語

Raspberry Piを使用して、64x64のRGB LEDマトリクスにQRコードを動的に生成・表示するPythonスクリプトです。

### 🌟 特徴
- 任意のURLやテキストから動的にQRコードを生成。
- 64x64のLEDマトリクスに最適化された表示（読み取り精度を上げるための2x2ピクセルスケーリング）。
- カメラの白飛びを防ぎ、確実なスキャンを可能にする輝度調整機能。

### 🛠 必要なハードウェア
- Raspberry Pi (例: Raspberry Pi 3/4)
- 64x64 RGB LEDマトリクスパネル
- Adafruit RGB Matrix Bonnet for Raspberry Pi

### 🚀 インストールとセットアップ

1. **リポジトリをクローン:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **仮想環境（venv）の作成と有効化:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **依存ライブラリのインストール:**
   ```bash
   pip install qrcode Pillow
   ```
   *(注: 環境に合わせて `rpi-rgb-led-matrix` ライブラリのセットアップも行ってください)*

### 💡 使い方

スクリプトを実行します。GPIO経由でLEDマトリクスを制御するにはroot権限が必要なため、`sudo` と共に仮想環境内のPythonを指定して実行します。

```bash
sudo venv/bin/python qr_display.py
```

### 🔍 トラブルシューティングと最適化（工夫した点）
- **白飛び対策:** LEDマトリクスは非常に明るいため、スマホカメラでの白飛びを防ぐべく輝度を20〜30%に抑えてスキャン成功率を向上させています。
- **スケーリングと余白:** 一般的なURL（バージョン3、29x29セル）を表示する際、1セルを2x2ピクセルで描画することで58x58ピクセルに拡大。64x64パネルの中央に配置することで、読み取りに必須な3ピクセルの余白（クワイエットゾーン）を確保しています。

---
## 📄 License
This project is licensed under the MIT License.
