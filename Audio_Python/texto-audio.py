from gtts import gTTS
from playsound import playsound

audio02  = 'testando123.mp3'
languagePT = 'pt-br'

######
audio01    = 'text.mp3'
language = 'pt-br'

voice01 = gTTS(
    text = 'Arquivo para teste... sou bem vindo ao mundo agora !',
    lang = language
)

voice01.save(audio01)
playsound(audio01)