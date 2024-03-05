##piszemy w cmd
# cd Desktop\
# cd TinderBot\
# dir
# ...
# python TinderBot.py
# ...
#(owiera sie strona internetowa Tinder)
#logujemy sie a w tym czasie cos tam nam pisze w terminalu
#jak polubimyy kogos wyswietla sie nam info otej osobie
#gdy bot przesuwa w prawo zeby robil ss ekranu co kogo polubil'
#zeby wylaczyc to narzedzie wystarczy kliknac CTRL+C
#zdjecia zapisuja sie w folderze cmd (repozytorium)
#robimy to w Spider(Python 3.8)
#time.sleep - czasem strona nie zdazy zaladowac sie do konca a system juz szuka tego gużika
#uzywamy spacza nie HTML 
#trzeba zainstalowac xPath Finder i klikamy na stronie Tinder wyrazam zgode i mamy informacje zwrotną jaki to jest xPath
#musi byc zainstalowany python
#musi byc zainstalowany silenium (pip install selenium)
#w folderze Tinder na laptopie musi byc (chromedriver, READMI(z googla),Readmi (z obrazem READMI),TinderBOT (notatki),user(notatki))
from selenium import webdriver
import time 

class TinderBot():
    def __init__(self):
        self.browser = webdriver.Chrome()
    def login(self):
        print('Author = [Artur Danyliv] ')
        time.sleep(0.5)
        print('GitHub = https://github.com/PSZMAJ')
        time.sleep(0.5)
        print('Youtube = https://www.youtube.com/channel/UCewT7Lr5F6LWvqSPXmOJKRw')
        time.sleep(0.5)
        print('TinderBot.py ver 1.0')
        time.sleep(0.5)
        print('Login with data with facebook')

        login =input('Hi , type Your mail: ')
        time.sleep(0.5)
        password = input('Hi type Your password: ')
        self.browser.get('https://tinder.com/')
        print(self.browser.title)
        time.sleep(4)

        ### ---> Find akcept button and click
        self.button_agreed = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button/span') #albo spam
        self.button_agreed.click()
        time.sleep(1)

        ### ---> Login with Facebook account
        self.buttonLoginWithFacebook = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button/span')
        self.buttonLoginWithFacebook.click()
        time.sleep(1)

        ### ---> Change windows to login with Facebook
        self.base_window = self.browser.window_handles[0]
        time.sleep(1)
        self.browser.switch_to_window(self.browser.window_handles[1])
        time.sleep(1)

        ### ---> Find password form , provide password and click
        self.facebookPassword = self.browser.find_element_by_xpath('//*[@id - "pass"]')
        time.sleep(1.5)
        self.facebookPassword.click()
        time.sleep(1.5)
        self.facebookPassword.send_keys(password)
        time.sleep(1.5)

        ### ---> Find password form,prvide password and click
        self.facebookPassword = self.browser.find_element_by_xpath('//*[@id - "pass"]')
        time.sleep(1.5)
        self.facebookPassword.click()
        time.sleep(1.5)
        self.facebookPassword.send_keys(password)
        time.sleep(1.5)

        ### ---> Find button 'logon' and cklick 
        self.facebookLoginButton = self.browser.find_element_by_xpath('//*[@id - "u_0_0"]')
        time.sleep(1.5)
        self.facebookLoginButton.click()
        time.sleep(1.5)
        self.browser.switch_to_window(self.browser.window_handles[0])
        time.sleep(2)

        ### ---> Allow Tinder Localization
        time.sleep(2)
        self.tinderAllowButton = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        time.sleep(1.5)
        self.tinderAllowButton.click()
        time.sleep(3)

        ### ---> Allow Tinder notification
        self.tinderAllowNotification = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        time.sleep(1.5)
        self.tinderAllowNotification.click()
        time.sleep(1.5)

        time.sleep(1.5)
        time.sleep(1.5)

        ### ---> show and download information about person
    def like(self):
        time.sleep(0.5)
        self.information_Person = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]...')
        self.indoAge_Person = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]...')
        self.infoMoreAbout_Person = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]...')
        #pobiera wiecej informacij z profilu danej osoby
        self.getPhoto = self.browser.get_screenshot_as_file(self.infoName_Person.text + ".png") #robi na ss pobiera zdjecie osoby
        print('-------------------------------------------------------------------------------------------------------------------------------------------')
        print('Imie polubionej osoby to : ',self.infoName_Person.text ," wiek ",self.infoAge_Person.text )
        print(('Informacje z profilu : ',self.infoMoreAbout_Person.text.replace("\n"," ")))
        print('-------------------------------------------------------------------------------------------------------------------------------------------')
        self.buttonLikePerson = self.browser.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div[1]/div/div/div[1]/div/div[2]/div[4]/...')
        time.sleep(2.5)
        self.buttonLiePerson.click()
        time.sleep(2.5)  

        ### ---> funkction auto swipe
        ### ---> if program will meet obstacle,next check exceptions
    def autoLike(self): #dziala w petli while obsluguje wyjatki caly czas lajkowanie sprawdza czy wyskoczy nam jakes info (np dodaj cos)
        while True:
            time.sleep(0.5)
            try:
                self.like() 
                # self.eet info()
            except Exception:
                self.closeMatch()
    
    def closeAddStartWindow(self): #funkcja odpowiada za zamkniecie pupapu ktory segeruje nas trzeba dodac Tindera na laptopa dekstop
        time.sleep(0.5)
        self.notificationAddStartWindow = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[1]')
        time.sleep(0.5)
        self.notificationAddStartWindow.click()

    def closeMatch(self): #odpowiada za zamkniecie okna gdzie mam info ze zostalismy parą
        time.sleep(0.5)
        self.notificationMatchAllert = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]...')
        time.sleep(0.5)
        self.notificationMatchAllert.click()

TinderBotUser = TinderBot()
TinderBotUser.login()
TinderBotUser.autoLike()