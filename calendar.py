class Calendar(object):
    def __init__(self):
        self.calendars = {
                            'first_calendar': ['first_event']
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

    def see_events(self):
        """Naomi"""
        pass

    def view_last_event(self):
        """Idd"""
        pass
        