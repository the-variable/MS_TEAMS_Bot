from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

uid, password = '', ''

browser = webdriver.Chrome('chromedriver')
message1 = 'Hi! This is an automated message sent by Python.'
message2 = 'IEEE-RAS rocks!!'

def tab():
    pyautogui.hotkey('alt', 'tab')

def login():
    try:
        uid = input('Enter your e-mail id\n')
        password = input('Enter your password\n')
        tab()
        browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1646150801&rver=7.3.6960.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2frpsauth%2fv1%2faccount%2fSignInCallback%3fstate%3dhttps%3a%2f%2fwww.microsoft.com%2fen-in%2fmicrosoft-teams%2fgroup-chat-software&id=74335')
        time.sleep(1)
        pyautogui.hotkey('win', 'up')
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(uid) #enter email id
        browser.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(1.5)
        browser.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password) #enter password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(2)
        if(browser.find_element(By.XPATH, '//*[@id="idBtn_Back"]').is_displayed()):
            browser.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click() #choosing not to stay signed in
            browser.get('https://teams.live.com/_') #redirecting to MS Teams
            time.sleep(10)
            browser.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a').click() #choosing to use the web version
            time.sleep(8)

    except:
        time.sleep(2)
        print('Wrong credentials entered.\nRe-enter your credentials')
        pyautogui.hotkey('win', 'down')
        tab()
        login()
        time.sleep(4)


def chat():
     
     

     browser.find_element_by_xpath('//*[@id="toast-container"]/div/div/div[2]/div/button[2]/div').click() #dismiss notifications
     time.sleep(1)
     while(True):
        browser.find_element(By.XPATH, '//*[@id="left-rail-header"]/div/button[3]').click() #clicking on the compose button

        tab()
        email = input('Enter e-mail id of recepient: (print "end" to logout and exit)\n') #getting recipient from the user

        if(email == 'end'): logout()
            
        tab()

        time.sleep(4)
        pyautogui.click(x = 892, y = 237) #clicking on id box
        pyautogui.write(email, interval = 0.01) #entering the ID
        time.sleep(6)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(x = 888, y = 999)
        time.sleep(2.5)
        #message1
        pyautogui.click(x = 888, y = 999) #clicking on the message box
        time.sleep(3)
        pyautogui.write(message1, interval = 0.01) #typing the message
        time.sleep(2)
        pyautogui.press('enter') #send!
        time.sleep(1)
        #message2
        pyautogui.write(message2, interval = 0.01) #typing the message
        time.sleep(2)
        pyautogui.press('enter') #send!
        time.sleep(4)
     

def logout():
    tab()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="personDropdown"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="logout-button"]').click()
    time.sleep(4)
    tab()
    """
    f = input('\t\t\tDID U LIKE IT??!?!(y/n)\n\t\t\t\t')
    if(f=='y'): print('\t\t\tTHANK YOU!!')
    if(f=='n'): print('\t\t\tCOOL, NP :)')
    """
    browser.quit()
    exit()

tab()
time.sleep(5)
login()
chat()
logout()