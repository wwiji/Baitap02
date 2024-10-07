from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd

gecko = r"D:\\data\\geckodriver.exe"

ser = Service(gecko)

options = webdriver.firefox.options.Options()
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
options.headless = False

driver = webdriver.Firefox(options = options, service=ser)
driver.get("https://gochek.vn/collections/all")
time.sleep(3)

products = driver.find_elements(By.CLASS_NAME, "product-block")

data = []
for product in products:
    try:
        product_name = product.find_element(By.CLASS_NAME, "pro-name").text
        product_price = product.find_element(By.CLASS_NAME, "pro-price.highlight").text
        product_compare_price = product.find_element(By.CLASS_NAME, "compare-price").text if product.find_elements(By.CLASS_NAME, "compare-price") else "Không có giá cũ"
        data.append({"product_name": product_name, "product_price": product_price, "product_compare_price": product_compare_price})
    except:
        pass

df = pd.DataFrame(data)
df.to_excel("gochek11.xlsx", index=False)
driver.quit()
