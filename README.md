# Comfy Scraping Project

This project uses the Scrapy framework for parsing product data from the comfy.ua/ua website. Its purpose is to get information about various products such as name, price, category, availability, etc.
***

# Installation
## First, clone the repository:

git clone https://github.com/kovalenko1927/data_parser
***

## Navigate to the project directory:
cd data_parser
***

### It is recommended to use a Python virtual environment to isolate the project dependencies. Create a virtual environment and activate it:
python3 -m venv venv

source venv/bin/activate
***

## Install the project dependencies from the requirements.txt file:
pip install -r requirements.txt
***

## Running the Scraper
### The scraper can be executed using the following command:
make run
***
### The parsing results will be saved in CSV file

## Running analytics script
make analytic
***