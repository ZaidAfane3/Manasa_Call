import sys
import json
import logging
import arabic_reshaper
from os import system
from os import getenv
from time import time
from time import sleep
from datetime import datetime
from typing import Counter

logging.basicConfig(filename="/home/ubuntu/manasa/manasa.log", level=logging.INFO)
with open ("/home/ubuntu/manasa/cred.json") as f:
    # environ = json.load('/home/ubuntu/manasa/cred.json')  
    environ = json.load(f)

def make_call():
    from twilio.rest import Client
    account_sid = environ['TWILIO_ACCOUNT_SID']
    auth_token = environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)
    # print ('[%s] Making Call' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    logging.info('[%s] Making Call' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    call = client.calls.create(
        twiml='<Response><Say>Hurry Up</Say></Response>',
        # to='+962790810526',
        to=environ['MY_PHONE'],
        from_=environ['TWILIO_PHONE']
    )
    print(call.sid)
def delay():
    from random import randint
    from random import uniform
    sleep(uniform(1, 10))
def manasa():
    from time import time
    from datetime import datetime
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

    Counter = 5 

    # print ('[%s] Script Started' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    logging.info('[%s] Script Started' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    if environ['TEST_CALL'] == 'True':
        make_call()

    # binary = FirefoxBinary('/app/vendor/firefox/firefox') #
    options = Options()#
    options.add_argument("--headless")##
    driver = webdriver.Firefox(options=options, executable_path='/home/ubuntu/manasa/geckodriver')
    # driver = webdriver.Firefox()

    while True: 
        # English
        link = 'https://www.gateway2jordan.gov.jo/landplatform/'
        driver.get(link)
        # print ('[%s] Page Opened In English' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        logging.info('[%s] Page Opened In English' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        sleep(3)
        options = Select(driver.find_element_by_xpath('//*[@id="ddlCrossingpoint"]')).options
        # print ('[%s] Options:' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) , end= "\t")
        logging.info('[%s] Options:' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        # print([option.text for option in options])
        logging.info([option.text for option in options])
        for option in options:
            words = option.text.split()
            for word in words: 
                # print(word.lower().strip())
                if 'king' in word.lower().strip():
                    make_call()
                    break
        if len(options) != 5:
            make_call()
            break

        # print ("\n")
        #Arabic
        link = 'https://www.gateway2jordan.gov.jo/landplatform/ar/'
        driver.get(link)
        # print ('[%s] Page Opened In Arabic' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        logging.info('[%s] Page Opened In Arabic' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        sleep(3)
        options = Select(driver.find_element_by_xpath('//*[@id="ddlCrossingpoint"]')).options
        # print ('[%s] Options:' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) , end= "\t")
        logging.info('[%s] Options:' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) )
        # print ( [arabic_reshaper.reshape(word)[::-1] for word in [option.text for option in options]] )
        logging.info( [arabic_reshaper.reshape(word)[::-1] for word in [option.text for option in options]])
        for option in options:
            words = option.text.split()
            for word in words: 
                if 'الملك' == arabic_reshaper.reshape(word)[::-1]:
                    make_call()
                    break
        if len(options) != 5:
            make_call()
            break

        delay()
        # print ('[%s] Refreshing' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        logging.info('[%s] Refreshing' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        print ("\n")

        # driver.close()
        # driver.refresh()


def main():
    # make_call()
    manasa()

if __name__ == "__main__":
    main()


