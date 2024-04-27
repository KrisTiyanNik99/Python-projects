import tkinter
import customtkinter
from pytube import YouTube

# Add needed defs
# First def is for download a video when "download_btn" is clicked
def download_Video():
    # Message for our user to know is the video is successfully downloaded or not
    is_downloaded = ''
    
    # Try to download the video
    try:
        # Url where we want to save videos
        saved_file_url = r"C:\Users\Christian\Desktop\Python projects\Third Project\Downloaded_videos"
        
        # Get the url from "link" field and parsed to YouTube object
        yt_link = yt_url.get()
        yt_Object = YouTube(yt_link, on_progress_callback=progress_response)
        yt_video = yt_Object.streams.get_highest_resolution()
        notification_message.configure(text='')
        
        # Download video
        yt_video.download(saved_file_url)
        is_downloaded = f"Successfully Downloaded {yt_video.title} Video!"
        color_text = 'green'
    except Exception as e:
        # Print with red letters our exception
        color_text = 'red'
        is_downloaded = f"An error occurred: {str(e)}"
        
        # Reset progress bar and text above him
        percentage_label.configure(text="0%")
        progress_bar.set(0)
    # Message in the end
    notification_message.configure(text=is_downloaded, text_color=color_text)

# Second def is for progressing bar when the video is download
def progress_response(stream, chunks, remain_bytes):
    # Get file size
    total_size = stream.filesize
    
    # Get how many bytes we need are download
    downloaded_bytes = total_size - remain_bytes
    complete_downloaded_percentage = downloaded_bytes / total_size * 100
    
    # Turn percentage into a string
    percentage_text = str(int(complete_downloaded_percentage)) + "%"
    percentage_label.configure(text=percentage_text)
    percentage_label.update()
    
    # Update progress bar
    progress_bar.set(float(complete_downloaded_percentage) / 100)

# App Gui settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Main setting on our frame
frame = customtkinter.CTk()
frame.geometry("720x480")
frame.title("YouTube Downloader")

# Add GUI elements
title = customtkinter.CTkLabel(frame, text="Insert your YouTube link here:")
title.pack(padx=10, pady=10)

# Link bar and inputs
yt_url = tkinter.StringVar()
link = customtkinter.CTkEntry(frame, width=350, height=40, textvariable=yt_url)
link.pack()

# Notification message
notification_message = customtkinter.CTkLabel(frame, text="")
notification_message.pack()

# Progress percentage label and progress bar
percentage_label = customtkinter.CTkLabel(frame, text="0%")
percentage_label.pack()
progress_bar = customtkinter.CTkProgressBar(frame, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Add "download" button
download_btn = customtkinter.CTkButton(frame, text="Download", command=download_Video)
download_btn.pack(padx=10, pady=10)

# Run app
frame.mainloop()