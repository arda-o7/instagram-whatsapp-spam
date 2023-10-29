#gerekli kütüphaneleri kuruyoruz
import pyautogui
import time

#Spam iletilere yönelik işlevi tanımlayın
def spam_messages(message, number_of_messages):
    #Gönderilecek mesaj sayısını yineleyin
    for i in range(number_of_messages):
        pyautogui.typewrite(message)
        #Enter tuşuna basın
        pyautogui.press('enter')
        #1 saniye bekleme süresi
        time.sleep(1)

spam_messages("Hello, How Are You", 10)
# "" içine yazmak istedğiniz mesajı giriniz.
#10 yazan kısımada kaç adet mesaj atmak istiyorsunuz girniz.