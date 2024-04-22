# Web Scraper With Selenium

## Overview
This Python script is designed to scrape data from a webpage, including links, images, titles, and emails, and save the extracted data into an Excel file.

## Features
- Extracts inner and outer links from the webpage.
- Downloads images from the webpage and saves them locally.
- Retrieves titles and emails from the webpage.
- Generates an Excel file containing the extracted data.

## Requirements
- Python 3.x
- Selenium
- Requests
- BeautifulSoup4
- Pandas
- ChromeDriver (for Selenium WebDriver)

## Installation
1. Clone or download the repository.
2. Install the required Python packages using pip:
    ```
    pip install -r requirements.txt
    ```
    Make sure to run this command from the directory where the `requirements.txt` file is located.

3. Use the ChromeDriver in the git repository **or** download the latest ChromeDriver executable and place it in your system PATH and specify the path to it in the script.

## Usage
1. Instantiate the `webScraper` class with the URL of the webpage you want to scrape.
    ```python
    url = "https://example.com"
    bot = webScraper(url)
    ```
2. Run all scraping functions using the `runAllFunctions()` method.
    ```python
    bot.runAllFunctions()
    ```
3. Generate the Excel file containing the scraped data using the `makeExcelSheet()` method.
    ```python
    bot.makeExcelSheet()
    ```

## Example Code Snippet
```python
url = "https://www.monolithai.com/blog/4-ways-ai-is-changing-the-packaging-industry"
bot = webScraper(url)
bot.runAllFunctions()
bot.makeExcelSheet()
```
## Example Excel File and Image Directory
**If you run above snippet (which is in python file by default) you get**
- An Excel file named `monolithai.xlsx` containing the scraped data will be generated after running the script.
- Images from the webpage is saved in a directory named `monolithai`.

*example excel file and images directory are in repository*

Note: Please make sure to have proper permissions to create directories and write files in the script execution directory.

## Author
- Abhai Matta