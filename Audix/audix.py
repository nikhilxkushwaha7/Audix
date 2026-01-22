# ======================================
# AUDIX - CLI AUDIO DOWNLOADER
# AUTHOR: NIKHIL KUSHWAHA
# ======================================

import yt_dlp
import os
import sys
import time
import json
from colorama import init, Fore, Style

# ---------- INIT ----------
init(autoreset=True)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# ---------- SILENT LOGGER ----------
class SilentLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

# ---------- COLORS ----------
ACCENT = Fore.CYAN + Style.BRIGHT
MUTED = Fore.WHITE + Style.BRIGHT
SUCCESS = Fore.CYAN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT

# ---------- UI ----------
def slow_print(text, delay=0.01):
    for ch in text:
        sys.stdout.write(MUTED + ch.upper())
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ---------- SETUP BANNER ----------
def setup_banner():
    clear_terminal()
    width = os.get_terminal_size().columns

    art = [
        " ███████╗███████╗████████╗██╗   ██╗██████╗ ",
        " ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗",
        " ███████╗█████╗     ██║   ██║   ██║██████╔╝",
        " ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ ",
        " ███████║███████╗   ██║   ╚██████╔╝██║     ",
        " ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ",
    ]

    print("\n")
    for line in art:
        print(ACCENT + line.center(width))

    print(ACCENT + ("─" * 36).center(width))
    slow_print("INITIAL CONFIGURATION\n")

# ---------- CONFIG ----------
CONFIG_FILE = "conf.json"

DEFAULT_CONFIG = {
    "download_path": "",
    "audio_quality": ""
}

def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG.copy()
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

config = load_config()

# ---------- SETUP ----------
def setup_config():
    setup_banner()

    while True:
        path = input(
            "\nTYPE THE PATH WHERE YOU WANT TO SAVE DOWNLOADED MUSIC:\n> "
        ).strip()
        if path:
            break
        print(ERROR + "PATH CANNOT BE EMPTY")

    while True:
        quality = input(
            "\nSELECT AUDIO QUALITY (128 / 192 / 320):\n> "
        ).strip()
        if quality in ["128", "192", "320"]:
            break
        print(ERROR + "INVALID QUALITY")

    config["download_path"] = path
    config["audio_quality"] = quality

    os.makedirs(path, exist_ok=True)
    save_config(config)

    print(SUCCESS + "\nSETUP COMPLETED SUCCESSFULLY\n")
    time.sleep(1)

# ---------- AUTO SETUP CHECK ----------
if not config.get("download_path") or not config.get("audio_quality"):
    setup_config()

# ---------- MAIN BANNER ----------
def banner():
    clear_terminal()
    width = os.get_terminal_size().columns

    art = [
        "   █████╗ ██╗   ██╗██████╗ ██╗██╗  ██╗",
        "  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██╔╝",
        "  ███████║██║   ██║██║  ██║██║ ╚███╔╝ ",
        "  ██╔══██║██║   ██║██║  ██║██║ ██╔██╗ ",
        "  ██║  ██║╚██████╔╝██████╔╝██║██╔╝ ██╗",
        "  ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝",
    ]

    print("\n")
    for line in art:
        print(ACCENT + line.center(width))

    print(ACCENT + ("─" * 28).center(width))
    print(MUTED + "HIGH-QUALITY AUDIO DOWNLOADER".center(width))
    print("\n")

# ---------- PROGRESS BAR ----------
def progress_hook(d):
    if d.get("status") == "downloading":
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        downloaded = d.get("downloaded_bytes", 0)

        if total:
            percent = int(downloaded * 100 / total)
            bar_len = 30
            filled = int(bar_len * percent / 100)
            bar = "█" * filled + "░" * (bar_len - filled)

            sys.stdout.write(
                f"\r{ACCENT}[{bar}] {percent}%"
            )
            sys.stdout.flush()

    elif d.get("status") == "finished":
        sys.stdout.write(
            f"\r{ACCENT}[{'█' * 30}] 100%"
        )
        sys.stdout.flush()

# ---------- SEARCH ----------
def search_youtube(query, page):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
        "logger": SilentLogger()
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info(
            f"ytsearch{(page+1)*6}:{query}", download=False
        )

    return res.get("entries", [])[page*6:(page*6)+6]

def search_and_select(query):
    page = 0

    while True:
        results = search_youtube(query, page)
        if not results:
            print(ERROR + "NO MORE RESULTS")
            time.sleep(1)
            return None

        banner()
        main_menu()
        slow_print(f"\nSEARCH RESULTS — PAGE {page+1}\n")

        for i, r in enumerate(results, 1):
            slow_print(f"{i}. {r['title'].upper()}")

        slow_print("\nN. NEXT PAGE")
        slow_print("B. BACK")

        choice = input("\nSELECT OPTION: ").strip().upper()

        if choice == "B":
            return None
        if choice == "N":
            page += 1
            continue
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            return results[int(choice)-1]["url"]

# ---------- DOWNLOAD ----------
def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "logger": SilentLogger(),
        "progress_hooks": [progress_hook],
        "outtmpl": f"{config['download_path']}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": config["audio_quality"]
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n" + SUCCESS + "DOWNLOAD SUCCESSFUL\n")

# ---------- MENUS ----------
def main_menu():
    slow_print("1. DOWNLOAD AUDIO")
    slow_print("2. RECONFIGURE SETUP")
    slow_print("3. EXIT")

# ---------- MAIN ----------
while True:
    banner()
    main_menu()
    choice = input("\nSELECT OPTION: ").strip()

    if choice == "1":
        while True:
            banner()
            main_menu()
            query = input("\nENTER SONG NAME (B = BACK): ").strip().upper()

            if query == "B":
                break
            if not query:
                continue

            url = search_and_select(query)
            if url:
                download_audio(url)

    elif choice == "2":
        setup_config()

    elif choice == "3":
        clear_terminal()
        slow_print("SESSION CLOSED")
        break
