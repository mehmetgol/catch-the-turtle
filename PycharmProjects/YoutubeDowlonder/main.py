import pytube
import os

url = input(" enter  video  url ")

name_of_file = "yotube videos "

os.makedirs(name_of_file, exist_ok=True)
path = r"C:/kulanıcılar\mehmet emre göl\Pycharm Projects\YoutubeDowlonder\youtube videos"

pytube.YouTube(url).streams.get_highest_resolution().download(path)



