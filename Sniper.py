import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://rollbit.com/nft/lobby/sportsbots")
time.sleep(60)

while (True):

    time.sleep(5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[1]/div/div[3]/button[2]').click()  # Click Main Filter
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]').click()  # Click on Lowest Price Filter

    time.sleep(2)

    price = driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div[1]/div/div[4]/div[1]/div[4]/div[3]/div').text.replace("$", "")
    # Price of the cheapest NFT
    print(price)

    try:
        priceFloat = float(price)

    except:
        priceFloat = 1000.0

    buyPrice = 850

    if priceFloat < buyPrice:
        driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div[1]/div/div[4]/div[1]/div[5]/button[1]').click()
        # Click on Lowest Price Filter
        print("BUY | " + driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div[1]/div/div[4]/div[1]/div[1]/div/a/div').text + " | Price: $" + price)

    driver.refresh()
