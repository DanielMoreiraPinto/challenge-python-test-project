

class hotel():
    
    def __init__(
            self, name, rating, 
            weekday_price_regular, 
            weekend_price_regular,
            weekday_price_reward,
            weekend_price_reward):
        self.name = name
        self.rating = rating
        self.prices = {
            'weekday': {
                'regular': weekday_price_regular,
                'reward': weekday_price_reward},
            'weekend': {
                'regular': weekend_price_regular,
                'reward': weekend_price_reward}}
        
    
    
        
        
        