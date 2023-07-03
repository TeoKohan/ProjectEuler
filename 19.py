from __future__ import annotations
from enum import Enum

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def next(self, n) -> None:
        v = (self.value + n) % 7
        return Weekday(v)

class Month(Enum):
    JANUARY = 0
    FEBRUARY = 1
    MARCH = 2
    APRIL = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUGUST = 7
    SEPTEMBER = 8
    OCTOBER = 9
    NOVEMBER = 10
    DECEMBER = 11

    def next(self) -> None:
        v = (self.value + 1) % 12
        return Month(v)

def is_leap_year(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(month: Month, year: int):
    match month:
        case Month.JANUARY: 
            return 31
        case Month.FEBRUARY: 
            return 28 + (1 if is_leap_year(year) else 0)
        case Month.MARCH: 
            return 31
        case Month.APRIL: 
            return 30
        case Month.MAY: 
            return 31
        case Month.JUNE: 
            return 30
        case Month.JULY: 
            return 31
        case Month.AUGUST: 
            return 31
        case Month.SEPTEMBER: 
            return 30
        case Month.OCTOBER: 
            return 31
        case Month.NOVEMBER: 
            return 30
        case Month.DECEMBER: 
            return 31

class Date:
    def __init__(self, weekday: Weekday, month: Month, year: int) -> Date:
        self.weekday = weekday
        self.month = month
        self.year = year
    
    def next_month(self):
        self.weekday = self.weekday.next(days_in_month(self.month, self.year))
        if self.month == Month.DECEMBER:
            self.year += 1
        self.month = self.month.next()
    
    def __repr__(self) -> str:
        return f'({self.weekday}/{self.month}/{self.year})'

date = Date(Weekday.MONDAY, Month.JANUARY, 1900)

first_sundays = 0
while date.year < 2001:
    if date.year >= 1901 and date.weekday == Weekday.SUNDAY:
        first_sundays += 1
    date.next_month()
print(first_sundays)