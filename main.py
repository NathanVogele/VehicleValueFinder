######################################################
##         VEHICLE VALUE FINDER - RELEASE 1.0       ##
######################################################
# This program is designed to take in a single row   #
# of vehicle VIN numbers & ping the VinAudit API     #
# the API returns High, Average & Low value numbers. #
# In order to use this program you need an API-Key   #
# You may obtain one by contacting VINAudit.com      #
######################################################

# PROGRAM REQUIRES PANDA & BS4  
from models import Vehicle
import pandas as pd
import api_lookup
import excel_import
import excel_export
import os

# This is the place you are going to link your xlsx file to. 
# Panda is extremely robust so with a little tinkering you can
# easily convert this from taking an .xlsx to a .csv or other
# spreadsheet style file. 


# I highly recommend setting up a test file with 2 - 4 vins 
# and running that before you actually run the full list. 
# this will save you a lot of money on API calls. 

# Please add vins to the excel import folder, that'll process them here.

excel_file = "excel_import/Vin_Builder.xlsx"

# Opens the spreadsheet as a dataframe. This program
# is setup to take a one sheet file, with only a vin number.
customers = pd.read_excel(excel_file)

# Ensure that before hand, your vins are formatted with the
# header "Vehicle VIN" so Panda knows what to put into a list.

vehicle_vins = customers['Vehicle VIN'].tolist()

# We clean the list from any spaces to prevent errorrs with the API
cleaned_vehicle_vins = [x.replace(' ', '') for x in vehicle_vins]
print(cleaned_vehicle_vins)

# Use API to pull vehicle average value
api_vehicles = []

# References the flie api_lookup - pulls the API functionality from there.
for i in cleaned_vehicle_vins:
    try:
        vehicle = api_lookup.findVehicleValue(i)
        print(vehicle.averagePrice)
        api_vehicles.append(vehicle)
    except:
        # A bit of error catching. 
        api_vehicles.append("Bad Vin")
        print("Bad Vin")
        pass

# Add the values from the object to seperate into an individual list
vehicle_values = []
for vehicle in api_vehicles:
    try:
        print(vehicle.averagePrice)
        vehicle_values.append(vehicle.averagePrice)
    except:
        # A bit more error handling, this will show you on your
        # spreadsheet where the vin failed to successfully lookup
        # thanks to the magic of beautifulSoup it will throw an 
        # error if the object from earlier isn't a BS4 object.
        print("Error has occured")
        vehicle_values.append("Bad Vin")
        pass

# Uses the DataFrame customers and inserts the values from the above API calls into 
# the final list, preparing it for exprt.
customers.insert(0,"Vehicle Value", vehicle_values,allow_duplicates = False)

# gives you a preview of what the file looks like before it writes.
print(customers.head())

customers.to_excel("excel_export/output.xlsx") # exporting file sheet.