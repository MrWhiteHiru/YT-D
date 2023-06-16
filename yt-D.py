import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from PIL import ImageTk, Image

window = tk.Tk()

def download_video():
    video_url = url_entry.get()
    save_path = filedialog.askdirectory()
    
    try:
        yt = YouTube(video_url)
        stream = yt.streams.first()
        stream.download(save_path)
        status_label.config(text="Download successful!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")



window.geometry("800x500")
window.resizable(False, False)
window.title("YOUTUBE Downloader [basic program]")
window.configure(background="#1c1e3d")


status_label = tk.Label(window, text="""
⠀⠀⢀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣹⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀
⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠁⠀
⠀""",bg="#1c1e3d", fg="red" )
status_label.pack()


title_label = tk.Label(window, text="""YOUTUBE DOWNLOADER""", font=("Arial", 23, "bold", "italic"), fg="#696fc9", bg="#1c1e3d")
title_label.pack()
tex = tk.Label(window, text="""                                                               By Mr WHITE HIRU
                                                                                   @ HISL""", font=("Arial", 11, "italic"), fg="#5fc964", bg="#1c1e3d")
tex.pack()
url_label = tk.Label(window, text="Video URL:", bg="#1c1e3d", fg="white",font=("Arial", 12, "bold", "italic"))
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack(pady=3)


# Create download button
download_button = tk.Button(window, text="Download", command=download_video, bg="#1c1e3d", fg="white",font=("Arial", 12, "bold", "italic"))
download_button.pack(pady=20)

# Create status label
status_label = tk.Label(window, text="", bg="#1c1e3d", fg="white",font=("Arial", 12, "bold", "italic"))
status_label.pack()

title_label.pack(pady=30)
window.mainloop()