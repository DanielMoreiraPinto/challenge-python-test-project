from distutils.log import ERROR
from src.enums import ClientType as cli, DayType as day


class Hotel():
    
    def __init__(
            self, name, rating, 
            weekday_price_regular, 
            weekend_price_regular,
            weekday_price_reward,
            weekend_price_reward):
        self.name = name
        self.rating = rating
        self.prices = {
            day.WEEKDAY.value: {
                cli.REGULAR.value: weekday_price_regular,
                cli.REWARD.value: weekday_price_reward},
            day.WEEKEND.value: {
                cli.REGULAR.value: weekend_price_regular,
                cli.REWARD.value: weekend_price_reward}}
        
    def get_reservation_price(self, weekdays, weekend_days, client_type):
        price = (weekdays * self.prices[day.WEEKDAY.value][client_type]
                + (weekend_days * self.prices[day.WEEKEND.value][client_type]))
        return price

            
    
    
        
        
        