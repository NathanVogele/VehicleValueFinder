import requests
from models import Vehicle
from bs4 import BeautifulSoup

# Function is referenced in main.py
# Requires a single vin number to make
# the API request.

def findVehicleValue(lookupVin):

    # Don't Forget To Replace This With Your Own API Key
    api_key = "YOUR_VINAUDIT_API_KEY"

    # VinAudit lets you specify a milage as well, you could easily
    # add an additional spreadsheet field and pull specific values
    # with an actual vehicle mileage.
    # ##### 
    # For my purposes, I've left the average mileage attribute because
    # the lists I run generally don't have a users upto date vehicle
    # mileage. 


    response = requests.get('http://marketvaluev1.vinaudit.com/getmarketvalue.php', params={'key':api_key,'vin':lookupVin,'format':'xml','period':'90','mileage':'average'})

    soup = BeautifulSoup(response.text, 'xml')

    # BS4 by default returns an object, so you want to seperate that to a string for use later in thhe
    # main program. 

    current_vin = soup.find('vin').string
    current_details = soup.find('vehicle').string
    current_mileage = soup.find('mileage').string
    current_certainty = soup.find('certainty').string
    current_mean = soup.find('mean').string
    current_average_price = soup.find('average').string
    current_below_price = soup.find('below').string

    # Builds the object and returns it at the end of the program to be
    # added to a list.

    # I've built a more robust object that will utilize the full response from the API -- You may use any of these attributes 
    # to build a database of customer vehicle information simply from their vin # with these attributes. 

    vehicle = Vehicle(current_vin,current_details,current_mileage,current_certainty,current_mean,current_average_price,current_below_price)

    # valueList = [current_vin,current_details,current_mileage,current_certainty,current_mean,current_average_price,current_below_price]
    
    # Very useful for checking a vehicles value as the program is running. 
    print(vehicle.averagePrice)

    return vehicle

