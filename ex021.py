from pygame import init, mixer, event
init()
mixer.music.load('music.mp3')
mixer.music.play()
event.wait() #faz esperar a música terminar para terminar o programa

#o arquivo de música deve ser copiado para a pasta do projeto


