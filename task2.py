from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Setup Chrome Driver
chromedriver_path = "C:/Users/Alexyesudass/Desktop/BANAO TASK/chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

profile = "wix"
driver.get(f"https://twitter.com/{profile}")
print(f"Visiting https://twitter.com/{profile}")

wait = WebDriverWait(driver, 15)

# Scroll to ensure elements load
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

# Fetch Followers Count
try:
    followers_xpath = '//a[contains(@href, "followers")]//span'
    followers_element = wait.until(EC.presence_of_element_located((By.XPATH, followers_xpath)))
    followers_count = followers_element.text
    print(f"Found Followers: {followers_count}")
except Exception as e:
    followers_count = "Not found"
    print("Oops, couldn’t find Followers:", e)

# Fetch Following Count
try:
    following_xpath = '//a[contains(@href, "following")]//span'
    following_element = wait.until(EC.presence_of_element_located((By.XPATH, following_xpath)))
    following_count = following_element.text
    print(f"Found Following: {following_count}")
except Exception as e:
    following_count = "Not found"
    print("Oops, couldn’t find Following:", e)

# Fetch Bio
try:
    bio_xpath = '//div[@data-testid="UserDescription"]'
    bio_element = wait.until(EC.presence_of_element_located((By.XPATH, bio_xpath)))
    bio = bio_element.text
    print(f"Bio: {bio}")
except Exception as e:
    bio = "Not found"
    print("Oops, couldn’t find Bio:", e)

# Fetch Location
try:
    location_xpath = '//span[@data-testid="UserLocation"]'
    location_element = wait.until(EC.presence_of_element_located((By.XPATH, location_xpath)))
    location = location_element.text
    print(f"Location: {location}")
except Exception as e:
    location = "Not found"
    print("Oops, couldn’t find Location:", e)

# Fetch Website
try:
    website_xpath = '//a[@data-testid="UserUrl"]'
    website_element = wait.until(EC.presence_of_element_located((By.XPATH, website_xpath)))
    website = website_element.text
    print(f"Website: {website}")
except Exception as e:
    website = "Not found"
    print("Oops, couldn’t find Website:", e)

# Save Data to CSV
data = {
    "Username": [profile],
    "Bio": [bio],
    "Location": [location],
    "Website": [website],
    "Followers": [followers_count],
    "Following": [following_count]
}
filename = f"twitter_data_{time.strftime('%Y%m%d_%H%M%S')}.csv"
df = pd.DataFrame(data)
df.to_csv(filename, index=False)
print(f"Saved data to {filename}")

# Close Browser
driver.quit()
print("All done!")
