from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# Step 1: Set up Chrome WebDriver with WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Open the Google Scholar Profile URL
driver.get('https://scholar.google.co.in/citations?hl=en&user=gWHstAoAAAAJ&view_op=list_works')

# Step 3: Keep clicking "Show more" button until it's no longer available
while True:
    try:
        # Find the "Show more" button by its class or other identifiers
        show_more_button = driver.find_element("xpath", '//button[@id="gsc_bpf_more"]')  # Example: find by id
        if show_more_button:
            show_more_button.click()
            time.sleep(2)  # Give time for new publications to load
    except (ElementClickInterceptedException, NoSuchElementException):
        print("No more 'Show more' button found, all publications loaded.")
        break

# Step 4: Get page source after loading all publications
page_source = driver.page_source

# Step 5: Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'lxml')

# Step 6: Find all publications (assumes publications are within <a> tags with class 'gsc_a_at')
publications = soup.find_all('a', class_='gsc_a_at')

# Step 7: Extract and print the publication titles
with open('publications.txt', 'w', encoding='utf-8') as file:
    for pub in publications:
        title = pub.get_text()
        file.write(title + '\n')
        print(title)  # Print the title to the console

# Step 8: Close the Selenium WebDriver
driver.quit()
