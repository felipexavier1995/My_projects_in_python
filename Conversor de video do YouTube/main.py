# Importações necessarias para realização do programa.
from pytube import YouTube, streams
from pytube.cli import on_progress

# 1° Passo é a varivel que vai receber o link do youtube.
link = input("Link do video do youtube: ")

# 2° Passo é a variavel que recebe a função de processo de download
# Esse processo vai ser apresentado para o usuário final.
Yt = YouTube(link, on_progress_callback = on_progress)

#  3° Passo é o nome do do video e o print de 'download' em andamento.
print("Titulo = ", Yt.title)
print("Processando download...")

#  4° passo é apenas uma para varivel que vai fazer o armazenamento no diretorio e vai sempre fazer o download em alta resolução.
Ys = Yt.streams.get_highest_resolution()
Ys.download()