<div align="center">
  <h1>🎵 Audix</h1>
  <p><b>A fast, clean, and professional command-line audio downloader built using Python and yt-dlp.</b></p>
  
  [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-Available-blue.svg)](#-license)
</div>

<br/>

Audix provides a minimal, distraction-free CLI experience for searching and downloading high-quality audio from YouTube with precise user control.

---

## ✨ Features

- 🔍 **YouTube Search**: Interactive searching with multiple selectable results.
- 📄 **Paginated Results**: Easy navigation with 6 results per page.
- 📊 **Live Progress Bar**: Real-time synced download progress bar for a seamless experience.
- 🎧 **High Quality**: Choose your preferred MP3 audio quality (`128` / `192` / `320` kbps).
- ⚙️ **Easy Configuration**: One-time initial setup for download path and audio quality, which can be reconfigured at any time.
- 💻 **Cross-Platform**: Works smoothly on Windows, Linux, and macOS.

---

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.9** or newer: [Download Python](https://www.python.org/downloads/)
- **FFmpeg**: Must be installed and available in your system's PATH. [Download FFmpeg](https://ffmpeg.org/download.html)
- **Internet Connection**: Required for searching and downloading audio data.

---

## 🚀 Installation & Usage

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/nikhilxkushwaha7/Audix.git
   cd Audix/Audix
   ```
   *(If you downloaded the code as a ZIP file, extract it and navigate via terminal to the inner folder where `audix.py` is located).*

2. **Install the required dependencies** (`yt-dlp` and `colorama`):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Audix**:
   ```bash
   python audix.py
   ```

---

## 🛠️ First Run Setup

On the first launch, Audix will prompt you to set up your preferences:
1. **Download Path**: Type the directory path where you want to save downloaded music.
2. **Audio Quality**: Select your preferred quality (`128`, `192`, or `320` kbps).

The configuration is saved locally in `conf.json` and automatically used for all future downloads.

---

## 🎮 How to Use

1. Launch Audix from your terminal using `python audix.py`.
2. Select **"1. DOWNLOAD AUDIO"** from the main menu.
3. Enter the name of the song or audio you want to search for.
4. Browse the paginated results (use `N` for the next page, `B` to go back) and select your desired track by entering its number.
5. Watch the live progress bar as the audio is downloaded directly to your configured path!

---

## ⚙️ Reconfigure Setup

At any time, you can select **"2. RECONFIGURE SETUP"** from the main menu to alter:
- Your default download path.
- Your default audio extraction quality.

*(Note: Configuration changes are instantly saved and applied).*

---

## 📜 License

See the `LICENSE` file for full usage terms and restrictions.

---

## ⚠️ Disclaimer

This tool is intended for **personal and educational use only**. 
Downloaded content remains the property of its respective owners. Users are responsible for complying with local laws and platform terms of service.

---

## 🧑‍💻 Author

**Nikhil Kushwaha**

---
<div align="center">
  <i>Made with ❤️ for music and the command line.</i>
</div>
