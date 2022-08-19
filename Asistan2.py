from bs4 import BeautifulSoup
import datetime
import requests
from selenium.webdriver.firefox.service import Service
import random
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By



r = sr.Recognizer()
class SesliAsistan():

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang="tr")
        file="file"+str(random.randint(0,54865485484654))+".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)

    def sesKaydedici(self):
        with sr.Microphone() as seskaynak:
            listen = r.listen(seskaynak)
            voice=" "
            while voice==" ":
                try:
                    voice = r.recognize_google(listen, language="tr-TR")
                except:
                    self.text_to_speech("ne söylediğinizi anlayamadım, tekrar eder misiniz?")
                    listen = r.listen(seskaynak)
            else:
                return voice

    def SesliYanit(self, new_input):
        if "selam" in new_input:
            self.text_to_speech("selam, nasıl yardımcı olabilirim?")

        elif "merhaba" in new_input:
            self.text_to_speech("merhaba, nasıl yardımcı olabilirim?")

        elif "nasılsın" in new_input:
            self.text_to_speech("iyiyim, siz nasılsınız?")

        elif "video aç" in new_input or "youtube'u aç" in new_input or "şarkı aç" in new_input:
            try:
                self.text_to_speech("aradığınız içerik adı nedir?")
                data = self.sesKaydedici()
                self.text_to_speech("{} açılıyor".format(data))
                time.sleep(1)
                url="https://www.youtube.com/results?search_query={}".format(data)
                firefox_driver_path = "C:\\Users\\bosta\OneDrive\\Masaüstü\\SesliAsistan\\geckodriver.exe"
                s = Service(firefox_driver_path)
                tarayici = webdriver.Firefox(service=s)
                tarayici.get(url)  
                try:
                    button = tarayici.find_element(By.XPATH, "*//*[@id='video-title']/yt-formatted-string").click()
                except:
                    self.text_to_speech("böyle bir içerik bulunamadı")
            except:
                self.text_to_speech("İnternetten kaynaklı bir hata meydana geldi. Lütfen internet bağlantınızı kontrol edin.")
        
        
        elif "arama motorunu aç" in new_input or "arama yap" in new_input:
            try:
                self.text_to_speech("Ne aramamı istersiniz?")
                data = self.sesKaydedici()
                self.text_to_speech("{} için bulduğum sonuçlar bunlar".format(data))
                url = "https://www.google.com/search?q={}".format(data)
                firefox_driver_path = "C:\\Users\\bosta\OneDrive\\Masaüstü\\SesliAsistan\\geckodriver.exe"
                s = Service(firefox_driver_path)
                tarayici = webdriver.Firefox(service=s)
                tarayici.get(url)  
            except:
                self.text_to_speech("İnternetten kaynaklı bir hata meydana geldi. Lütfen internet bağlantınızı kontrol edin.")
        

        elif "tarayıcıyı kapat" in new_input:
            try:
                self.text_to_speech("tarayıcı kapatılıyor.")
                firefox_driver_path = "C:\\Users\\bosta\OneDrive\\Masaüstü\\SesliAsistan\\geckodriver.exe"
                s = Service(firefox_driver_path)
                tarayici = webdriver.Firefox(service=s)
                tarayici.close()
                tarayici.quit()
            except:
                self.text_to_speech("tarayıcı zaten kapalı.")

        elif "hava durumu" in new_input or "hava durumu tahmini" in new_input:

            try:

                self.text_to_speech("hangi şehrin hava durumunu istersiniz")
                cevap=self.sesKaydedici()

                url = "https://www.ntvhava.com/{}-hava-durumu".format(cevap)
                request = requests.get(url)
                html_icerigi = request.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                gunduz_sicakliklari = soup.find_all("div",
                                                    {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
                gece_sicakliklari = soup.find_all("div",
                                                    {"class": "daily-report-tab-content-pane-item-box-bottom-degree-small"})
                hava_durumlari = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})

                gun_isimleri = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-date"})

                gunduz = []
                gece = []
                hava = []
                gunler = []

                for x in gunduz_sicakliklari:
                    x = x.text
                    gunduz.append(x)
                for y in gece_sicakliklari:
                    y = y.text
                    gece.append(y)
                for z in hava_durumlari:
                    z = z.text
                    hava.append(z)

                for a in gun_isimleri:
                    a = a.text
                    a = a[0:3:]
                    if (a == "Cmt"):
                        a = "Cumartesi"
                    elif (a == "Paz"):
                        a = "Pazar"
                    elif (a == "Pzt"):
                        a = "Pazartesi"
                    elif (a == "Sal"):
                        a = "Salı"
                    elif (a == "Çar"):
                        a = "Çarşamba"
                    elif (a == "Per"):
                        a = "Perşembe"
                    elif (a == "Cum"):
                        a = "Cuma"
                    gunler.append(a)

                self.text_to_speech("{} şehiri için günlük , yarının ya da 5 günlük hava raporlarını mı istersiniz".format(cevap))
                print(cevap)
                cevap2=self.sesKaydedici()

                if(cevap2=="bugünün" or cevap2=="günlük"):
                    saat=datetime.now().strftime("%H:%M")
                    if(saat<="17:00"):
                        self.text_to_speech("{} için hava durumu bugün şöyle: {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap,hava[0],gunduz[0],gece[0]))
                    else:
                        self.text_to_speech("{} için hava durumu bu akşam şöyle: {} gece sıcaklığı :{}".format(cevap,hava[0],gece[0]))

                elif(cevap2=="yarın" or cevap2=="yarınınki" or cevap2=="ertesi günün"):
                    self.text_to_speech("{} için yarın hava durumu şöyle: {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap,hava[1],gunduz[1],gece[1]))

                elif(cevap2=="beş günlük" or cevap2=="haftalık"):
                    saat=datetime.now().strftime("%H:%M")
                    if(saat<="17:00"):
                        self.text_to_speech("{} için hava durumu bugün şöyle: {} gündüz sıcaklığı {} gece sıcaklığı: {}"
                                        "yarın {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                        "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                        "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                        "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap,hava[0],gunduz[0],gece[0],hava[1],gunduz[1],gece[1],gunler[2],hava[2],gunduz[2],gece[2],gunler[3],hava[3],gunduz[3],gece[3],gunler[4],hava[4],gunduz[4],gece[4]))

                    else:
                        self.text_to_speech("{} için hava durumu bugün şöyle: {} gece sıcaklığı: {}"
                                            "yarın {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                            "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                            "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                            "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap, hava[0],
                                                                                                    gece[0],
                                                                                                    hava[1], gunduz[1],
                                                                                                    gece[1], gunler[2],
                                                                                                    hava[2], gunduz[2],
                                                                                                    gece[2], gunler[3],
                                                                                                    hava[3], gunduz[3],
                                                                                                    gece[3], gunler[4],
                                                                                                    hava[4], gunduz[4],
                                                                                                    gece[4]))
            except:
                self.text_to_speech("istediğinz şehre göre bir içerik bulunamadı.lütfen istediğinz şehri veya internetinizi kontrol ediniz")






asistan = SesliAsistan()




while True:
    ses = asistan.sesKaydedici()
    if(ses!= " "):
        ses=ses.lower()
        print(ses)
        asistan.SesliYanit(ses)
        