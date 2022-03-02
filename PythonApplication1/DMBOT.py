from selenium import webdriver
import time
unames = ['___vilas__']
messages = 'Hey! This is an auto generated message from PYTHON.'
browser = webdriver.Chrome('chromedriver')

def login(u, p):
    browser.get('https://www.instagram.com/')
    time.sleep(2)
    userin = browser.find_element_by_name('username')
    passin = browser.find_element_by_name('password')
    userin.send_keys(u)
    passin.send_keys(p)
    passin.submit()

def message():
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
    time.sleep(3)
    
    for i in unames: #iterate through usernames
        browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i) #enter the name
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]').click() #select the account
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div').click() #next
        time.sleep(1.5)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(messages) #type message
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click() #send the message
        time.sleep(1)
login('soulful_vampyr', '1Coconut1')
message()