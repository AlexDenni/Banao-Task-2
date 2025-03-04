from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up Chrome Driver
chromedriver_path = "C:/Users/Alexyesudass/Desktop/BANAO TASK/chromedriver.exe"  # Path to ChromeDriver
service = Service(chromedriver_path)  # Initialize service

# Launch Chrome browser
driver = webdriver.Chrome(service=service)

# Define Twitter profile to scrape
twitter_profile = "wix"
driver.get(f"https://twitter.com/{twitter_profile}")  # Open Twitter profile
print(f"Visiting https://twitter.com/{twitter_profile}")

# Set up explicit wait for elements to load
wait = WebDriverWait(driver, 15)

# Scroll down slightly to ensure elements are loaded
# Some elements might not appear until scrolling
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

# Fetch Followers Count
try:
    followers_xpath = '//a[contains(@href, "followers")]//span'  # XPath for followers count
    followers_element = wait.until(EC.presence_of_element_located((By.XPATH, followers_xpath)))
    followers_count = followers_element.text  # Extract text content
    print(f"Found Followers: {followers_count}")
except Exception as e:
    followers_count = "Not found"
    print("Oops, couldn’t find Followers:", e)

# Fetch Following Count
try:
    following_xpath = '//a[contains(@href, "following")]//span'  # XPath for following count
    following_element = wait.until(EC.presence_of_element_located((By.XPATH, following_xpath)))
    following_count = following_element.text  # Extract text content
    print(f"Found Following: {following_count}")
except Exception as e:
    following_count = "Not found"
    print("Oops, couldn’t find Following:", e)

# Fetch Bio (User Description)
try:
    bio_xpath = '//div[@data-testid="UserDescription"]'  # XPath for bio section
    bio_element = wait.until(EC.presence_of_element_located((By.XPATH, bio_xpath)))
    bio = bio_element.text  # Extract bio content
    print(f"Bio: {bio}")
except Exception as e:
    bio = "Not found"
    print("Oops, couldn’t find Bio:", e)

# Fetch Location
try:
    location_xpath = '//span[@data-testid="UserLocation"]'  # XPath for location section
    location_element = wait.until(EC.presence_of_element_located((By.XPATH, location_xpath)))
    location = location_element.text  # Extract location content
    print(f"Location: {location}")
except Exception as e:
    location = "Not found"
    print("Oops, couldn’t find Location:", e)

# Fetch Website
try:
    website_xpath = '//a[@data-testid="UserUrl"]'  # XPath for website section
    website_element = wait.until(EC.presence_of_element_located((By.XPATH, website_xpath)))
    website = website_element.text  # Extract website content
    print(f"Website: {website}")
except Exception as e:
    website = "Not found"
    print("Oops, couldn’t find Website:", e)

# Save Scraped Data to CSV File
data = {
    "Username": [twitter_profile],
    "Bio": [bio],
    "Location": [location],
    "Website": [website],
    "Followers": [followers_count],
    "Following": [following_count]
}

# Generate unique filename with timestamp
filename = f"twitter_data_{time.strftime('%Y%m%d_%H%M%S')}.csv"
df = pd.DataFrame(data)  # Convert data dictionary to Pandas DataFrame
df.to_csv(filename, index=False)  # Save to CSV file without index
print(f"Saved data to {filename}")

# Close the browser
driver.quit()
print("All done!")
