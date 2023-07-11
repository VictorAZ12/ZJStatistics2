from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


# Set the path to your Chrome binary
chrome_binary_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

# Set the path to your Chrome WebDriver executable (e.g., chromedriver)
webdriver_path = 'D:/Downloads/chromedriver_win32/chromedriver.exe'


options = webdriver.ChromeOptions()
service = ChromeService(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
url = 'https://r.koif.uk/A-SOUL/ASOUL-REC-%E4%B8%80%E5%91%A8%E5%B9%B4/XML%E5%BC%B9%E5%B9%95%E6%96%87%E4%BB%B6/2021.12.08%20%E5%98%89%E7%84%B6%20%E8%B4%9D%E6%8B%89%20%E4%B9%83%E7%90%B3%20%E5%92%8C%E7%84%B6%E7%84%B6%E5%A7%90%E5%A7%90%E5%8E%BB%E5%94%B1%E6%AD%8C%EF%BC%81%EF%BC%81%EF%BC%81.xml'

driver.get(url)

# Wait for the page to load (you can increase the timeout as needed)
timeout = 360
wait = WebDriverWait(driver, timeout)
wait.until(EC.presence_of_element_located((By.ID, 'target-element-id')))

# Activate JavaScript (e.g., click on a button)
button_element = driver.find_element(By.ID, 'hope-select-cl-34-trigger')
button_element.click()

# Wait for the file to be downloaded
# (You may need to add a suitable delay or use other techniques depending on the website behavior)

# Close the web driver
driver.quit()
