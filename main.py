from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep

import pandas as pd  # manipulate the date


def get_currencies(currencies, start, end, export_csv=False):
    frames = []  # store data for each currency

    # Get the historic data between USD and other currencies
    for currency in currencies:
        while True:
            try:
                #
                my_url = f"https://investing.com/currencies/usd-{currency.lower()}-historical-data"
                option = Options()
                option.add_experimental_option("excludeSwitches", ["enable-logging"])
                option.headless = False  # Make the actions visible
                driver = webdriver.Chrome(options=option)
                driver.get(my_url)
                print("Got the URL.")
                driver.maximize_window()
                print("Maximized window.")
                sleep(5)

                # Accept the cookies, otherwise the prompt does not go away...
                cookies_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
                )
                cookies_button.click()
                print("Accepted the cookies.")
                sleep(5)

                # Click on the date button to change the range
                date_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "flatDatePickerCanvasHol"
                            # By.XPATH,
                            # "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span",
                        )
                    )
                )
                date_button.click()
                print("Clicked the date button.")
                sleep(5)

                # Select Start and End Date, clear their contents and input our own
                start_bar = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[7]/div[1]/input[1]")
                    )
                )
                start_bar.clear()
                start_bar.send_keys(start)
                print("Entered the start date.")
                sleep(5)

                end_bar = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[7]/div[1]/input[2]")
                    )
                )
                end_bar.clear()
                end_bar.send_keys(end)
                print("Entered the end date.")
                sleep(5)

                # Click the apply button and wait a bit
                apply_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[5]/a"))
                )
                apply_button.click()
                print("Clicked 'Apply'.")
                sleep(5)

                # Get the source code of the page that appeared with pandas
                # Use the default read_html flavor parameter (lxml)
                dataframes = pd.read_html(driver.page_source)
                # From the webpage source code we collected, keep only the table containing the historical data
                for dataframe in dataframes:
                    # print(dataframe.columns.tolist())
                    if dataframe.columns.tolist() == [
                        "Date",
                        "Price",
                        "Open",
                        "High",
                        "Low",
                        "Change %",
                    ]:
                        frames.append(dataframe)
                        df = dataframe
                        break
                # print(frames)
                frames.append(df)

                # Export to csv if asked by function argument
                if export_csv:
                    df.to_csv("currency.csv", index=False)
                    print(f"{currency}.csv exported")
                driver.quit()
                print(f"{currency} scraped.")
                break
            except:
                driver.quit()
                print(f"Failed to scrape {currency}. Trying again in 10 seconds.")
                sleep(10)
                continue
    return frames


print(get_currencies(["EUR"], "01/01/2020", "01/01/2021", True))
