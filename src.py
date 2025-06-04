import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define Flipkart search URL for mobiles under ₹70000
flipkart_url = "https://www.flipkart.com/search?q=mobile+under+70000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_6_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+7000&requestId=55ab0416-7d35-4251-9087-d26dcab4b634&as-searchtext=mobile"

# Set up User-Agent rotation
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
]

# Configure Selenium with Chrome options
options = Options()
options.add_argument(f'user-agent={user_agents[0]}')
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

# Navigate to Flipkart's page
driver.get(flipkart_url)

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract product details
mobiles = []
for mobile in soup.find_all('div', {'class': '_4rR01T'}):  # Extract mobile names
    price = mobile.find_next('div', {'class': '_30jeq3 _1_WHN1'})  # Extract price
    if mobile and price:
        mobiles.append({
            "Product": mobile.text.strip(),
            "Price": price.text.strip()
        })

# Display extracted data
for item in mobiles:
    print(f"{item['Product']} - {item['Price']}")

# Close Selenium driver
driver.quit()
