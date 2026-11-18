from DataManager import DataManager
from Rental import Rental
from BikesManager import BikesManager
from PricingManager import PricingManager
from Bike import Bike
from datetime import datetime

class RentalsManager:

    def __init__(self, bikes, rentals):
        self.bikes = bikes
        self.rentals = rentals
        self.prices_calculation = PricingManager()
        
    def check_bike_available(self, bike_id):
        bike = BikesManager.search_bike_by_id(bike_id, self.bikes)
        if not bike:
            return None
        if not bike.is_available or not bike.is_operational:
            return None
        return bike

    def make_rental(self, customer_name, bike_id, start_datetime,expected_return_datetime):
        bike = self.check_bike_available(bike_id)
        if not bike:
            return False
        if start_datetime > expected_return_datetime or start_datetime < datetime.now():
            return False
        total_price =  PricingManager.calculate_price(start_datetime, expected_return_datetime, bike)
        rental_id = self.make_rental_id()
        r = Rental(rental_id, customer_name, bike_id, start_datetime, expected_return_datetime, total_price, "Active")
        bike.set_available(False) 
        DataManager.dump_bikes(self.bikes)
        self.rentals.append(r)
        DataManager.dump_rentals(self.rentals)
        return True

    def make_rental_id(self):
        if not self.rentals:
            return "R001"
        rental_id = max(int(rental.rental_id[1:]) for rental in self.rentals) + 1
        return f"R{rental_id:03d}"

    def search_rental_by_id(self, rental_id):
        for rental in self.rentals:
            if rental.rental_id == rental_id:
                return rental
        return None

    def check_customer_rentals(self, customer_name):
        return [rental for rental in self.rentals if rental.customer_name == customer_name]

    def check_active_rentals(self):
        return [rental for rental in self.rentals if rental.status == "Active"]

    def return_bikes(self, rental_id, actual_return_datetime):
        active_rentals = self.check_active_rentals()
        rental = self.search_rental_by_id(rental_id)
        if not rental or rental not in active_rentals:
            return False
        late_fee = PricingManager.calculate_fee(rental, actual_return_datetime)
        rental.complete_rental(actual_return_datetime, late_fee)
        rental.status = "Completed"
        bike = BikesManager.search_bike_by_id(rental.bike_id, self.bikes)
        if bike:
            bike.set_available(True)
        DataManager.dump_bikes(self.bikes)
        DataManager.dump_rentals(self.rentals)
        return True
    