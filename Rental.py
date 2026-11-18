from datetime import datetime

class Rental:
    def __init__(self, rental_id, customer_name, bike_id, start_datetime, expected_return_datetime, total_price, status, actual_return_datetime=None, late_fee = 0.0):
        self._rental_id = rental_id
        self._customer_name = customer_name
        self._bike_id = bike_id
        self._start_datetime = start_datetime
        self._expected_return_datetime = expected_return_datetime
        self._actual_return_datetime = actual_return_datetime
        self._total_price = total_price
        self._late_fee = late_fee
        self._status = status

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def bike_id(self):
        return self._bike_id

    @property
    def start_datetime(self):
        return self._start_datetime

    @property
    def expected_return_datetime(self):
        return self._expected_return_datetime

    @property
    def actual_return_datetime(self):
        return self._actual_return_datetime

    @property
    def total_price(self):
        return self._total_price

    @property
    def late_fee(self):
        return self._late_fee

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if self._status == "Completed":
            raise ValueError("Error: Cannot modify a rental that has already been completed!")
        if new_status not in ("Active", "Completed"):
            raise ValueError("Invalid status value.")
        self._status = new_status

    def to_dict(self):
        return {
            "rental_id": self._rental_id,
            "customer_name": self._customer_name,
            "bike_id": self._bike_id,
            "start_datetime": datetime.isoformat(self._start_datetime),
            "expected_return_datetime": datetime.isoformat(self._expected_return_datetime),
            "actual_return_datetime": self._actual_return_datetime.isoformat() if isinstance(self._actual_return_datetime, datetime) else self._actual_return_datetime,
            "total_price": self._total_price,
            "late_fee": self._late_fee,
            "status": self._status
        }
    
    @classmethod
    def dict_from(cls, data):
        return cls(
            rental_id = data["rental_id"],
            customer_name = data["customer_name"],
            bike_id = data["bike_id"],
            start_datetime = datetime.fromisoformat(data["start_datetime"]),
            expected_return_datetime = datetime.fromisoformat(data["expected_return_datetime"]),
            actual_return_datetime = datetime.fromisoformat(data["actual_return_datetime"]) if data.get("actual_return_datetime") else None,
            total_price = data["total_price"],
            late_fee = data["late_fee"],
            status = data["status"]
        )

    def complete_rental(self, return_datetime, late_fee):
        if self._status == "Completed":
            raise ValueError("This rental is already completed.")
        if isinstance(return_datetime, str):
            self._actual_return_datetime = datetime.fromisoformat(return_datetime)
        else:
            self._actual_return_datetime = return_datetime
        self._late_fee = late_fee
        self.status = "Completed" 