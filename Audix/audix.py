# ======================================
# AUDIX - PREMIUM CLI AUDIO DOWNLOADER
# AUTHOR: NIKHIL K
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

# ---------- CONFIG ----------
CONFIG_FILE = "conf.json"

DEFAULT_CONFIG = {
    "download_path": "DOWNLOADS",
    "audio_quality": "192"
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)

config = load_config()
os.makedirs(config["download_path"], exist_ok=True)

# ---------- UI ----------
def slow_print(text, delay=0.01):
    for ch in text:
        sys.stdout.write(MUTED + ch.upper())
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ---------- BANNER ----------
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

# ---------- PROGRESS ----------
def progress_hook(d):
    if d.get("status") == "downloading":
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        if total:
            percent = int(d.get("downloaded_bytes", 0) * 100 / total)
            bar = "█" * (percent // 3) + "░" * (30 - percent // 3)
            sys.stdout.write(f"\r{ACCENT}[{bar}] {percent}%")
            sys.stdout.flush()
    elif d.get("status") == "finished":
        sys.stdout.write(f"\r{ACCENT}[{'█'*30}] 100%")
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
        res = ydl.extract_info(f"ytsearch{(page+1)*6}:{query}", download=False)
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
    slow_print("2. SETUP / CONFIG")
    slow_print("3. ABOUT")
    slow_print("4. EXIT")

def setup_menu():
    slow_print("1. CHANGE DOWNLOAD PATH")
    slow_print("2. CHANGE AUDIO QUALITY")
    slow_print("3. CHECK CURRENT CONFIG")
    slow_print("4. BACK")

def show_config():
    banner()
    slow_print("CURRENT CONFIGURATION\n")
    slow_print(f"DOWNLOAD PATH : {config['download_path']}")
    slow_print(f"AUDIO QUALITY : {config['audio_quality']} KBPS")
    input("\nPRESS ENTER TO GO BACK")

def about():
    clear_terminal()
    slow_print("AUDIX V1.0")
    slow_print("PREMIUM CLI AUDIO DOWNLOADER")
    input("\nPRESS ENTER TO GO BACK")

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
        while True:
            banner()
            setup_menu()
            sub = input("\nSELECT OPTION: ").strip()

            if sub == "1":
                path = input("ENTER NEW DOWNLOAD PATH: ").strip()
                if path:
                    config["download_path"] = path
                    os.makedirs(path, exist_ok=True)
                    save_config(config)
                    print(SUCCESS + "DOWNLOAD PATH UPDATED")
                    time.sleep(1)

            elif sub == "2":
                q = input("ENTER AUDIO QUALITY (128/192/320): ").strip()
                if q in ["128", "192", "320"]:
                    config["audio_quality"] = q
                    save_config(config)
                    print(SUCCESS + "AUDIO QUALITY UPDATED")
                    time.sleep(1)

            elif sub == "3":
                show_config()

            elif sub == "4":
                break

    elif choice == "3":
        about()

    elif choice == "4":
        clear_terminal()
        slow_print("SESSION CLOSED")
        break
