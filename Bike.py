class Bike:
    def __init__(self, bike_id, model, bike_type, hourly_price, daily_price, is_available, is_operational):
        self._bike_id = bike_id
        self._model = model
        self._bike_type = bike_type
        self._hourly_price = hourly_price
        self._daily_price = daily_price
        self._is_operational = is_operational
        self._is_available = is_available if is_operational else False

    @property
    def bike_id(self):
        return self._bike_id

    @property
    def model(self):
        return self._model

    @property
    def bike_type(self):
        return self._bike_type

    @property
    def hourly_price(self):
        return self._hourly_price

    @hourly_price.setter
    def hourly_price(self, value):
        if value < 0:
            raise ValueError("Hourly price cannot be negative.")
        self._hourly_price = value

    @property
    def daily_price(self):
        return self._daily_price

    @daily_price.setter
    def daily_price(self, value):
        if value < 0:
            raise ValueError("Daily price cannot be negative.")
        self._daily_price = value

    @property
    def is_operational(self):
        return self._is_operational

    @is_operational.setter
    def is_operational(self, status):
        self._is_operational = status
        if not status:
            self._is_available = False

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, status):
        if status and not self._is_operational:
            raise ValueError("Cannot make bike available because it is not operational!")
        self._is_available = status

    def to_dict(self):
        return {
            "bike_id": self._bike_id,
            "model": self._model,
            "bike_type": self._bike_type,
            "hourly_price": self._hourly_price,
            "daily_price": self._daily_price,
            "is_available": self._is_available,
            "is_operational": self._is_operational
        }
    
    @classmethod
    def dict_from(cls, data):
        return cls(
            bike_id = data["bike_id"],
            model = data["model"],
            bike_type = data["bike_type"],
            hourly_price = data["hourly_price"],
            daily_price = data["daily_price"],
            is_available = data["is_available"],
            is_operational = data["is_operational"]
        )
    
    def set_available(self, status):
        self.is_available = status  

    def set_operational(self, status):
        self.is_operational = status 