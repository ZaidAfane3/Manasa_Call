from os import system
from os import getenv
import sys
from time import sleep
from time import time
from datetime import datetime

from six import binary_type

def make_call():
    from twilio.rest import Client
    import os
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)
    print ('[%s] Making Call' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    call = client.calls.create(
        twiml='<Response><Say>Hurry Up</Say></Response>',
        # to='+962790810526',
        to=os.environ['MY_PHONE'],
        from_=os.environ['TWILIO_PHONE']
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

    print ('[%s] Script Started' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    while True: 
        binary = FirefoxBinary('/app/vendor/firefox/firefox') #
        link = 'https://www.gateway2jordan.gov.jo/landplatform/'
        options = Options()#
        options.add_argument("--headless")##
        driver = webdriver.Firefox(options=options, executable_path='/app/vendor/geckodriver/geckodriver', firefox_binary=binary)
        # driver = webdriver.Firefox()

        # English
        driver.get(link)
        options = Select(driver.find_element_by_xpath('//*[@id="ddlCrossingpoint"]')).options
        if getenv('TEST_CALL') == 'TRUE':
            make_call()
        for option in options:
            words = option.text.split()
            for word in words: 
                if 'Hussein' == word.lower():
                    make_call()
                    break
        if len(options) != 5:
            make_call()
            break

        #Arabic
        link = 'https://www.gateway2jordan.gov.jo/landplatform/ar/'

        driver.get(link)
        options = Select(driver.find_element_by_xpath('//*[@id="ddlCrossingpoint"]')).options
        if getenv('TEST_CALL') == 'TRUE':
            make_call()
        for option in options:
            words = option.text.split()
            print (words)
            for word in words: 
                if 'حسين' == word.lower():
                    make_call()
                    break
        if len(options) != 5:
            make_call()
            break

        
        delay()


        # driver.refresh()
        driver.close()


def main():
    # make_call()
    manasa()

if __name__ == "__main__":
    main()


