from pytube import YouTube
from pytube import Playlist

def progress_respond(stream, chunks, bytes_remaining):
    
    remaining = stream.filesize
    other = (bytes_remaining / remaining) * 100
    sum = int(other)
    print(f"{sum} bytes remaining...")

yt = YouTube(
    'http://youtube.com/watch?v=2lAe1cqCOXo')
video = yt.streams.get_highest_resolution()
video.download()

pty = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

print("This is!")
#for video in pty.videos:
    #print(video)
    #video.streams.first().download()