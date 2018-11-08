from skpy import Skype
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import random
import time

redish ="\033[01;31m"
lightblue = "\033[01;36m"
green = "\033[01;32m"
yellow = "\033[01;39m"


print(redish+"  WWWWWWWWWWWWWWW    "+green+"WWWWWWWWWWWWWWW")
print(redish+"  WWWWWWWWWWWWWWW    "+green+"WWWWWWWWWWWWWWW")
print(redish+"  WWWWWWWWWWWWWWW    "+green+"WWWWWWWWWWWWWWW")
print(redish+"  WWWWWWWWWWWWWWW    "+green+"WWWWWWWWWWWWWWW")
print(redish+"  WWWWWWWWWWWWWWW    "+green+"WWWWWWWWWWWWWWW")
print(redish+"  WWWWWWWWWWWWWWW    "+green+"WWWWWWWWWWWWWWW")
print("                                  ")
print(lightblue+"  WWWWWWWWWWWWWWW    "+yellow+"WWWWWWWWWWWWWWW")
print(lightblue+"  WWWWWWWWWWWWWWW    "+yellow+"WWWWWWWWWWWWWWW")
print(lightblue+"  WWWWWWWWWWWWWWW    "+yellow+"WWWWWWWWWWWWWWW")
print(lightblue+"  WWWWWWWWWWWWWWW    "+yellow+"WWWWWWWWWWWWWWW")
print(lightblue+"  WWWWWWWWWWWWWWW    "+yellow+"WWWWWWWWWWWWWWW")
print(lightblue+"  WWWWWWWWWWWWWWW    "+yellow+"WWWWWWWWWWWWWWW")

print("\n             Mircosoft-Skype - The black parallex ")
options = raw_input("\noption: ")
if options == "1" or options == "single":
#connect to app to send message
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    contact = raw_input("Target: ")
    msg = raw_input("Message: ")
    num = raw_input("Msg amount: ")
    skyp = Skype(str(username), str(password))

    chat = skyp.contacts([contact]).chat

    for _ in range(0,int(num)):
	    chat.sendMsg(msg) #

if options == "2" or options == "group":
    #https://join.skype.com/aPrDqSy8g9KW
    url = raw_input("skype_url: ")
    #using website to create spam account aka bot
    profile = webdriver.FirefoxProfile()
    useragents = random.choice([
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
	    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55',
	    'Mozilla/5.0 (X11; Heathrow/1.4; Linux i686; rv:30) Gecko/30 Firefox/30',
	    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN 10.2;MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'
    ])
    profile.set_preference("general.useragent.override", useragents)

    binary = FirefoxBinary('base/firefox/firefox')
    name = str(random.choice(['LubeSkywank','The_Zucc','joisadsdrfe','asdsasderewr','obama_3043','donald','trump','islam','mic','daddy','getgood','obama','get_f**K','who_that_pokemon_','is_that_you']))
    name2 =str(random.choice(['kill','hunter','a','windows','1','1212','3213213','32432432','23234','2','234324','_skypekiller']))
    mes = str(random.choice(['Iraq','fuck me daddy','daddy this that you','hi','hello','its me mario','cant spell','help me','bury me low','hmmmmmmmm','just kill skype','awesome','people of earth','cancer itself',':)','^-^','(^_^)','danger',':O','i cant belive youve done this']))


    br = webdriver.Firefox(firefox_binary=binary,executable_path='base/geckodriver',firefox_profile=profile)
    br.implicitly_wait(4000)
    br.get(url)
    time.sleep(12)
    #click buttom to join chat
    br.find_element_by_xpath("//a[@class='buttonBlue join-promt-mobile__c2a js-goGuestStep2']").click()
    #make random user name for guest
    br.find_element_by_id("guestName").send_keys((name+name2))
    br.find_element_by_xpath("//a[@class='buttonBlue guest-signin__join']").click()
    time.sleep(1)
    #send message
    for _ in range(1,99):
    	br.find_element_by_xpath("//textarea[@id='chatInputAreaWithQuotes']").send_keys(str(mes))
        br.find_element_by_xpath("//span[@class='iconfont send']").click()
