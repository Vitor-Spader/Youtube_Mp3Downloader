import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

def download_mp3_from_youtube(url, output_path):
    # Define the yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    # Download and convert the video to mp3
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def browse_output_path():
    output_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

def start_download():
    url = url_entry.get()
    output_path = output_path_entry.get()

    if not url or not output_path:
        messagebox.showerror("Error", "Please provide all the required inputs.")
        return

    try:
        download_mp3_from_youtube(url, output_path)
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube to MP3 Downloader")

# Create and place the widgets
tk.Label(root, text="YouTube URL").grid(row=0, column=0, padx=10, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Save to").grid(row=1, column=0, padx=10, pady=5)
output_path_entry = tk.Entry(root, width=50)
output_path_entry.grid(row=1, column=1, padx=10, pady=5)
output_path_button = tk.Button(root, text="Browse", command=browse_output_path)
output_path_button.grid(row=1, column=2, padx=10, pady=5)

download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=3, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()