#!/usr/bin/env python3
# Student ID: skarki28

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(time):
    '''Format a Time object as a string in hh:mm:ss format.'''
    return f'{time.hour:02}:{time.minute:02}:{time.second:02}'

def time_to_sec(time):
    '''Convert a Time object to a single integer representing the number of seconds from midnight.'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''Convert a given number of seconds to a Time object in hour, minute, second format.'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    '''Add two Time objects and return the sum as a new Time object.'''
    t1_sec = time_to_sec(t1)
    t2_sec = time_to_sec(t2)
    total_sec = t1_sec + t2_sec
    return sec_to_time(total_sec)

def change_time(time, seconds):
    '''Modify a Time object by adding the number of seconds.'''
    current_sec = time_to_sec(time)
    new_sec = current_sec + seconds
    # Ensure seconds is within the range of a day
    new_sec %= 86400
    new_time = sec_to_time(new_sec)
    # Update the original Time object
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None
