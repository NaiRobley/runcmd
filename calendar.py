class Calendar(object):
    def __init__(self):
        self.calendars = {
                            'first_calendar': ['first_event', 'second_event', 'third_event'], 'calendar2': ['event1', 'event2', 'event3']
                            }

    def create_calendar(self):
        """Ledduh"""
        pass

    def add_event(self):
        """Ledduh"""
        pass

    def see_events(self):
        """Naomi"""
        pass
#################################################################################################################################
############# CALENDAR TEAM PROJECT: IDD-HANDLING VIEW LAST EVENT IN THE CALENDAR ###############################################
#################################################################################################################################
    def view_last_event(self, cal_name):
        """get calendar and find events in the calendar, return last event"""
        # calendar_name=self.calendar_name
        event_list=0
        last_event=""
        if cal_name not in self.calendars:
        	print("This calendar does not exisit")
        else:
        	event_list=self.calendars.get(cal_name)
        	last_event=event_list[-1]
        	print (last_event)
        	return last_event

newCal = Calendar()
newCal.view_last_event('first_calendar')
newCal.view_last_event('calendar2')
newCal.view_last_event('another')
