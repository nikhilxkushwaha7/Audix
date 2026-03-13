<div align="center">

# 🎵 AUDIX 

**The Ultimate Command-Line Experience for Audio Downloading**

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![yt-dlp](https://img.shields.io/badge/Powered_by-yt--dlp-FF0000.svg?style=for-the-badge&logo=youtube)](https://github.com/yt-dlp/yt-dlp)
[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg?style=for-the-badge)](#license)
[![Terminal](https://img.shields.io/badge/CLI-Distraction_Free-black.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)](#features)

*Search, select, and download high-quality audio directly from your terminal. No ads, no web interfaces—just pure, uninterrupted music.*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) 

</div>

---

## ✨ Features

Audix isn't just a wrapper; it's a carefully crafted CLI environment designed for speed and simplicity.

| 🚀 Fast & Fluid | 🎧 High Quality | 🛠️ Fully Customizable |
| :--- | :--- | :--- |
| **Search on the fly:** Interactive YouTube search with multiple results. | **Multiple Bitrates:** Choose from `128kbps`, `192kbps`, or `320kbps` MP3 output. | **Setup Once:** Configure your download directory and preferred quality on the first run. |
| **Wait-free:** Paginated results (6 per page) let you browse effortlessly. | **FFmpeg Powered:** Perfect audio extraction every time. | **Easy Reconfig:** Change your settings anytime via the main menu. |
| **Live Tracking:** Beautiful, real-time download progress bar. | **Metadata:** Clean filenames and properly extracted audio. | **Cross-Platform:** Works identically on Windows, macOS, and Linux. |

---

## ⚡ Quick Start

### Prerequisites
Make sure you have [**Python 3.9+**](https://www.python.org/downloads/) installed, and that [**FFmpeg**](https://ffmpeg.org/download.html) is available in your system's `PATH`.

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Audix.git
cd Audix/Audix

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Audix
python audix.py
```

---

## 🎮 How It Works

<details open>
<summary><b>1. First-Run Setup ⚙️</b></summary>
<br>
When you run Audix for the first time, it will guide you through a quick setup:
<ul>
  <li>Enter the <b>absolute path</b> to your music folder.</li>
  <li>Select your preferred audio quality.</li>
</ul>
<i>Your preferences are saved locally in <code>conf.json</code>.</i>
</details>

<details open>
<summary><b>2. Searching & Downloading 🔍</b></summary>
<br>
<ul>
  <li>Select <b>"DOWNLOAD AUDIO"</b> from the main menu.</li>
  <li>Type your search query (e.g., <i>"lofi hip hop radio"</i>).</li>
  <li>Navigate pages using <code>N</code> and <code>B</code>.</li>
  <li>Type the number of the track you want, and watch the progress bar!</li>
</ul>
</details>

<details>
<summary><b>3. Reconfiguration 🔄</b></summary>
<br>
Need to change your download folder? Just select <b>"RECONFIGURE SETUP"</b> from the main menu at any time. Updates take effect immediately.
</details>

---

## 🖼️ Application Preview

*(The terminal interface uses beautiful `colorama`-powered Cyan and White text prompts for a visually pleasing, cyberpunk-esque vibe.)*

```text
 ────────────────────────────────────
   █████╗ ██╗   ██╗██████╗ ██╗██╗  ██╗
  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██╔╝
  ███████║██║   ██║██║  ██║██║ ╚███╔╝ 
  ██╔══██║██║   ██║██║  ██║██║ ██╔██╗ 
  ██║  ██║╚██████╔╝██████╔╝██║██╔╝ ██╗
  ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
 ────────────────────────────
   HIGH-QUALITY AUDIO DOWNLOADER
```

---

## 📜 License & Disclaimer

- **Disclaimer:** Audix is intended for **personal and educational use only**. Downloaded content remains the property of its respective owners. Please respect creators' rights and comply with local laws and platform terms of service.
- **License:** See the `LICENSE` file for usage conditions.

---

<div align="center">
  <b>Built with ❤️ by Nikhil Kushwaha</b>
  <br><br>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00FFFF&height=100&section=footer" width="100%"/>
</div>
