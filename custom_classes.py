import time as time


class Register:
    def __init__(self, topic, event_date, time_spent, brief_description):
        self.topic = topic
        self.event_date = event_date
        self.time_spent = time_spent
        self.brief_description = brief_description
        self.daily_percentage = str(calculate_daily_percentage(time_spent))+'%'


def calculate_daily_percentage(hours):
    return hours/8 * 100

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Configs:
    db = 'register.db'
    test_db = 't.db'
    user_name = 'Isaque'
    mini_logo = """

                           _    _                  
                          | |  (_)                 
 _ __ ___   _   _  ______ | |_  _  _ __ ___    ___ 
| '_ ` _ \ | | | ||______|| __|| || '_ ` _ \  / _ \\
| | | | | || |_| |        | |_ | || | | | | ||  __/
|_| |_| |_| \__, |         \__||_||_| |_| |_| \___|
             __/ |                                 
            |___/                                  
"""
