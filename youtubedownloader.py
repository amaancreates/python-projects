from pytube import YouTube
identity = input(" Please enter your name: ")
link = input(f"Enter the link {identity} : ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
input()
