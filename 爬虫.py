# https://sites.google.com/a/chromium.org/chromedriver/downloads
# VS Code发现一个bug，CTRL+F5运行浏览器会自动关闭，按上面的绿色三角运行就不会关闭

from selenium import webdriver

PATH = 'C:/Users/WIN10/Desktop/Selenium/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.dcard.tw/f')
print(driver.title)

# 关闭driver
driver.quit()