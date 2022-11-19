


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os, sys

from bs4 import BeautifulSoup
delayTime = 2
audioToTextDelay = 10

byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")


"""
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import time,requests
from selenium.webdriver.common.keys import Keys













import time
import random
import os
import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
    

exec_file_name =  os.path.basename(__file__)[:-3]




op = Options()
op.add_argument("--disable-gpu")
op.add_argument("--disable-extensions")
op.add_argument("--proxy-server='direct://'")
op.add_argument("--proxy-bypass-list=*")
op.add_argument("--start-maximized")
#op.add_argument('headless')
# op.add_argument("--headless")
# op.add_argument('--user-agent=hogehoge')
#Iniciar navegador habitual (las cookies se pueden utilizar tal cual)
#driver = webdriver.Chrome(options=op)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)

#go to https://es.wallapop.com/

driver.get("https://es.wallapop.com/")


def custom_time_sleep():
    sec = 4 + random.uniform(0.1, 1)
    time.sleep(sec)


WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
)

#check if css id "onetrust-accept-btn-handler" is present. If it is, click it
custom_time_sleep()
if driver.find_element(by=By.CSS_SELECTOR, value='#onetrust-accept-btn-handler'):
    driver.find_element(by=By.CSS_SELECTOR, value='#onetrust-accept-btn-handler').click()
    


#click on login button

if driver.find_element(by=By.CSS_SELECTOR, value='.BtnLogin'):
    driver.find_element(by=By.CSS_SELECTOR, value='.BtnLogin').click()


if driver.find_element(by=By.CSS_SELECTOR, value='.Welcome__btn-go-login-form'):
    driver.find_element(by=By.CSS_SELECTOR, value='.Welcome__btn-go-login-form').click()


#get input with name="email" and set it to 'asederado@gmail.com'


driver.find_element(by=By.CSS_SELECTOR, value='input[name="email"]').send_keys('asederado6@gmail.com')
driver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]').send_keys('nicetry')
#find recaptcha-checkbox-border class and click it


#wait for google captcha iframe to load
#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/enterprise/anchor?']")))
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()










import whisper


model = whisper.load_model('base')











delayTime = 2

filename = '1.mp3'

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)
def audioToText(mp3Path):
    
    #wait for result = model.transcribe('1.mp3'), if it takes more than 10 seconds, return None
        
    try:
        result = model.transcribe('1.mp3')
    except:
        driver.find_element(by=By.CSS_SELECTOR, value='.rc-button-reload').click()
        audioBtnClick()
    if (result['text'] == '' or result['text'] == None or result['text'] == ' '):
        print('sin audio!')
        #click on class rc-button-reload
      
        driver.find_element(by=By.CSS_SELECTOR, value='.rc-button-reload').click()
        audioBtnClick()
        
    
   # result = model.transcribe(filename)
    print("audio: "+ result['text'])
    return result['text']






outeriframe = driver.find_element(By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/enterprise/anchor?']")
outeriframe.click()
#allIframesLen = driver.find_element(By.CSS_SELECTOR, value='iframe')
custom_time_sleep()
audioBtnFound = False
audioBtnIndex = -1


no_captcha = False
# go to iframe that has https://www.google.com/recaptcha/enterprise/bframe in src
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/enterprise/bframe?']"))
# wait for #recaptcha-audio-button to be clickable
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#recaptcha-audio-button")))
except Exception as e:
    print(e)
    #switch driver back to default content
    driver.switch_to.default_content()

    driver.find_element(by=By.CSS_SELECTOR, value='#sign-in-wallapop').click()
    no_captcha = True

    custom_time_sleep()

    pass


def audioBtnClick():
    try:
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/enterprise/bframe?']"))
    except:
        pass
    audioBtn = driver.find_element(by=By.CSS_SELECTOR, value='#recaptcha-audio-button')
    audioBtn.click()
    print('encontrado')
    custom_time_sleep()
    audioBtnFound = True
    #audioBtnIndex = index
    """
    except Exception as e:
        print("detectado error:")
        print(e)

        pass
    """
    if audioBtnFound:
        #switch to default content
        driver.switch_to.default_content()
        #wait for iframe[src^='https://www.google.com/recaptcha/enterprise/bframe?'] to load
        # get all iframe[src^='https://www.google.com/recaptcha/enterprise/bframe?'] elements and switch to the one that has audio source
        audioframe = driver.find_elements(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/enterprise/bframe?']")
        print(audioframe)
        print(audioframe[0])
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(audioframe[0]))

        href = driver.find_element_by_id('audio-source').get_attribute('src')
        response = requests.get(href, stream=True)
        saveFile(response,filename)


        response = audioToText(os.getcwd() + '/' + filename)


        print(response)   

        inputbtn = driver.find_element_by_id('audio-response')
        inputbtn.send_keys(response)
        inputbtn.send_keys(Keys.ENTER)
        time.sleep(2)
        errorMsg = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
        if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
            print("Success")
            driver.switch_to.default_content()
        no_captcha = True
    else:
        print('Button not found. This should not happen.')
        #click on id sign-in-wallapop
        driver.switch_to.default_content()
        driver.find_element(by=By.CSS_SELECTOR, value='#sign-in-wallapop').click()

    driver.switch_to.default_content()
    driver.find_element(by=By.CSS_SELECTOR, value='#sign-in-wallapop').click()


    print('done')


if (no_captcha == False):
    audioBtnClick()


custom_time_sleep()

#click button with id top-bar-upload
#wait for #top-bar-upload to be clickable
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#top-bar-upload")))
driver.find_element(by=By.CSS_SELECTOR, value='#top-bar-upload').click()
#click on a tsl-svg-icon with the src="/assets/icons/herocat-consumer-goods.svg"
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "tsl-svg-icon[src='/assets/icons/herocat-consumer-goods.svg']"))
)
driver.find_element(by=By.CSS_SELECTOR, value='tsl-svg-icon[src="/assets/icons/herocat-consumer-goods.svg"]').click()
#put into input with formcontrolname="title" the value of "iphone 11"
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='title']"))
)
driver.find_element(by=By.CSS_SELECTOR, value='input[formcontrolname="title"]').send_keys('bot autosubir productos')
#click to class Dropdown
script = "document.querySelectorAll('.placeholder')[0].click()"
#execute script
driver.execute_script(script)
#scroll down in class options to div with class cat_12485
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(by=By.CSS_SELECTOR, value='.cat_12485'))

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cat_12485"))
    )
custom_time_sleep()
driver.find_element(by=By.CSS_SELECTOR, value='.cat_12485').click()

#set input with id price to 100
driver.find_element(by=By.CSS_SELECTOR, value='#price').send_keys('100')