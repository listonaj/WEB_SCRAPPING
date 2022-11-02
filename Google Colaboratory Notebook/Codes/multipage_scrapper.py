# Group work Clark College : Web Scrapping - Real Estate - Houses's prices in Correlation with crime index in Portland, OR
# NTEC 365 - BIG DATA ANALYTICS
# Phase 1 - Gathering Data - This code take into consideration multiple web pages data gathering
# Date : 10/28/2022
# group members:
#               Treyce 
#               Elias
#               Georgette
#               Jean-Marc : Coded by Jean-Marc Romain
#
# Note : if you run the code make sure to update the upi key with your personal key, 
# the one provided by in code is no longer active. Visit https://api.webscrapingapi.com, 
# create an account to get your api-key.

# the data colected has been saved in a csv file that you can find in the Data folder 

# Importing the BS4, Requests, and Pandas modules
from bs4 import BeautifulSoup 
import pandas as pd
import requests

def main():
  
  # declare the variables of type list
  prices = []
  beds = []
  baths = []
  sizes = []
  addresses = []

  #page starts at 1
  page = 1
  
  # Loop until reach the last page
  # my loop start here
  while page!=86:

    # My API Headers and Request
    url = "https://api.webscrapingapi.com/v1"
    params = {"api_key": "eBiY1EnI2X1RnBFG7mYXpoNhdmrLLhPN","url": 
       f"https://www.realtor.com/realestateandhomes-search/Portland_OR/pg-{page}"}
    res = requests.request("GET", url, params=params)

    # loading the web page in the variable soup 
    soup = BeautifulSoup(res.content, 'html.parser')

    # finding the list of houses on Sale in Portland, OR
    lists = soup.find_all('li', class_='jsx-1881802087 component_property-card')

    # nested loop  - scrapping elements that discribe the house on sale
    for element in lists:
      price = element.find('span', attrs={'data-label': 'pc-price'})
      bed = element.find('li', attrs={'data-label': 'pc-meta-beds'})
      bath = element.find('li', attrs={'data-label': 'pc-meta-baths'})
      size = element.find('li', attrs={'data-label': 'pc-meta-sqft'})
      address = element.find('div', attrs={'data-label': 'pc-address'})
      if bed and bath:
        nr_beds = bed.find('span', attrs={'data-label': 'meta-value'})
        nr_baths = bath.find('span', attrs={'data-label': 'meta-value'})
        if nr_beds and float(nr_beds.text) >= 2 and nr_baths and float(nr_baths.text) >= 1:
           # '.text' only extract the text value 
           beds.append(nr_beds.text)
           baths.append(nr_baths.text)

           if price and price.text:
               prices.append(price.text)
           else:
               prices.append('No display data')

           if size and size.text:
               sizes.append(size.text)
           else:
               sizes.append('No display data')

           if address and address.text:
               addresses.append(address.text)
           else:
               addresses.append('No display data')  
    
    #update page number at end of loop cycle    
    page = page + 1

  # create a csv file containing data gathered (5 columns for 5 lists)
  df = pd.DataFrame({'Address': addresses, 'Price': prices, 'Beds': beds, 'Baths': baths, 'Sizes': sizes})
  df.to_csv('listings.csv', index=False, encoding='utf-8')   


    
main()