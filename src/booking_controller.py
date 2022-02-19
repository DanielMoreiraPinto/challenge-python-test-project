from os import getcwd, listdir, path
from re import sub
from datetime import datetime

from src.hotel import Hotel


class BookingController():
    
    def __init__(self):
        self.__hotels = []
        self.__data_dir = './data'
        
    def assist_booking(self):
        self.__get_hotels()
        input_str = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'
        client_type, dates = self.__process_input(input_str)
        
        qtd_weekdays = qtd_weekends = 0
        for date in dates:
            if date.weekday() < 4:
                qtd_weekdays += 1
            else:
                qtd_weekends += 1
        
        cheapest_hotel = None
        cheapest_price = 0
        for hotel in self.__hotels:
            cur_price = hotel.get_reservation_price(qtd_weekdays, 
                                                    qtd_weekends, 
                                                    client_type)
            if (cheapest_hotel == None or 
                cur_price < cheapest_price
                or (cur_price == cheapest_price and
                    hotel.rating < cheapest_hotel.rating)):
                cheapest_hotel = hotel
                cheapest_price = cur_price
                
        print(cheapest_hotel.name)
                
        
    def __process_input(self, input_str):
        client_type, dates_unformatted = input_str.replace(' ', '').split(':')
        dates_unformatted = sub(r"\([^()]*\)", "", dates_unformatted)
        dates = []
        for date_unformatted in dates_unformatted.split(','):
            date = datetime.strptime(date_unformatted, '%d%b%Y')
            dates.append(date)
        return (client_type, dates)
    
    def __get_hotels(self):
        lakewood = Hotel('Lakewood', 3, 110, 90, 80, 80)
        bridgewood = Hotel('Bridgewood', 4, 160, 60, 110, 50)
        ridgewood = Hotel('Ridgewood', 5, 220, 150, 100, 40)
        hotels = [lakewood, bridgewood, ridgewood]
        self.__hotels = hotels
        
         