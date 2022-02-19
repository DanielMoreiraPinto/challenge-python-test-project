from enum import Enum


class ClientType(Enum):
    REGULAR = 'Regular'
    REWARD = 'Rewards'
    
class DayType(Enum):
    WEEKDAY = 'Weekday'
    WEEKEND = 'Weekend'