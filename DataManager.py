import json
from pathlib import Path
from Bike import Bike
from Rental import Rental

# Constant Variable change to uppercase
base_path = Path(__file__).parent
bikes_file = base_path / "bikes.json"
rentals_file = base_path / "rentals.json"

class DataManager:
    
    @staticmethod
    def load_bikes():
        try:
            with open(bikes_file, "r", encoding="utf-8") as js:
                data = json.load(js)
                return [Bike.dict_from(d) for d in data] if data else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    @staticmethod
    def load_rentals():
        try:
            with open(rentals_file, "r", encoding="utf-8") as js:
                data = json.load(js)
                return [Rental.dict_from(d) for d in data] if data else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    @staticmethod
    def dump_bikes(bikes):
        try:
            with open(bikes_file, "w", encoding="utf-8") as js:
                json.dump([b.to_dict() for b in bikes], js, indent=2)
                return True
        except FileNotFoundError:
            return False
    
    @staticmethod
    def dump_rentals(rentals):
        try:
            with open(rentals_file, "w", encoding="utf-8") as js:
                json.dump([r.to_dict() for r in rentals], js, indent=2)
                return True
        except FileNotFoundError:
            return False