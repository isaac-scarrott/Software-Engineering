import simplejson as json
import os
from selenium import webdriver
import time
## MAX OSX ##
#br = webdriver.Firefox(executable_path='/Users/isaacscarrott/Universirty Work/Software Engineering/Programming/webdrivers/firefox/geckodriver')

## WINDOWS OS ##
br = webdriver.Firefox(executable_path='C:/Users/Kyle/Desktop/geckodriver.exe')

br.implicitly_wait(15) 
br.get('http://www.omdbapi.com/')

search = br.find_element_by_name('t')
search.send_keys('blade runner')
search_button = br.find_element_by_id('search-by-title-button')
search_button.click()
search_return = br.find_element_by_class_name('alert-success').text
data = json.loads(search_return)
print(data)

time.sleep(5)
print(br.title)