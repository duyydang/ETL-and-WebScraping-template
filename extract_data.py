import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'


def extract_from_url():
    df = pd.DataFrame(columns=['Rank', 'Name', 'MC_USD_Billion'])

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    # Get body
    table = soup.find_all('tbody')
    rows = table[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            # Name have \n and I replaced this.
            data_dict = {'Rank': int(
                col[0].text), 'Name': str(col[1].text).replace('\n', ''), 'MC_USD_Billion': float(col[2].text)}
            data_temp = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, data_temp], ignore_index=True)

    return df
