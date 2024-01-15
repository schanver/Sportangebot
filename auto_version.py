from bot import book_a_reservation
import datetime

tage = ["montag","dienstag","mittwoch","donnerstag","freitag","samstag","sonntag"]

def anmelden():
    today = datetime.datetime.today().weekday()
    return tage[today]

day = anmelden()
book_a_reservation(day)
