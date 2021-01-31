# ScrapingBot

A scraping bot with python using the selenium library and pandas.</br>
Based on [How to Code a Scraping Bot with Selenium and Python](https://www.freecodecamp.org/news/how-to-code-a-scraping-bot-with-selenium-and-python/).

## Installation

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Selenium](https://www.selenium.dev/), [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html#) and [lxml](https://lxml.de/index.html).

```cmd
pip install selenium
pip install pandas
pip install lxml
```

- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (make sure it matches the browser's version)</br>
  Extract executable in _C://Users//{username}//AppData//Local//Programs//Python//Python{version}_ or _C://Program Files[(x86)]?//Python{version}_, depending on where you installed Python

## Debugging

- [Bluetooth: Getting Default Adapter Failed](https://stackoverflow.com/questions/61561112/how-to-solve-getting-default-adapter-failed-error-when-launching-chrome-and-tr)

## Bugs

- Sometimes (but not consistently), the website will show a "Subscribe to newsletter" popup, which will break the iteration and the program will run again

## TODO

- Return data for multiple currencies
- Update function that receives an existing dataframe and returns historical data up to today
