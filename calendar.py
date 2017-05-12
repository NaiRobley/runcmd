class Calendar(object):
    def __init__(self):
        self.calendars = {
                            'first_calendar': ['first_event', 'second_event'],
                            'second_calendar':['first_event','second_event']
                            }

    def create_calendar(self,calendar_name):
        """Ledduh"""
        self.calendars[calendar_name] = []
        print("New calendar has been created") 
        return self.calendars 



    def add_event(self, calendar_name, event_name):
        """Ledduh"""
        self.calendars[calendar_name].append(event_name)
        print("New event has been added")

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

