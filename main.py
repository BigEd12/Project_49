from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_dev_path = "C:\Dev\chromedriver.exe"

#**************************-Logging in-**************************#
driver = webdriver.Chrome(chrome_dev_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3357211164&f_AL=true&f_E=1%2C2%2C3&f_WRA=true&geoId=92000000&keywords=python&location=Worldwide&refresh=true")
time.sleep(3)

login_button = driver.find_element(By.LINK_TEXT, "Sign in")
login_button.click()

time.sleep(4)

email_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

email_field.send_keys(YOUR-EMAIL)
password_field.send_keys(YOUR-PASSWORD)
password_field.send_keys(Keys.ENTER)


time.sleep(5)

# #**************************-Jobs page-**************************#
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card")
        easy_apply.click()
        time.sleep(5)

        apply_now = driver.find_element(By.LINK_TEXT, "Next")
        apply_now.click()
        time.sleep(3)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()



    except NoSuchElementException:
        print("No application button, skipped.")
        continue


driver.quit()