class Reports:

    @staticmethod
    def show_total_rentals(rentals):
        print(f"\n[Report] Total Rentals Executed: {len(rentals)}")

    @staticmethod
    def show_active_rentals_count(rentals):
        active_count = len([r for r in rentals if r.status == "Active"])
        print(f"\n[Report] Currently Active Rentals: {active_count}")

    @staticmethod
    def show_completed_rentals_count(rentals):
        completed_count = len([r for r in rentals if r.status == "Completed"])
        print(f"\n[Report] Completed Rentals: {completed_count}")

    @staticmethod
    def show_total_revenue(rentals):
        completed_rentals = [r for r in rentals if r.status == "Completed"]
        total_revenue = sum(r.total_price for r in completed_rentals)
        print(f"\n[Report] Total Revenue from Completed Rentals: {total_revenue:.2f} ILS")

    @staticmethod
    def show_total_late_fees(rentals):
        completed_rentals = [r for r in rentals if r.status == "Completed"]
        total_late_fees = sum(r.late_fee for r in completed_rentals)
        print(f"\n[Report] Total Late Fees Collected: {total_late_fees:.2f} ILS")

    @staticmethod
    def show_top_customer(rentals):
        customer_counts = {}
        for r in rentals:
            customer_counts[r.customer_name] = customer_counts.get(r.customer_name, 0) + 1
        if customer_counts:
            top_customer = max(customer_counts, key=customer_counts.get)
            count = customer_counts[top_customer]
            print(f"\n[Report] Top Customer: {top_customer} ({count} rentals)")
        else:
            print("\n[Report] No rental data available.")

    @staticmethod
    def show_most_rented_bike(rentals):
        bike_counts = {}
        for r in rentals:
            bike_counts[r.bike_id] = bike_counts.get(r.bike_id, 0) + 1
        if bike_counts:
            top_bike_id = max(bike_counts, key=bike_counts.get)
            count = bike_counts[top_bike_id]
            print(f"\n[Report] Most Rented Bike ID: {top_bike_id} ({count} times)")
        else:
            print("\n[Report] No rental data available.")

    @staticmethod
    def show_average_rental_price(rentals):
        completed_rentals = [r for r in rentals if r.status == "Completed"]
        completed_count = len(completed_rentals)
        total_revenue = sum(r.total_price for r in completed_rentals)
        if completed_count > 0:
            avg_price = total_revenue / completed_count
            print(f"\n[Report] Average Rental Price: {avg_price:.2f} ILS")
        else:
            print("\n[Report] No completed rentals to calculate average price.")