from bs4 import BeautifulSoup
from datetime import datetime
import requests

# Create instance of Data time and format it 
current_data = datetime.now().strftime("%Y-%m-%d")

# Format the url
url = f"https://bg.fuelo.net/prices/date/{current_data}?lang=bg"

# Use formatted url for real get request
html_content = requests.get(url).text
soups = BeautifulSoup(html_content, 'html')

div_table_content = soups.find('div', class_='table-responsive')

table_content = div_table_content.find('table')

# Take all table headers
table_head = table_content.find('thead')
# Take only first tr because there is our needed headers
table_headers = table_head.find('tr')

table_titles = table_headers.find_all('th')
fuels = []
# Save data from table in list
for title in table_titles[1:]:
    fuels.append(title.text)

# Take inflation price from table head
price_rise = []
header_prices = table_head.find_all('tr')[1:]
for buff_prices in header_prices:
    all_buff_prices = buff_prices.find_all('sup')
    for price in all_buff_prices:
        price_rise.append(price.text.strip())

# Take all data's in the table body
table_body = table_content.find('tbody')

# Take all rows
table_rows = table_body.find_all('tr')

brands_fuels_prices = []
for row in table_rows:
    cur_dictionary = {}
    # Take only brands
    brand = row.find('td').text.strip()
    # Take all prices for our fuel from the table
    prices = row.find_all('td')[1:]
    # Save brand in dictionary
    cur_dictionary['brand'] = brand
    # Create var 'interaction' for looping our fuels and take them by index
    interaction = 0
    for price in prices:
        text_price = price.text.strip()
        # Check if the fuel has no price
        if text_price == '':
            text_price = 'empty'
        
        cur_dictionary[fuels[interaction]] = text_price
        interaction += 1
    
    brands_fuels_prices.append(cur_dictionary)

print(brands_fuels_prices)