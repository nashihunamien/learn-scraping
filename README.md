# Learn-Scrape: A Python Web Scraping Project

`Learn-Scrape` is a Python project focused on web scraping various websites. The initial version targets `rumah.com` for property listings, but more websites will be added in the future.

## Dependencies

The project uses several Python libraries:

- `beautifulsoup4`: For parsing and navigating the HTML content.
- `requests`: To make HTTP requests.
- `cloudscraper`: To bypass Cloudflare's anti-bot measures.

We use `poetry` to manage these dependencies.

## Setup

### Prerequisites

- Ensure you have Python 3.11 or newer installed.
- Install `poetry`:
   ```bash
   pip install poetry
   ```

### Installation

1. Clone the `learn-scrape` repository to your local machine.
2. Navigate to the project's directory.
3. Install the dependencies using:
   ```bash
   poetry install
   ```

## Running the Script

To run the script, use the following command:

```bash
poetry shell
python3 main.py
```

This will start the scraping process for `rumah.com`. The script will navigate through the paginated listings, capturing the required details and writing them into a CSV file.

## Future Plans

- Add more websites to the scraping list.
- Enhance error handling and optimize the scraping process.
- Integrate with databases for structured storage of scraped data.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.
