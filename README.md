# Property Scraper

This script scrapes property listings from `rumah.com` for properties located in Yogyakarta. The script captures details such as title, location, price, number of bedrooms and bathrooms, features, and the URL of the listing.

## Dependencies

This script uses several Python libraries:

- `cloudscraper`: To bypass Cloudflare's anti-bot measures.
- `BeautifulSoup`: For parsing and navigating the HTML content.
- `requests`: To make HTTP requests.
- `csv`: To write the scraped data into a CSV file.
- `datetime`: To generate timestamps.

We use `poetry` to manage these dependencies.

## Setup

1. Ensure you have Python installed.
2. Install `poetry`:
   ```bash
   pip install poetry
   ```

3. Navigate to the script's directory and install the dependencies using:
   ```bash
   poetry install
   ```

## Running the Script

To run the script, use the following command:

```bash
poetry run python3 rumahcom-scrape.py
```

This will start the scraping process. The script will navigate through the paginated listings, and for each property, it will capture the required details and write them into a CSV file named `jogja_properties_<timestamp>.csv`.

## Notes

- The script includes error handling to manage connection issues and retries failed requests up to 5 times.
- To avoid being blocked, the script waits for a random duration between 10 to 35 seconds between requests.

---

You can save the above content into a `README.md` file in the root directory of your script. Adjustments can be made as per your requirements.