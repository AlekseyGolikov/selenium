# Selenium 
# Start
from selenium import webdriver
from time import sleep

url = "http://militera.lib.ru/"

driverChrome = webdriver.Chrome(executable_path='/home/aleksey/PycharmProjects/selenium/chromedriver')
# driverFirefox = webdriver.Firefox(executable_path='/home/aleksey/PycharmProjects/selenium/geckodriver')

try:
    driverChrome.get(url=url)
    # driverFirefox.get(url=url)

    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driverChrome.close()
    # driverFireFox.close()
