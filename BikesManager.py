from Bike import Bike
from DataManager import DataManager

class BikesManager:
    @staticmethod
    def show_bike(bike):
        if not bike.is_available:
            a_answer = " not"
        else:
            a_answer = ""
        if not bike.is_operational:
            o_answer = " not"
        else:
            o_answer = ""
        print(f"{bike.bike_id}: model- {bike.model}, bike type- {bike.bike_type}, hourly price- {bike.hourly_price}, daily price- {bike.daily_price}, the bike is{a_answer} available and{o_answer} operational.")

    @staticmethod
    def show_all_bikes(bikes):
        for bike in bikes:
            BikesManager.show_bike(bike)

    @staticmethod
    def search_bike_by_id(bike_id, bikes):
        for bike in bikes:
            if bike.bike_id == bike_id:
                return bike
        return None

    @staticmethod
    def show_available_bikes(bikes):
        counter = 0
        for bike in bikes:
            if bike.is_available:
                counter += 1
                print(f"{bike.bike_id}: model- {bike.model}, bike type- {bike.bike_type}, hourly price- {bike.hourly_price}, daily price- {bike.daily_price}")
        if not counter:
            print("There aren't bikes available!")

    @staticmethod
    def make_bike_id(bikes):
        if not bikes:
            return "B001"
        next_id = max(int(bike.bike_id[1:]) for bike in bikes) + 1
        return f"B{next_id:03d}"

    @staticmethod
    def add_bike(bikes, model, bike_type, hourly_price, daily_price, is_available, is_operational):
        bike_id = BikesManager.make_bike_id(bikes)
        b = Bike(bike_id, model, bike_type, hourly_price, daily_price, is_available, is_operational)
        bikes.append(b)
        DataManager.dump_bikes(bikes)

    @staticmethod
    def update_bike(bikes, bike_id, hourly_price = None, daily_price = None, is_operational = None):
        bike = BikesManager.search_bike_by_id(bike_id, bikes)
        if hourly_price is not None:
            bike.hourly_price = hourly_price
        if daily_price is not None:
            bike.daily_price = daily_price
        if is_operational is not None:
            bike.set_operational(is_operational)
        DataManager.dump_bikes(bikes)      
