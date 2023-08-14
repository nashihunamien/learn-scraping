import time
import random
import csv
import cloudscraper
import requests
from datetime import datetime
from bs4 import BeautifulSoup

BASE_URL = "https://www.rumah.com"
START_URL = BASE_URL + "/properti-dijual/1?freetext=DI+Yogyakarta&maxprice=0&maxsize=0&minprice=0&minsize=0&region_code=IDYO"

# Current date for filename and metadata
current_date = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"jogja_properties_{current_date}.csv"

# CSV file setup
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Location", "Price", "Bedrooms", "Bathrooms", "Features", "URL", "Created_Date"])

    scraper = cloudscraper.create_scraper()
    def fetch_page(url, retries=5):
        for attempt in range(retries):
            try:
                print(f"Fetching page: {url}")  # Display the current page being scanned
                return scraper.get(url)
            except (Exception, requests.exceptions.ConnectionError) as e:
                if attempt < retries - 1:  # i.e. if it's not the last attempt
                    print(f"Error fetching page: {e}. Retrying in a few seconds...")
                    time.sleep(random.randint(10, 35))
                else:
                    raise


    response = fetch_page(START_URL)  # Use fetch_page here
    soup = BeautifulSoup(response.content, 'html.parser')

    while True:
        time.sleep(random.randint(10, 35))  # Random sleep time between 10 to 35 seconds
        properties = soup.find_all('div', class_='listing-card')


        for prop in properties:
            title_tag = prop.find('a', {'data-automation-id': 'listing-card-title-txt'})
            title = title_tag.text if title_tag else "N/A"
            url = title_tag['href'] if title_tag else "N/A"
            
            location_tag = prop.find('span', {'data-automation-id': 'listing-card-street-address-txt'})
            location = location_tag.text if location_tag else "N/A"
            
            price_tag = prop.find('li', {'data-automation-id': 'listing-card-price-txt'})
            price = price_tag.text.strip() if price_tag else "N/A"
            
            features_tag = prop.find('ul', {'data-automation-id': 'listing-card-other-details-txt'})
            features = [feature.text for feature in features_tag.find_all('li')] if features_tag else []
            
            bed_tag = prop.find('span', class_='bed')
            bed = bed_tag.text.strip() if bed_tag else "N/A"
            
            bath_tag = prop.find('span', class_='bath')
            bath = bath_tag.text.strip() if bath_tag else "N/A"
            
            writer.writerow([title, location, price, bed, bath, ', '.join(features), BASE_URL + url, current_date])

        # Check for the next page
        next_page = soup.find('li', class_='pagination-next')
        if next_page:
            next_page_link = next_page.find('a')
            if next_page_link:
                time.sleep(random.randint(10, 35))
                response = fetch_page(BASE_URL + next_page_link['href'])  # Use fetch_page here
                soup = BeautifulSoup(response.content, 'html.parser')
            else:
                break
        else:
            break