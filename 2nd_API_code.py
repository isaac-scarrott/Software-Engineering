import simplejson as json
import os
from selenium import webdriver
import time
import re

br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver32.exe")

text="up"

br.implicitly_wait(15) 

br.get('https://api.themoviedb.org/3/search/movie?api_key=1e0dcaa7e93980fb84e1d2430d01b887&query=' + text)

id_num = br.find_element_by_id('/results/0/id').text
id_num = re.findall('\d', id_num)
id = ''.join(map(str, id_num))

#print(id)

br.get('https://api.themoviedb.org/3/movie/' + id + '?api_key=1e0dcaa7e93980fb84e1d2430d01b887')

search_button = br.find_element_by_id('rawdata-tab')
search_button.click()
search_return = br.find_element_by_class_name('data').text
data = json.loads(search_return)
poster = br.find_element_by_id('poster_path')

img = 'https://image.tmdb.org/t/p/w185' + poster_path)

https://image.tmdb.org/t/p/w185/nk11pvocdb5zbFhX5oq5YiLPYMo.jpg


#print (data)

#os.system("TASKKILL /F /IM firefox.exe")

