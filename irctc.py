from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import relative_locator
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
import cv2
import base64
import numpy as np
import time
from detect import bringbro





options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-web-security')
options.add_argument("--disable-notifications")  # Disable notifications
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)
driver = webdriver.Chrome(options= options)


driver.maximize_window()
options.add_argument("start-maximized")



driver.get("https://www.irctc.co.in/nget/train-search")



login_button = driver.find_element(By.XPATH,"//a[normalize-space()='LOGIN']")
login_button.click()

time.sleep(2)

username = 'jadaavinash'
pwd = 'Avn#@1011'
login_username = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="userid"]')
login_username.send_keys(username)

login_password = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
login_password.send_keys(pwd)




def captcha():
    image_element = driver.find_element(By.CLASS_NAME, 'captcha-img')  # Adjust locator
    img_url = image_element.get_attribute('src')

    base64_str = img_url.split(",")[1]
    image_data = base64.b64decode(base64_str)


    np_array = np.frombuffer(image_data, np.uint8)
        
    #     # Convert numpy array to an OpenCV image
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)


        # Pass the image to the bringbro function
    input_element = driver.find_element(By.ID, "captcha")
    input_element.send_keys(bringbro(image))

# captcha()

while True:
    captcha()  # Attempt to solve the captcha
    time.sleep(1)
    try:
        # Check for "Invalid Captcha" message
        
        driver.find_element(By.XPATH, f"//*[contains(text(), 'Invalid Captcha...')]")
        print("Invalid captcha detected, retrying...")
        time.sleep(1)
    except:
        # If no "Invalid Captcha" message, break the loop
        print("Captcha solved successfully!")
        time.sleep(1)
        break





# time.sleep(10)






date_element = driver.find_element(By.CSS_SELECTOR, 'p-calendar[formcontrolname="journeyDate"] span > input')
date_element.clear()
# date_element.click()
date_element.send_keys("05/01/2025")



origin_element = driver.find_element(By.XPATH,'//*[@id="origin"]/span/input')
# origin_element.send_keys("VISAKHAPATNAM - VSKP (VISAKHAPATNAM)")
origin_element.send_keys("DUVVADA - DVD (VISAKHAPATNAM)")




destination_element = driver.find_element(By.XPATH,'//*[@id="destination"]/span/input')
destination_element.send_keys("KATPADI JN - KPD (VELLORE)")

date_element.send_keys("05/01/2025")


fake_element = driver.find_element(By.CLASS_NAME,"loginhead")
fake_element.click()

booking_type = driver.find_element(By.XPATH,'//*[@id="journeyQuota"]/div')
booking_type.click()


tatkal = driver.find_element(By.XPATH,'//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[1]/li')
tatkal.click()



search_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Search'])[1]")
search_button.click()

time.sleep(1)

def highlight_element(driver, element):
    """Highlights (blinks) a Selenium WebDriver element."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

try:
    wait = WebDriverWait(driver, 20)  # 10 seconds timeout

    # Locate the specific text (e.g., 'text')
    text_to_find = "06088"
    text_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text_to_find}')]")))
    text_to_find2 = 'AC 3 Economy'
    ac_3_tier = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), '{text_to_find2}')]").below(text_element))


    # # Click the button
    ac_3_tier.click()
    time.sleep(1)

    ac_3_tier_again = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), '3E')]").below(text_element))
    time.sleep(1)
    seat_button = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), '05')]").below(ac_3_tier_again))

    highlight_element(driver, ac_3_tier_again)

    seat_button.click()

    bookbutton = driver.find_element(locate_with(By.XPATH, f"//*[contains(text(), 'Book Now')]").below(text_element))
    bookbutton.click()


    # time.sleep(2)
    passenger_name = wait.until(EC.presence_of_element_located((By.XPATH, "//p-autocomplete[@field='masterPassengerName']//input[@placeholder='Name']")))
    # passenger_name = driver.find_element(By.XPATH,"//input[@placeholder='Passenger Name']")
    passenger_name.send_keys("Jada Avinash")

    passenger_age = driver.find_element(By.XPATH,"//input[@placeholder='Age']")
    passenger_age.send_keys('20')

    passenger_gender = driver.find_element(By.XPATH,'/html[1]/body[1]/app-root[1]/app-home[1]/div[3]/div[1]/app-passenger-input[1]/div[6]/form[1]/div[1]/div[1]/div[6]/p-panel[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/app-passenger[1]/div[1]/div[1]/span[1]/div[3]/select[1]')
    dd = Select(passenger_gender)
    dd.select_by_visible_text("Male")
    
    phone_number = driver.find_element(By.XPATH,"//input[@id='mobileNumber']")
    phone_number.clear()
    phone_number.send_keys('8179155683')

    upi_radio = driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-home[1]/div[3]/div[1]/app-passenger-input[1]/div[6]/form[1]/div[1]/div[1]/div[14]/p-panel[1]/div[1]/div[2]/div[1]/table[1]/tr[2]/label[1]/p-radiobutton[1]/div[1]/div[2]/span[1]")
    upi_radio.click()

    continue_with_payment = driver.find_element(By.XPATH,"//button[@class='train_Search btnDefault']")
    continue_with_payment.click()

    # time.sleep(20)


    def s_captcha():
        image_element = driver.find_element(By.CLASS_NAME, 'captcha-img')  # Adjust locator
        img_url = image_element.get_attribute('src')

        base64_str = img_url.split(",")[1]
        image_data = base64.b64decode(base64_str)


        np_array = np.frombuffer(image_data, np.uint8)
            
        #     # Convert numpy array to an OpenCV image
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)


            # Pass the image to the bringbro function
        input_element = driver.find_element(By.ID, "captcha")
        input_element.send_keys(bringbro(image))

    #################################
    captcha = wait.until(EC.presence_of_element_located((By.XPATH,"//img[@class='captcha-img']")))
    # captcha = driver.find_element(By.XPATH,"//img[@class='captcha-img']")
    # time.sleep(10)

    
    while True:
        s_captcha()  # Attempt to solve the captcha
        time.sleep(1)
        try:
            # Check for "Invalid Captcha" message
            
            driver.find_element(By.XPATH, f"//*[contains(text(), 'Invalid Captcha')]")
            print("Invalid captcha detected, retrying...")
        except:
            # If no "Invalid Captcha" message, break the loop
            print("Captcha solved successfully!")
            break






    continue_butt = driver.find_element(By.XPATH,"//button[@class='btnDefault train_Search']")
    continue_butt.click()


except Exception as e:
    print(f"An error occurred: {e}")









time.sleep(10)

# driver.quit()

