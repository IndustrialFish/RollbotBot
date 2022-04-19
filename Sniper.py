import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://rollbit.com/nft/lobby/sportsbots")
time.sleep(5)

while(True):

    Mainfilter = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[1]/div/div[3]/button[2]').click()
    Lowestfilter = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]').click()

    print(driver.title)
    time.sleep(1)

