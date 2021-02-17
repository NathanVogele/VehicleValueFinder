
# Vehicle Value - Average Price is the main function we are using right now, but we are building out the other elements for future
# feature development. 

class Vehicle:
    def __init__(self,vin,details,mileage,certainty,meanPrice,averagePrice,belowPrice):
        self.vin = vin
        self.details = details
        self.mileage = mileage
        self.certainty = certainty
        self.meanPrice = meanPrice
        self.averagePrice = averagePrice
        self.belowPrice = belowPrice