from pytube import YouTube
import os

def download_video(url):
  yt = YouTube(url)
  video = yt.streams.get_highest_resolution()
  video.download()

def download_audio(url):
  yt = YouTube(url)

  audio = yt.streams.filter(only_audio=True).first()

  # Télécharge au format mp4 par défaut
  download = audio.download()

  # Conversion mp4 -> mp3
  base, ext = os.path.splitext(download)
  new_file = base + '_audio.mp3'
  os.rename(download, new_file)
