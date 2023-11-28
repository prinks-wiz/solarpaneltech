from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup

# Initialize Chrome webdriver
options = webdriver.ChromeOptions()


prefs = {'download.default_directory':'/Users/prinks/downloads'}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome()
# Open PVGIS website
driver.get("https://re.jrc.ec.europa.eu/pvg_tools/en/")


# Enter location
latitude_input = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[4]/div/form/div[2]/div[2]/input')
latitude_input.send_keys("13.077")

longitude_input = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[4]/div/form/div[2]/div[3]/input')
longitude_input.send_keys("80.259")

driver.find_element(By.XPATH,'//*[@id="tabsTools"]/ul/li[1]').click()

# Click "Calculate" button
calculate_button = driver.find_element('xpath', '/html/body/div[3]/div[1]/div[1]/div[4]/div/form/div[2]/div[4]')
driver.execute_script("arguments[0].click();", calculate_button)
print("grid connected")
PV_tech_input = Select(driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[3]/div[2]/select'))
#options CrystSi, CIS, CdTe
PV_tech_input.select_by_value('crystSi')


# Database_select= Select(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[1]/div[2]/select'))
# Database_select.select_by_visible_text("PVGIS-SARAH")

peakPower = driver.find_element('xpath', '/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[4]/div[2]/input')
value = '1'
driver.execute_script("arguments[0].value = '" + value + "'", peakPower)


loss_input = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[5]/div[2]/input')
value = '14'
driver.execute_script("arguments[0].value = '" + value + "'", loss_input)



mount_input = Select(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[8]/select'))
mount_input.select_by_value('free')

slope_input = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[10]/div[2]/input')
value = '35'
driver.execute_script("arguments[0].value = '" + value + "'", slope_input)


azimuth_input = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[12]/div[2]/input')
value = '0'
driver.execute_script("arguments[0].value = '" + value + "'", azimuth_input)

PVEco_checkbox = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[14]/div/label/input')
driver.execute_script("arguments[0].click();", PVEco_checkbox)


PV_cost = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[15]/div[2]/input')
value = '39.09'
driver.execute_script("arguments[0].value = '" + value + "'", PV_cost)


interest_input = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[17]/div[2]/input')
value = '8'
driver.execute_script("arguments[0].value = '" + value + "'", interest_input)

lifetime_input = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/div/div/div/div[1]/form/fieldset/div/div/div/div/div/div[19]/div[2]/input')
value = '10'
driver.execute_script("arguments[0].value = '" + value + "'", lifetime_input)

json_get = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div')
driver.execute_script("arguments[0].click();", json_get)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href]')))

# Get the HTML content of the page
html_content = driver.page_source

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the download link element
download_link = soup.find_all('a', href=True)


for i in download_link:
    print()
    print(i)
    

# Create a network interceptor object


print("\n\n SUCCESS \n\n")




