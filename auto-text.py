import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(1)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(10)


class Whatsapp():
    '''Class to Send Messages in WhatsApp using web.whatsapp
        Provide the contact name to whom the message is to be sent and the message to be sent it will be sent
    '''

    def __init__(self, contactName, message):
        self.contactName = contactName
        self.message = message

    def getContactName(self):
        return self.contactName

    def getMessage(self):
        return self.message

    def findContact(self):
        contact = None
        try:
            contact = driver.find_element_by_xpath(
                '//span[@title="' + self.contactName + '"]')
            contact.click()
        except:
            contact = driver.find_element_by_xpath(
                '//span[@title="' + self.contactName + '"]')
            contact.click()
        return contact

    def sendMessage(self):
        if self.message != None:
            textbox = driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            textbox.send_keys(self.message)
            textbox.send_keys(Keys.ENTER)
            print('Message Sent: '+self.message)
            driver.implicitly_wait(5)
        driver.quit()


def messageSelector():
    MORNING = './morning.json'
    NIGHT = './night.json'
    LUNCH = './lunch.json'
    EVE = './eve.json'
    filename = ''

    now = datetime.datetime.now()

    today12pm = now.replace(hour=12, minute=0, second=0, microsecond=0)
    today11pm = now.replace(hour=23, minute=0, second=0, microsecond=0)
    today4am = now.replace(hour=4, minute=0, second=0, microsecond=0)
    today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
    today8pm = now.replace(hour=20, minute=0, second=0, microsecond=0)

    if now <= today12pm:
        filename = MORNING
    elif now > today12pm and now <= today5pm:
        filename = LUNCH
    elif now > today5pm and now <= today8pm:
        filename = EVE
    elif now >= today11pm and now <= today4am:
        filename = NIGHT
    else:
        print("Not Appropriate to send Message now!!")
        return "HI!"
    data = []
    with open(filename) as f:
        data = json.load(f)
    i = random.randint(0, len(data)-1)
    return data[i]


def main():
    msg = messageSelector()
    wts = Whatsapp('Pengu 🐧', msg)
    wts.findContact()
    wts.sendMessage()


if __name__ == "__main__":
    main()
