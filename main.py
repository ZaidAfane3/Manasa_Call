from os import system
import sys
from time import sleep
from time import time
from datetime import datetime

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

    binary = FirefoxBinary('/app/vendor/firefox/firefox')

    # print ('[%s] Started Script' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    link = 'https://www.gateway2jordan.gov.jo/landplatform/'
    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path='/app/geckodriver')
    driver = webdriver.Firefox(options=options, executable_path='/app/vendor/geckodriver/geckodriver', firefox_binary=binary)

    driver.get(link)
    while True: 
        # print ('[%s] Page Loaded' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        options = Select(driver.find_element_by_xpath('//*[@id="ddlCrossingpoint"]')).options
        start = time()
        # print (f'[%s] {[ option.text for option in options]}' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        for option in options:
            words = option.text.split()
            for word in words: 
                if 'king' == word.lower():
                    make_call()
                    break

        if len(options) != 5:
            make_call()
            break
        # print ('[%s] Didn\'t Open Yet' %(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), flush=True)
        delay()
        driver.refresh()


def main():
    # make_call()
    manasa()

if __name__ == "__main__":
    main()


