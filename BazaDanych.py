from time import sleep
from selenium import webdriver

browser = webdriver.Chrome('D:\Driver\chromedriver.exe')

browser.get("http://localhost/abcd/index.php")

idk=browser.find_element_by_name("id")
imie=browser.find_element_by_name("imie")
nazwisko=browser.find_element_by_name("nazwisko")
miasto=browser.find_element_by_name("miasto")

idk.send_keys('ABFD')
sleep(2)
imie.send_keys('AAAA')
sleep(2)
nazwisko.send_keys('AAAA')
sleep(2)
miasto.send_keys('Poniatowa')

button1=browser.find_element_by_id("s1")
sleep(5)
button1.click()

browser.close()