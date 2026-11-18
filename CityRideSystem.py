from datetime import datetime
from DataManager import DataManager
from BikesManager import BikesManager
from RentalsManager import RentalsManager
from PricingManager import PricingManager
from Reports import Reports


class CityRideSystem:
    def __init__(self):
        self.bikes = DataManager.load_bikes()
        self.rentals = DataManager.load_rentals()
        self.rental_manager_instance = RentalsManager(self.bikes, self.rentals)

    def main_manager(self):
        user_choice = ""
        while user_choice != "4":
            print("""
==============================
       City ride system  
==============================
1. Bike manager
2. Rental manager
3. Reports
4. Exit""")
            user_choice = input("Chose an option (1-4): ")
            if user_choice == "1":
                self.bike_manager()
            elif user_choice == "2":
                self.rental_manager()
            elif user_choice == "3":
                self.reports_menu()
            elif user_choice == "4":
                print("bye!🙋")
            else:
                print("Invalid option! Please choose between 1 and 4.")

    def bike_manager(self):
        user_choice = ""
        while user_choice != "7":
            print("""
================================
          Bike manager  
================================
1. Show all bikes
2. Search bike by ID
3. Show available bikes
4. Add bike
5. Update bike details
6. Set bike operational or not
7. Back to Main menu""")
            user_choice = input("Chose an option (1-7): ").strip()
            if user_choice == "1":
                BikesManager.show_all_bikes(self.bikes)
            elif user_choice == "2":
                found = False
                while not found:
                    bike_id = CityRideSystem.validate_input("Enter bike ID: ")
                    if bike_id:
                        bike = BikesManager.search_bike_by_id(bike_id, self.bikes)
                    if bike:
                        BikesManager.show_bike(bike)
                        found = True
                    else:
                        print("Bike not found!")
            elif user_choice == "3":
                BikesManager.show_available_bikes(self.bikes)
            elif user_choice == "4":
                model = None
                while not model:
                    model = CityRideSystem.validate_input("Enter bike model: ").strip()
                valid_type = False
                b_type = ""
                while not valid_type:
                    b_type = CityRideSystem.validate_input("Enter bike type (Regular/Mountain/Electric): ").capitalize()
                    if b_type in ("Regular", "Mountain", "Electric"):
                        valid_type = True
                    else:
                        print("Invalid bike type! Please choose from Regular, Mountain, or Electric.")
                valid_h_price = False
                h_price = 0.0
                while not valid_h_price:
                    try:
                        h_price = float(input("Enter hourly price: ").strip())
                        if h_price <= 0:
                            print("Hourly price must be greater than 0.")
                            continue
                        valid_h_price = True
                    except ValueError:
                        print("Invalid price input! Please enter a valid number.")
                valid_d_price = False
                d_price = 0.0
                while not valid_d_price:
                    try:
                        d_price = float(input("Enter daily price: ").strip())
                        if d_price <= 0:
                            print("Daily price must be greater than 0.")
                            continue
                        valid_d_price = True
                    except ValueError:
                        print("Invalid price input! Please enter a valid number.")
                BikesManager.add_bike(self.bikes, model, b_type, h_price, d_price, True, True)
                print("New bike added successfully!")
            elif user_choice == "5":
                change_status = False
                while not change_status:
                    bike_id = CityRideSystem.validate_input("Enter bike ID: ")
                    if bike_id:
                        bike = BikesManager.search_bike_by_id(bike_id, self.bikes)
                        if not bike:
                            print("Bike not found!")
                            continue
                        try:
                            h_price_in = input("Enter new hourly price (press Enter to skip): ").strip()
                            d_price_in = input("Enter new daily price (press Enter to skip): ").strip()
                            h_price = int(h_price_in) if h_price_in else None
                            d_price = int(d_price_in) if d_price_in else None
                            BikesManager.update_bike(self.bikes, bike_id, hourly_price=h_price, daily_price=d_price)
                            print("Bike prices updated successfully!")
                            change_status = True
                        except ValueError:
                            print("Invalid price values!") 
            elif user_choice == "6":
                change_status = False
                while not change_status:
                    bike_id = CityRideSystem.validate_input("Enter bike ID: ")
                    if bike_id:
                        bike = BikesManager.search_bike_by_id(bike_id, self.bikes)
                        if not bike:
                            print("Bike not found!")
                            continue
                        is_operational = input("Enter operational status (y/n): ").strip().lower()
                        if is_operational in ("y", "n"):
                            is_op = (is_operational == "y")
                            BikesManager.update_bike(self.bikes, bike_id, is_operational=is_op)
                            change_status = True
                            print("Operational status updated!")
                            break
                        else:
                            print("Must be 'y' or 'n'!")
            elif user_choice == "7":
                print("Going back to Main menu...")
            else:
                print("Invalid option! Please choose between 1 and 7.")

    def rental_manager(self):
        user_choice = ""
        while user_choice != "6":
            print("""
================================
          Rental manager  
================================
1. New rental
2. Search rental by id
3. Search all customer rentals
4. Search all active rentals
5. Close rental
6. Back to Main menu""")
            user_choice = input("Chose an option (1-6): ")
            if user_choice == "1":
                customer_name = None
                while not customer_name:
                    customer_name = CityRideSystem.validate_input("Enter customer name: ")
                bike_id = None
                while not bike_id:
                    bike_id = CityRideSystem.validate_input("Enter bike ID: ")
                valid_dates = False
                start_dt, exp_dt = None, None
                while not valid_dates:
                    print("Enter start date & time (YYYY-MM-DD HH:MM)")
                    start_str = CityRideSystem.validate_input("Start datetime: ")
                    print("Enter expected return date & time (YYYY-MM-DD HH:MM)")
                    exp_str = CityRideSystem.validate_input("Expected return datetime: ")
                    try:
                        start_dt = datetime.fromisoformat(start_str.replace(" ", "T"))
                        exp_dt = datetime.fromisoformat(exp_str.replace(" ", "T"))
                        if start_dt > exp_dt:
                            print("Error: Start datetime cannot be later than expected return datetime.")
                            continue
                        valid_dates = True
                    except (ValueError, AttributeError):
                        print("Invalid datetime format! Please use YYYY-MM-DD HH:MM and try again.")
                success = self.rental_manager_instance.make_rental(customer_name, bike_id, start_dt, exp_dt)
                if success:
                    print("Rental created successfully!")
                else:
                    print("Failed to create rental! Check if bike exists, is operational, is available, or if dates are valid.")
            elif user_choice == "2":
                rental_id = None
                while not rental_id:
                    rental_id = CityRideSystem.validate_input("Enter rental ID: ")
                rental = self.rental_manager_instance.search_rental_by_id(rental_id)
                if rental:
                    print(f"ID: {rental.rental_id} | Customer: {rental.customer_name} | Bike: {rental.bike_id} | Status: {rental.status} | Total: {rental.total_price} ILS | Late Fee: {rental.late_fee} ILS")
                else:
                    print("Rental not found!")
            elif user_choice == "3":
                customer_name = None
                while not customer_name:
                    customer_name = CityRideSystem.validate_input("Enter customer name: ")
                c_rentals = self.rental_manager_instance.check_customer_rentals(customer_name)
                if c_rentals:
                    for r in c_rentals:
                        print(f"ID: {r.rental_id} | Bike: {r.bike_id} | Status: {r.status} | Total: {r.total_price} ILS")
                else:
                    print("No rentals found for this customer.")
            elif user_choice == "4":
                act_rentals = self.rental_manager_instance.check_active_rentals()
                if act_rentals:
                    for r in act_rentals:
                        print(f"ID: {r.rental_id} | Customer: {r.customer_name} | Bike: {r.bike_id} | Start: {r.start_datetime}")
                else:
                    print("No active rentals found.")
            elif user_choice == "5":
                rental_id = None
                while not rental_id:
                    rental_id = CityRideSystem.validate_input("Enter rental ID to close: ")
                valid_return_date = False
                act_dt = None
                while not valid_return_date:
                    print("Enter actual return date & time (YYYY-MM-DD HH:MM)")
                    act_str = CityRideSystem.validate_input("Actual return datetime: ")
                    try:
                        act_dt = datetime.fromisoformat(act_str.replace(" ", "T"))
                        valid_return_date = True
                    except (ValueError, AttributeError):
                        print("Invalid datetime format! Please try again.")
                success = self.rental_manager_instance.return_bikes(rental_id, act_dt)
                if success:
                    print("Rental closed and bike returned successfully!")
                else:
                    print("Failed to close rental! Check rental ID and verify the rental is active.")
            elif user_choice == "6":
                print("Going back to Main menu!")
            else:
                print("Invalid option! Please choose between 1 and 6.")

    def reports_menu(self):
        in_reports_menu = True
        while in_reports_menu:
            print("""
================================
         Reports Menu  
================================
1. Total rentals count
2. Active rentals count
3. Completed rentals count
4. Total revenue
5. Total late fees collected
6. Top customer
7. Most rented bike
8. Average rental price
9. Back to Main menu""")
            
            user_choice = input("Choose a report to generate (1-9): ").strip()
            if user_choice == "1":
                Reports.show_total_rentals(self.rentals)
            elif user_choice == "2":
                Reports.show_active_rentals_count(self.rentals)
            elif user_choice == "3":
                Reports.show_completed_rentals_count(self.rentals)
            elif user_choice == "4":
                Reports.show_total_revenue(self.rentals)
            elif user_choice == "5":
                Reports.show_total_late_fees(self.rentals)
            elif user_choice == "6":
                Reports.show_top_customer(self.rentals)
            elif user_choice == "7":
                Reports.show_most_rented_bike(self.rentals)
            elif user_choice == "8":
                Reports.show_average_rental_price(self.rentals)
            elif user_choice == "9":
                print("Returning to Main Menu...")
                in_reports_menu = False
            else:
                print("Invalid choice! Please select an option between 1 and 9.")
    
    @staticmethod
    def validate_input(prompt):
        is_valid = False
        val = ""
        while not is_valid:
            val = input(prompt).strip()
            if not val:
                print("Input cannot be empty! Please try again.")
            else:
                is_valid = True
        return val

if __name__ == "__main__":
    system = CityRideSystem()
    system.main_manager()
