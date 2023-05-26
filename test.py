from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()

dr = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe' , options=options)
time.sleep(1)
dr.get("https://studio.youtube.com/channel/UC4L81glDJwzQKo3Xmn0nA5w")