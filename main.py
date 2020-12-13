from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


browser = webdriver.Chrome()
browser.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=00a4db61-b8a0-4aea-bf25-d549c63dec58&&client-request-id=d64616fc-fc4e-4536-828f-9bbdd2a96672&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=fc07a0e9-2beb-462a-8079-3447ac21c443&domain_hint=")
browser.implicitly_wait(15)

username = browser.find_element_by_id("i0116")
username.send_keys("ghavtadze.sopio@students.gov.ge")
submit = browser.find_element_by_id("idSIButton9").click()
time.sleep(5)
password = browser.find_element_by_id("i0118")
password.send_keys("Sopio1$")
submit = browser.find_element_by_id("idSIButton9").click()
time.sleep(3)
submit = browser.find_element_by_id("KmsiCheckboxField").click()
submit = browser.find_element_by_id("idSIButton9").click()
time.sleep(10)
#link = browser.find_element_by_link_text('Use the web app instead')
#link.click()
#time.sleep(7)
submit = browser.find_element_by_id("app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c").click()
time.sleep(10)
submit = browser.find_element_by_id("AAMkADJjN2ExYzk2LTIzMjUtNDM3NS1iM2I5LTNkOWE4MjA4YTViNQFRAAgI2IXUu5tAAEYAAAAATFCjDNqqQ0SVP5ZP4GKErwcABeXBK3befkeisLy2-7ePHAAAAAABDQAABeXBK3befkeisLy2-7ePHAABPa0ayQAAEA==").click()
time.sleep(2)
#list of lessons
link = browser.find_element_by_link_text('English Language')
submit = browser.find_element_by_id("id__125").click()
time.sleep(1500)
link = browser.find_element_by_link_text('Russian Language')
submit = browser.find_element_by_id("id__131").click()
time.sleep(1500)


WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']"))).click()