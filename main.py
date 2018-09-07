from selenium import webdriver
import time



url = 'https://nike.com/de/launch'

driver=webdriver.Chrome('ChromeDriver')
driver.get(url)

driver.find_element_by_class_name('ncss-btn-accent').click()

time.sleep(2)

driver.find_element_by_class_name('join-log-in').click()

time.sleep(1)

driver.find_element_by_link_text('Jetzt registrieren.').click()

time.sleep(1)

driver.find_element_by_name('emailAddress').send_keys('E-Mail Adress')

time.sleep(1)

driver.find_element_by_name('password').send_keys('Password')

time.sleep(0.5)

driver.find_element_by_name('firstName').send_keys('FirstName')

time.sleep(0.5)

driver.find_element_by_name('lastName').send_keys('lastName')

time.sleep(0.5)

driver.find_element_by_name('dateOfBirth').send_keys('Birthday')

time.sleep(5)

driver.find_element_by_class_name('country').send_keys('Country')
