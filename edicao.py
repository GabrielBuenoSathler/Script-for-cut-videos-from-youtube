#!/usr/bin/env python3
from pytube import YouTube
from  moviepy.editor import *

#passa o link do video para baixar
link = input("Digite o link:  ")


youtube_video_url = link

#baixa o video
try:
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    #faz o download do video com a maior qualidade
    arquivo = input ("nome do arquivo : ")
    filters.get_highest_resolution().download(output_path='/home/niko', filename=arquivo)
    print('Video baixado')
except Exception as e:
    print(e)

#video
clip = VideoFileClip(arquivo)
duration = clip.duration

#tempo de video
print("Duraçao : " + str(duration))

#clip.subclip em secundos (s_começa,s_termina)
comeco = float(input('digite o começo do corte: '))


fim = float(input('digite o fim do corte: '))




clip = clip.subclip(comeco,fim)
#gera o corte

clip.write_videofile("corte.mp4")  
clip.ipython_display(width = 360) 
