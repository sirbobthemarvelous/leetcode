class MyCalendar:

    def __init__(self):
        self.calendar = {}
        #create an empty calendar dictionary of fillable dates
        
    def book(self, start: int, end: int) -> bool:
        #check if any dates are booked
        for date in range(start,end):
            if self.calendar.get(date) == 1:
            #to get a value form a dictionary use .get()
                return False
            
        #ok this isn't quick enough, lets use max min values
        
        #book those dates before returning true
        for date in range(start,end):
            self.calendar[date] = 1
        return True
