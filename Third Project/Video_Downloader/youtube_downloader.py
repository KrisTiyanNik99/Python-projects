import tkinter
import tkinter.filedialog as filedialog
import customtkinter
from pytube import YouTube

is_resolution_check = False

# Add needed defs
# Get resolutions method
def get_resolutions(yt_Object):
    # Get the YouTube object
    stream_yt_object = yt_Object.streams
    
    resolutions = set()
    # Loop through all available variations
    for resolution in stream_yt_object:
        # Take a resolution and add it to the "set"
        res = resolution.resolution
        
        # If we had no resolution entry - skip
        if res == None:
            continue
        resolutions.add(res)
    # Return the "set"
    return resolutions

# Choose resolution method
def take_resolution():
    global is_resolution_check
    # Try to get video link
    try:
        yt_link = yt_url.get()
        yt_obj = YouTube(yt_link)
        yt_resolutions = get_resolutions(yt_Object=yt_obj)
        resolution_menu.configure(values=yt_resolutions)
        
        # Turn "is_resolution_check" to True
        is_resolution_check = True
    except Exception as e:
        notification_message.configure(text=e)

# First def is for download a video when "download_btn" is clicked
def download_Video():
    global is_resolution_check
    
    # Color of the message text
    color_text = ''
    
    # Try to download the video
    try:
        # Checking if the resolution options of the current URL link are provided
        if is_resolution_check:
            # Url where we want to save videos
            saved_file_path = filedialog.askdirectory()
            downloaded_location.configure(text="")
            
            # Get the url from "link" field and parsed to YouTube object
            yt_link = yt_url.get()
            yt_Object = YouTube(yt_link, on_progress_callback=progress_response)
        
            # Get value from drop down menu with resolutions
            resolution = resolution_menu.get()
            print(resolution)
            
            # Check for chosen option
            if resolution == "None":
                yt_video = yt_Object.streams.get_lowest_resolution()
            elif resolution == "" or resolution == None:
                yt_video = yt_Object.streams.get_audio_only()
            else:
                yt_video = yt_Object.streams.filter(res=resolution).first()
                if yt_video == None:
                    yt_video = yt_Object.streams.get_highest_resolution()
                print(yt_video)
            notification_message.configure(text='')
            
            # Download video
            yt_video.download(saved_file_path)
            is_downloaded = f"Successfully Downloaded {yt_video.title} Video!"
            
            # Message settings
            color_text = 'green'
            downloaded_location.configure(text=f"Video is downloaded in: {saved_file_path}", text_color=color_text)
            
            # Reset "is_resolution_check" to False
            is_resolution_check = False
        else:
            is_downloaded = f"Get a resolutions first from 'Get Resolution' button!"
            color_text= "red"
    except Exception as e:
        # Print with red letters our exception
        color_text = 'red'
        is_downloaded = f"An error occurred: {str(e)}"
        downloaded_location.configure(text="Video Error!", text_color=color_text)
        
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
# Convert frame with title
convert_frame = customtkinter.CTkFrame(frame)
convert_frame.pack(pady=5, padx=5)

# Set title
title = customtkinter.CTkLabel(convert_frame, text="Insert your YouTube link here:")
title.pack(padx=10, pady=10)

# Link bar and inputs
yt_url = tkinter.StringVar()
link = customtkinter.CTkEntry(convert_frame, width=350, height=40, textvariable=yt_url)
link.pack(side="left")

# Button convert
convert_btn = customtkinter.CTkButton(convert_frame, text="Get Resolution", command=take_resolution)
convert_btn.pack(side="left")

# Drop down menu title
drop_menu_text = customtkinter.CTkLabel(frame, text="Choose resolution")
drop_menu_text.pack(padx=10, pady=10)

# Drop down menu with available resolutions and text
resolution_menu = customtkinter.CTkComboBox(frame, values=["None"], width=300, height=40)
resolution_menu.pack()

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

# Add file location
downloaded_location = customtkinter.CTkLabel(frame, text="")
downloaded_location.pack(padx=10, pady=10)

# Run app
frame.mainloop()