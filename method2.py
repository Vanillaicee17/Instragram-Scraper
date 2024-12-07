from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from dotenv import load_dotenv
import os

load_dotenv()
# Set up the WebDriver for Firefox
driver = webdriver.Firefox()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")


# Log in to Instagram
driver.get("https://www.instagram.com/accounts/login/")

# Wait for elements to be present and interact with them
wait = WebDriverWait(driver, 10)  # 10 seconds timeout

username_field = wait.until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_field.send_keys(USERNAME)

password_field = wait.until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_field.send_keys(PASSWORD)

submit_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))
)
submit_button.click()

# Wait for the login to complete
time.sleep(5)

# Handle the "Not now" popup
try:
    not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    not_now_button.click()
    print("Clicked 'Not Now' button.")
except TimeoutException:
    print("'Not Now' button not found: Timeout occurred.")
except NoSuchElementException:
    print("'Not Now' button not found: Element does not exist.")




def _get_names():
    """Helper function to scroll and extract names."""
    time.sleep(2)
    scroll_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))
    last_ht, ht = 0, 1
    names = set()  # Use a set to avoid duplicates

    while last_ht != ht:
        last_ht = ht
        time.sleep(1)  # Pause to allow new content to load
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
        """, scroll_box)

        # Fetch new visible links after each scroll
        links = scroll_box.find_elements(By.TAG_NAME, "a")
        for link in links:
            try:
                if link.text:
                    names.add(link.text)
            except Exception as e:
                print(f"Error accessing link: {e}")

    # Convert set to list for further use
    names = list(names)

    # Try to close the modal dialog
    try:
        close_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Close')]"))
        )
        close_button.click()
    except Exception as e:
        print(f"Close button not found: {e}. Attempting alternative methods.")
        try:
            driver.find_element(By.CSS_SELECTOR, "body").click()
        except Exception as click_outside_error:
            print(f"Failed to dismiss modal by clicking outside: {click_outside_error}")

    return names





def get_usernames(endpoint):
    """Scrapes usernames from followers or following pages."""
    driver.get(f"https://www.instagram.com/_ax3y_/{endpoint}/")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/_ax3y_/{endpoint}/"]'))).click()

    time.sleep(3)  # Ensure page has loaded
    return _get_names()


# Scrape followers and following
followers_names = get_usernames("followers")
print(f"Followers: {len(followers_names)} collected.")

following_names = get_usernames("following")
print(f"Following: {len(following_names)} collected.")

# Find accounts you follow but don't follow you back
not_following_back = set(following_names) - set(followers_names)

print("Accounts that don't follow you back:")
for username in not_following_back:
    print(username)

driver.quit()
