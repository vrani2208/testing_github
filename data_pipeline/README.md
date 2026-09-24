%%writefile README.md
%%writefile README.md

# Data Pipeline

## Overview

This module implements an end-to-end data engineering pipeline for scraping, cleaning, converting, storing, and querying book catalogue data.

The data is collected from Books to Scrape, a public website designed for scraping practice.

## Data Collection

The pipeline scrapes the first five pages of the All Products catalogue.

Each page contains approximately 20 books, resulting in approximately 100 scraped books.

From the scraped dataset, 60 books are selected for the project.

The selected dataset contains at least three different book categories.

The scraping process is automated and does not require manual copy-pasting of data.

## Libraries Used

The following Python libraries are used:

- requests
- BeautifulSoup
- pandas
- sqlite3

## Data Cleaning

The following transformations are applied:

- The pound symbol is removed from the price field.
- The cleaned price is converted to a float column named `price_gbp`.
- Star ratings such as One, Two, Three, Four, and Five are converted to integers from 1 to 5.
- Availability text is converted into a boolean column named `in_stock`.
- If a numeric field fails to parse, the median value is used for imputation.

## Currency Conversion

The project uses the required fixed project-defined conversion rate:

**1 GBP = 105.50 INR**

The INR price is calculated as:

```text
price_inr = price_gbp * 105.50  
