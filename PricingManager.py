from datetime import timedelta, datetime

class PricingManager:

    @staticmethod
    def calculate_price(start_datetime, expected_return_datetime, bike):
        price_hour = bike.hourly_price
        price_day = bike.daily_price
        duration = expected_return_datetime - start_datetime
        days = duration.days
        sec_left = duration.seconds
        hours = sec_left // 3600
        seconds = sec_left % 3600
        return (days*price_day + hours*price_hour + (price_hour if seconds else 0))

    @staticmethod
    def calculate_fee(rental, actual_return_datetime):
        LATE_FEE_LESS_HOUR = 20.0
        LATE_FEE_LESS_THREE_HOUR = 50.0
        LATE_FEE_MORE_THREE_HOUR = 100.0
        sec_duration = (actual_return_datetime - rental.expected_return_datetime).total_seconds()
        if sec_duration <= 0:
            return 0.0
        elif sec_duration <= 3600:
            return LATE_FEE_LESS_HOUR
        elif sec_duration <= 3600*3:
            return LATE_FEE_LESS_THREE_HOUR
        else:
            return LATE_FEE_MORE_THREE_HOUR