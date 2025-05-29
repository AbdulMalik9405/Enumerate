from enum import Enum

class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thurday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

DayInput = int(input("Write a number from 1-7 for the day to be displayed"))

for i in Weekday:
    if DayInput == i.value:
        print(i.name)
    NextDay = i.value+1
    if DayInput+1 == NextDay:
        if NextDay == 8:
            NextDay = 1
        print(Weekday(NextDay).name)
    PrevDay = i.value-1
    if DayInput-1 == PrevDay:
        if PrevDay == 0:
            PrevDay = 7
        print(Weekday(PrevDay).name)