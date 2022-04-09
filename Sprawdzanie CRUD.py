from time import sleep
from selenium import webdriver

browser = webdriver.Chrome('D:\Driver\chromedriver.exe')

browser.get("http://localhost/abcd/index.php")

idk=browser.find_element_by_name("id")
imie=browser.find_element_by_name("imie")
nazwisko=browser.find_element_by_name("nazwisko")
miasto=browser.find_element_by_name("miasto")

idk.send_keys('ABCD1')
imie.send_keys('Marek')
nazwisko.send_keys('ABCD')
miasto.send_keys('Lublin')
sleep(2)

button1=browser.find_element_by_id("s1")
button1.click()

browser.save_screenshot('D:\sreen\zapis.png')

browser.find_element_by_xpath ("//a [@href='edit.php?id=ABCD1']").click()

miasto2=browser.find_element_by_name("miasto")
miasto2.clear()
miasto2.send_keys('Poniatowa')
sleep(2)

browser.find_element_by_xpath ("//input [@value='zapisz']").click()
sleep(2)
browser.find_element_by_xpath ("//a [@href='index.php']").click()
sleep(2)
browser.save_screenshot('D:\sreen\edycja.png')

browser.find_element_by_xpath("//a [@href='usun.php?id=ABCD1']").click()
browser.find_element_by_xpath ("//a [@href='index.php']").click()

browser.save_screenshot('D:\sreen\exit.png')

sleep(2)
browser.close()