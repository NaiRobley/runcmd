#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This tool will help you manage you calendars like never before.

Usage:
    calendar create_calendar <calendar_name>
    calendar add_event <calendar_name> <event_name>
    calendar see_events <calendar_name>
    calendar see_calendars
    calendar view_last_event <calendar_name>
    calendar (-i | --interactive)
    calendar (-h | --help)
    calendar quit

Options:
    -i, --interactive                           :  runs the script in interactive mode
    -h, --help                                  :  prints this help message
    create_calendar <calendar_name>             :  creates a calendar with a given name
    add_event <calendar_name> <event_name>      :  adds an event to a specific calendar
    see_events <calendar_name>                  :  prints all the events in a specific calendar
    see_calendars                               :  prints all the calendars in the system
    view_last_event <calendar_name>             :  prints the last event in a specific calendar
    quit                                        :  exit interactive mode
"""

import sys
import os
import cmd
from docopt import docopt, DocoptExit
from calendar import Calendar

new_calendar = Calendar()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class OurCalendar(cmd.Cmd):
    prompt = 'Calendar >>> '
    file = None
    print(__doc__)

    @docopt_cmd
    def do_create_calendar(self, args):
        """Usage: create_calendar <calendar_name>"""
        calendar_name = args["<calendar_name>"]
        new_calendar.create_calendar(calendar_name)

    @docopt_cmd
    def do_add_event(self, args):
        """Usage: add_event <calendar_name> <event_name>"""
        calendar_name = args["<calendar_name>"]
        event_name = args["<event_name>"]
        new_calendar.add_event(calendar_name, event_name)
        # print("You have added the event {0} to the calendar {1}".format(event_name, calendar_name))

    @docopt_cmd
    def do_see_calendars(self, args):
        """Usage: see_calendars"""
        if new_calendar.calendars.keys():
            print("\tThis are the calendars available in the system:")
            for cal in new_calendar.calendars.keys():
                print("\t\t{}".format(cal))
        else:
            print("\n\tThere are no calendars in the system yet\n\tPlease add one and try again\n")

    @docopt_cmd
    def do_see_events(self, args):
        """Usage: see_events <calendar_name>"""
        calendar_name = args["<calendar_name>"]
        new_calendar.see_events(calendar_name)

    @docopt_cmd
    def do_view_last_event(self, args):
        """Usage: view_last_event <calendar_name>"""
        calendar_name = args["<calendar_name>"]
        new_calendar.view_last_event(calendar_name)

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    OurCalendar().cmdloop()

print(opt)
