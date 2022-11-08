#pip install pywhatkit
#pip install PyAudio
#pip install SpeechRecognition
#pip install gtts
#pip install playsound
#pip install beautifulsoup4
#pip install requests

import speech_recognition as speech_recognition
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound
import random
import datetime	
from bs4 import BeautifulSoup
import requests

url = "https://www.ntvhava.com/istanbul-hava-durumu"
request=requests.get(url)
html=request.content
soup=BeautifulSoup(html,"html.parser")

day=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-box-bottom-degree-big"})
night=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-box-bottom-degree-small"})
weather=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-text"})

day_=[]
night_=[]
weather_=[]
for x in day:
    x=x.text
    day_.append(x)
for y in night:
    y=y.text
    night_.append(y)
for z in weather:
    z=z.text
    weather_.append(z)

unified="İstanbul için hava raporları şöyle {} gündüz sıcaklığı {} gece sıcaklığı {} ".format(weather_[0],day_[0],night_[0])

joke_list = ["Tuvaletteki 10’a ne denir SİFON",
"Türkiye’nin en yeni şehri hangisidir NEVŞEHİR",
"Gardaş yan yana duran garlara mı deniyor",
"abi bizim ali'yi gordun mu hangi ali şehirler arasi otobus terminali",
"geçen gün kamyon sürdüm leonardo da vinci",
"adamın biri düşmüş karısı da dejavu",
"Gülen ördeğe ne denir? KIKIR-DUCK",
"Almanya’da Almanlar, Sakarya’da sakarlar yaşar",
"Adamın biri güneşte yanmış, ay da düz.",
"Ben kahve içiyorum, Nurgül Yeşilçay",
"Yağmur yağmış, kar peynir!",
"Yarasa yararlı bir hayvandır. Yararlı bir hayvan olmasaydı yaramasa derlerdi"]


def speech(text):
    print(text)
    language = "tr"
    output = gTTS(text=text, lang=language, slow=False)

    output.save(r"C:\\Users\ENES\Desktop\PROPHET\sounds\output.mp3")
    playsound(r"C:\\Users\ENES\Desktop\PROPHET\sounds\output.mp3")



def get_audio():
    recorder = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        playsound(r"C:\\Users\ENES\Desktop\PROPHET\sounds\sound.mp3")
        speech("Bir şey söyle")
        print("Bir şey söyle.....")       
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio) 
    print(f"{text}") 
    return  text


text = get_audio()

## pywhatkit.playonyt(text)
## pywhatkit.search(text)


if "merhaba" in text.lower():
    speech("Merhaba, ben yapay zekâ prophet.")
    x = datetime.datetime.now()
    speech("Bugünün tarih ve saati")
    speech(x.strftime("%c"))
    speech("Bugünün hava durumu")
    speech(unified)
    speech("Hoşça kal")
elif "marhaba" in text.lower():
    speech("Merhaba, ben yapay zekâ prophet.")
    x = datetime.datetime.now()
    speech("Bugünün tarih ve saati")
    speech(x.strftime("%c"))
    speech("Bugünün hava durumu")
    speech(unified)
    speech("Hoşça kal")
elif "youtube" in text.lower():
    speech("Tamam,youtube'dan istiyorum")
    pywhatkit.playonyt(text)
elif "espri" in text.lower():   
    speech(random.choice(joke_list))    
elif "hava" in text.lower():   
    speech(unified)  
else:
    speech("Tamam, senin için google'dan aratacağım")
    pywhatkit.search(text)


