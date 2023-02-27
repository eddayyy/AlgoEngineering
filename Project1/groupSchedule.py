# *********************************************************************************************************************************
# Program name: "Group Scheduling Problem". This program receives the input of 4 arrays, and an integer and then performs         *
# checks to see where there are potential meeting times for a group.                                                              * 
#                                                                                                                                 *
# Copyright (C) 2023 Eduardo Nunez & Juan Gonzalez                                                                                *  
#                                                                                                                                 *
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License       *
# version 3 as published by the Free Software Foundation.                                                                         *
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied              *
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.          *
# A copy of the GNU General Public License v3 is available here:  <https://www.gnu.org/licenses/>.                                *
# *********************************************************************************************************************************
# ========1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3
# 
# Authors' information
#   Author 1 name:  Eduardo Nunez
#   Author 2 name:  Juan Gonzalez 
#   Author 1 email: eduardonunez@csu.fullerton.edu
#   Author 2 email: gonzalez.juanant524@csu.fullerton.edu
#
# Program information
#   Program name: Group Scheduling Problem
#   Programming languages: Function Module written in Python
#   Date program began: 2023-Feb-24 0800 PDT GMT-07:00
#   Date of last update: 2023-Feb-26 1800 PDT GMT-07:00
#   Date comments upgraded: 2023-Feb-26
#   Files in this program: groupSchedule.py
#   Status: Finished.
#   References consulted: Geeks For Geeks, Algorithm Design in Three Acts (ADITA) By Kevin A. Wortman (Chapter 3, 4, 6), Stack Overflow, 
#                         Python Documentation: https://docs.python.org/3/library/datetime.html
# 
# Purpose
#   This program is an algorithm created to provide the user with potential meeting times with their group members. It demonstrates data manipulation 
#   techniques using lambda functions, the datetime module, iteration, etc.
# 
# This file
#   File name: groupSchedule.py
#   Language:  Python
# ========1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**
# Compiling and Linking this program and file:
#
# Step 1. Install python 3 on your machine. A tutorial for any OS can be found here https://realpython.com/installing-python/ 
#         
# Step 2. Enter the following in your linux terminal
# 
# python3 groupSchedule.py
# 
# ===== Begin code area ========================================================================================================

from datetime import datetime, timedelta

def schedule_meeting(person1_schedule, person1_daily_availability, person2_schedule, person2_daily_availability, duration_of_meeting):
    # Convert the daily availability times to datetime objects
    person1_start, person1_end = map(lambda x: datetime.strptime(x, '%H:%M'), person1_daily_availability)
    person2_start, person2_end = map(lambda x: datetime.strptime(x, '%H:%M'), person2_daily_availability)
    
    # Combine the schedules and sort by start time
    schedule = sorted(person1_schedule + person2_schedule, key=lambda x: datetime.strptime(x[0], '%H:%M'))
    
    # Assign last_end with the earliest a meeting can start 
    last_end = min(person1_start, person2_start)

    # Create a list of unavailability periods
    unavailabilities = []
    
    for start, end in schedule:
        start_time = datetime.strptime(start, '%H:%M')
        end_time = datetime.strptime(end, '%H:%M')

        if start_time > last_end:
            unavailabilities.append([last_end, start_time])

        last_end = max(last_end, end_time)

    if last_end < max(person1_end, person2_end):
        unavailabilities.append([last_end, max(person1_end, person2_end)])

    # Find available timeslots with specified duration
    available_times = []
    for start, end in unavailabilities:
        interval_start = start
        interval_end = start + timedelta(minutes=duration_of_meeting)
        while interval_end <= end:
            if interval_start >= person1_start and interval_end <= person1_end and \
                interval_start >= person2_start and interval_end <= person2_end:
                available_times.append([interval_start.strftime('%H:%M'), interval_end.strftime('%H:%M')])
            
            interval_start += timedelta(minutes=30)
            interval_end += timedelta(minutes=30)

    # Merge overlapping intervals
    merged_times = []
    for start, end in sorted(available_times, key=lambda x: datetime.strptime(x[0], '%H:%M')):
        if merged_times and start <= merged_times[-1][1]:
            merged_times[-1][1] = max(merged_times[-1][1], end)
        else:
            merged_times.append([start, end])

    # Filter out intervals less than specified duration
    final_times = []
    for start, end in merged_times:
        delta = datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')
        if delta.seconds >= (duration_of_meeting * 60):
            final_times.append([start, end])

    # Sort output in ascending order
    formatted_times = [[datetime.strptime(start, '%H:%M').strftime('%H:%M'), datetime.strptime(end, '%H:%M').strftime('%H:%M')] for start, end in final_times]
    formatted_times.sort()

    # Return the list of available times for a meeting
    return formatted_times

person1_schedule =[['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_dailyact = ['9:00', '19:00']
person2_schedule = [['9:00', '10:30'], ['12:20', '14:30'], ['14:00', '15:00'], ['16:00', '17:00']]
person2_dailyact = ['9:00', '18:30']
duration_of_meeting = 30

available_times = schedule_meeting(person1_schedule, person1_dailyact, person2_schedule, person2_dailyact, duration_of_meeting)

print(available_times)
