from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

name=input("Enter name")
msg=input("Enter msg")
no=int(input("no of times to spam"))
try:
    search_box =driver.find_element("xpath",'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    search_box.click()
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)

    '''first_search=driver.find_element("xpath",'//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]')
    first_search.click()'''

    for i in range(no+1):
        textbox=driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        textbox.send_keys(msg)
        textbox.send_keys(Keys.ENTER)

    
    time.sleep(10)
    driver.quit()

except:
    time.sleep(10)
    driver.quit()
