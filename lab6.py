from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://vk.com/")

login_field = driver.find_element_by_xpath("//*[@id=\"index_email\"]")
password_field = driver.find_element_by_xpath("//*[@id=\"index_pass\"]")
loginButton = driver.find_element_by_xpath("//*[@id=\"index_login_button\"]")
login, password = open('logpass1.txt').readlines()

login_field.send_keys(login)
password_field.send_keys(password)
loginButton.click()

WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'l_msg'))).click()
search_field = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'im_dialogs_search')))
search_field.click()
search_field.send_keys('Максим Волков')
search_field.send_keys(Keys.ENTER)
message_field = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'im_editable0')))
message_field.send_keys('Привет!')
message_field.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
driver.quit()
