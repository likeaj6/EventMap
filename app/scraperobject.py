"""
BunnB 2k17
Happy new year nerds HEHheHEheHhEhE

"""

import json
from sortedcollections import OrderedDict
from stringfixer import stringfix
from firebase import *

firebase = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)
result = firebase.get('/events',None)
curr_events = []   #Gets list of curr. events on firebase database
for id_key,event in result.items():
    for key,val in event.items():
        try:
            event[key] = val.encode("utf-8")
        except:
            pass
        event[key.encode("utf-8")] = event.pop(key)
    curr_events.append(event)

locDic = {"Clothier": (39.904258,-75.354876),
          "Bond Complex": (39.905395,-75.350844),
          "Black Cultural Center": (39.906952,-75.351481),
          "Kohlberg": (39.905830,-75.354873),
          "Lang Music Building": (39.905500,-75.356115),
          "Lang Performing Arts Center": (39.905377,-75.355310),
          "McCabe Library": (39.905361,-75.352797),
          "Friends Meeting House": (39.907342,-75.353221),
          "Parrish": (39.905188,-75.354202),
          "Matchbox": (39.901394,-75.355239),
          "Lamb-Miller Fieldhouse": (39.901279,-75.354112),
          "Trotter": (39.906415,-75.353912),
          "Science Center": (39.906859,-75.355855),
	  "No Location": (39.904321,-75.351434)
}

class SwatScraper():
    def __init__(self, string):
        """
        contains master string and current "reading" string
        contains keywords to identify Locations, Days, and Times
        """
        self.string = string
        self.curr = None
        self.locations = ['Clothier','Bond Complex','Black Cultural Center','Kohlberg','No Location','Lang Music Building','Lang Performing Arts Center','McCabe Library','Friends Meeting House','Parrish','Matchbox','Lamb-Miller Fieldhouse','Trotter','Science Center']
        self.days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',]
        self.times = ['AM','PM','All Day']
        self.events = curr_events

    def checkTime(self,line):
        for time in self.times:
            if time in line:
                return True
            else:
                pass
        return False

    def checkLoc(self,line):
        for loc in self.locations:
            if loc in line:
                return loc
            else:
                pass
        return None

    def checkDay(self,line):
        for day in self.days:
            if day in line:
                return True
            else:
                pass
        return False

    def findEvents(self):
        """
        grabs events
        """
        __id = 0
        while len(self.string) > 0:
            self.readline()
            loc = self.checkLoc(self.curr)
            if loc != None:
                location = loc
            elif self.checkDay(self.curr) == True:
                day = self.curr
            elif self.checkTime(self.curr) == True:
                if "Application Deadline" in self.curr:
                    pass
                else:
                    time_name = stringfix(self.curr)
                    if len(time_name) == 2:
                        event = {"name":time_name[1], "start_time":time_name[0], "end_time":" ", "location":location, "lat":locDic[location][0], "lng":locDic[location][1], "description":day}
                        if event in curr_events:
                            pass
                        else:
                            result = firebase.post("/events",event)
                    else:
                        event = {"name":time_name[2], "start_time":time_name[0], "end_time":time_name[1], "location":location, "lat":locDic[location][0], "lng":locDic[location][1], "description":day}
                        if event in curr_events:
                            pass
                        else:
                            result = firebase.post("/events",event)
                    __id += 1
            else:
                pass

    def readline(self):
        """
        reads a line from string
        upates current "read" string
        makes master string shorter
        """
        newstring = ''
        substring = ''
        for x in self.string:
            if x!= '\n':
                substring += x
            else:
                index = len(substring) + 1 ## +1 takes into account newline char
                newstring = self.string[index::]
                break
        self.string = newstring
        self.curr = substring


if __name__ == "__main__":
    string ="""Clothier - (Tarble-in-Clothier All-Campus Space)

Start Date and TimeEvent Details

Wednesday, December 07, 2016

4:30 PM - 5:30 PM Collection - a Celebration of Light

Kohlberg - (Kohlberg 228)

Start Date and TimeEvent Details

Tuesday, December 06, 2016

All Day Law as a Tool for Social Justice and Conflict Resolution"""
    myscraper = SwatScraper(string)
    myscraper.findEvents()
    print(myscraper.events)
