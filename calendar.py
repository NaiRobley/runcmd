class Calendar(object):
    def __init__(self):
        self.calendars = {
                            'first_calendar': ['first_event', 'second_event'],
                            'second_calendar':['first_event','second_event']
                            }

    def create_calendar(self):
        """Ledduh"""
        pass

    def add_event(self):
        """Ledduh"""
        pass

    def see_events(self, cal_name):
        """Naomi"""
        #gets the calendar name
        #gets the events as per that calendar
        #prints out the events for the calendar
        try:
            events=self.calendars[cal_name]
            print("The events are:")
            for event in events:
                print("{}".format(event))
        except KeyError:
            print("Sorry, the calendar name does not exist")
    def view_last_event(self):
        """Idd"""
        pass

new_cal=Calendar()
new_cal.see_events("third calendar")
