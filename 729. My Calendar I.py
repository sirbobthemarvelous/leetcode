class MyCalendar:

    def __init__(self):
        self.calendar = {}
        #create an empty calendar dictionary of fillable dates
        
    def book(self, start: int, end: int) -> bool:
        #check if any dates are booked
        for index,(minimum,maximum) in enumerate(self.calendar.items()):
            if start<=minimum<end or start<maximum<=end:
            #to get a value form a dictionary use .get()
                return False
            
        #ok this isn't quick enough, lets use max min values
        
        #book those dates before returning true
        self.calendar[start] = end
        return True
"""
apparently you can do this all with a list rather than dictionary

class MyCalendar(object):

    def __init__(self):
        self.__calendar = []


    def book(self, start, end):
        
        for i, j in self.__calendar:
            if start < j and end > i:
                return False
        self.__calendar.append((start, end))
        return True
"""