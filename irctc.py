from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import relative_locator
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

import time


options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-web-security')
driver = webdriver.Chrome()


driver.maximize_window()
options.add_argument("start-maximized")



driver.get("https://www.irctc.co.in/nget/train-search")



login_button = driver.find_element(By.XPATH,"//a[normalize-space()='LOGIN']")
login_button.click()

time.sleep(2)

username = 'jadaavinash'
pwd = 'Avn#@1011'
login_username = driver.find_element(By.CLASS_NAME,"form-control")
login_username.send_keys(username)

login_password = driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-home[1]/div[3]/app-login[1]/p-dialog[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/form[1]/div[2]/input[1]")
login_password.send_keys(pwd)



time.sleep(10)



origin_element = driver.find_element(By.XPATH,'//*[@id="origin"]/span/input')
origin_element.send_keys("VISAKHAPATNAM - VSKP (VISAKHAPATNAM)")


destination_element = driver.find_element(By.XPATH,'//*[@id="destination"]/span/input')
destination_element.send_keys("KATPADI JN - KPD (VELLORE)")

# date_element = driver.find_element(By.XPATH,'//*[@id="jDate"]/span/input')
# date_element.clear()
# date_element.send_keys("02/07/2024")


date_element = driver.find_element(By.XPATH,'//*[@id="jDate"]/span/input')
date_element.click()
# date_elementq = driver.find_element(By.XPATH,'//*[@id="jDate"]/span/div/div/div[2]/table/tbody/tr[2]/td[3]/a')
date_elementq = driver.find_element(By.XPATH,"//a[normalize-space()='31']")
date_elementq.click()


booking_type = driver.find_element(By.XPATH,'//*[@id="journeyQuota"]/div')
booking_type.click()

tatkal = driver.find_element(By.XPATH,'//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[1]/li')
tatkal.click()



search_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Search'])[1]")
search_button.click()





# # find_train_div = driver.find_element(By.XPATH,'')

# try:
#     # Wait until the text is present
#     text_to_find = " VIVEK EXPRESS (22504)"
#     wait = WebDriverWait(driver, 10)
#     text_element = WebDriverWait(driver, 10).until(
#         # EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{text_to_find}')]"))
#         train_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")
#     )
#     # train_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")

#     print("found")

#     # Click the button

# finally:
#     # Close the WebDriver
#     driver.quit()


# text_to_find = "22504"
# WebDriverWait(driver,15).until(
#     EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text_to_find}')]"))
# )

def highlight_element(driver, element):
    """Highlights (blinks) a Selenium WebDriver element."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

try:
    # Wait until the specific element is present (adjust the selector as needed)
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    # Locate the specific text (e.g., 'text')
    text_to_find = "22504"
    text_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text_to_find}')]")))

    # container_div = text_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'ng-star-inserted')]")

    # ac_3_tier = container_div.find_element(By.XPATH, ".//strong[contains(text(), 'AC 3 Tier')]")
    text_to_find2 = 'AC 3 Tier'
    ac_3_tier = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), '{text_to_find2}')]").below(text_element))


    # # Click the button
    ac_3_tier.click()
    time.sleep(2)

    ac_3_tier_again = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), '3A')]").below(text_element))
    seat_button = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), '31')]").below(ac_3_tier_again))

    highlight_element(driver, ac_3_tier_again)

    seat_button.click()

    bookbutton = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), 'Book Now')]").below(text_element))
    bookbutton.click()


    time.sleep(2)

    passenger_name = driver.find_element(By.XPATH,"//input[@placeholder='Passenger Name']")
    passenger_name.send_keys("Jada Avinash")

    passenger_age = driver.find_element(By.XPATH,"//input[@placeholder='Age']")
    passenger_age.send_keys('20')

    passenger_gender = driver.find_element(By.XPATH,'//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
    dd = Select(passenger_gender)
    dd.select_by_visible_text("Male")
    
    phone_number = driver.find_element(By.XPATH,"//input[@id='mobileNumber']")
    phone_number.clear()
    phone_number.send_keys('8179155683')

    upi_radio = driver.find_element(By.XPATH,"//span[@class='ui-radiobutton-icon ui-clickable']")
    upi_radio.click()

    continue_with_payment = driver.find_element(By.XPATH,"//button[@class='train_Search btnDefault']")
    continue_with_payment.click()

    time.sleep(20)


    #enter captcha
    #################################
    captcha = driver.find_element(By.XPATH,"//img[@class='captcha-img']")
    time.sleep(10)

    continue_butt = driver.find_element(By.XPATH,"//button[@class='btnDefault train_Search']")
    continue_butt.click()


    time.sleep(10)
    ##################################
    #payment
    multi_payrazr = driver.find_element(By.XPATH,"//span[normalize-space()='Multiple Payment Service']")
    multi_payrazr.click()



    ##
    razr = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), 'Razorpay')]")))
    razr.click()


    paynbook = driver.find_element(By.XPATH,"//button[@class='btn btn-primary hidden-xs ng-star-inserted']")
    paynbook.click()

    
    print("found")

except Exception as e:
    print(f"An error occurred: {e}")









time.sleep(10)

driver.quit()
