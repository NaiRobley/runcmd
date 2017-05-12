class Calendar(object):
    def __init__(self):
        self.calendars = {}

    def create_calendar(self,calendar_name):
        """Ledduh"""
        self.calendars[calendar_name] = []
        print('')
        print("\tNew calendar {} has been created".format(calendar_name))
        print('')
        return self.calendars

    def add_event(self, calendar_name, event_name):
        """Ledduh"""
        self.calendars[calendar_name].append(event_name)
        print('')
        print("\tNew event {0} has been added to the calendar {1}".format(event_name, calendar_name))
        print('')

    def see_events(self, cal_name):
        """Naomi"""
        #gets the calendar name
        #gets the events as per that calendar
        #prints out the events for the calendar
        print('')
        try:
            events=self.calendars[cal_name]
            if len(events) > 0:
                print("\tThe events in {}:".format(cal_name))
                for event in events:
                    print("\t\t{}".format(event))
            else:
                print("\tThere are currently no events in calendar {}".format(cal_name))
        except KeyError:
            print("\tSorry, the calendar name does not exist")
        print('')

#################################################################################################################################
############# CALENDAR TEAM PROJECT: IDD-HANDLING VIEW LAST EVENT IN THE CALENDAR ###############################################
#################################################################################################################################
    def view_last_event(self, cal_name):
        """get calendar and find events in the calendar, return last event"""
        # calendar_name=self.calendar_name
        event_list=0
        last_event=""
        if cal_name not in self.calendars:
        	print("\n\tThis calendar does not exist\n")
        else:
        	event_list=self.calendars.get(cal_name)
        	last_event=event_list[-1]
        	print ("\n\tThe last event in {0} is: {1}\n".format(cal_name, last_event))
        	return last_event
