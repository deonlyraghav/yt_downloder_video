# importing the module
from pytube import YouTube

# where to save
save_path = "Downloads"

# link of the video to be downloaded
link = input("enter the link of the video to be download: ")

try:
# object creation using YouTube
# which was imported in the beginning
    yt = YouTube(link)
except:
    print("connection error!!") #to handle exception

print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))
print(yt.streams.filter(progressive=True))

ys = yt.streams.get_highest_resolution()

try:
    # downloading the video
    ys.download()
    # ys.download(save_path)
except:
    print("error!!")

print("task completed")