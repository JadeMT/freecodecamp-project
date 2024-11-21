# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:18:43 2024

@author: jlove
"""

def add_time(start,duration,day_of_week=None):
    new_time=''
    # time input
    start_time,AM_PM = map(str,start.split())
    start_hours,start_min = map(int,start_time.split(':'))
    add_hours,add_min = map(int,duration.split(':'))
    dow = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    mins = start_min + add_min
    hours = start_hours + add_hours
    
    # minutes carry into hours
    if mins>=60:
        hours+=1
        mins-=60
    
    # calculate how many days and remains of hours
    days = hours // 24
    new_hours = hours % 24
    
    #check PM or AM
    if new_hours >12 and AM_PM =='PM':
        AM_PM = 'AM'
        new_hours = new_hours-12
        days+=1
    elif new_hours >12 and AM_PM =='AM':
        AM_PM = 'PM'
        new_hours = new_hours-12
    elif new_hours ==12 and AM_PM =='AM':
        AM_PM ='PM'
    elif new_hours ==12 and AM_PM =='PM':
        AM_PM ='AM'
        days+=1
    
    #check if any day of week input and return answer
    if day_of_week!=None:
        index = dow.index(day_of_week.capitalize())
        index = (index+days)%7
        
        if days ==1:    
            new_time = f'{new_hours}:{mins:>02} {AM_PM}, {dow[index]} (next day)'
        elif days>1:
            new_time = f'{new_hours}:{mins:>02} {AM_PM}, {dow[index]} ({days} days later)'
        else:
            new_time = f'{new_hours}:{mins:>02} {AM_PM}, {dow[index]}'
    else:
        if days ==1:    
            new_time = f'{new_hours}:{mins:>02} {AM_PM} (next day)'
        elif days>1:
            new_time = f'{new_hours}:{mins:>02} {AM_PM} ({days} days later)'
        else:
            new_time = f'{new_hours}:{mins:>02} {AM_PM}'

    print(new_time)
    return new_time
    
    
    
    
#The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('11:55 AM', '0:05')
add_time('2:59 AM', '24:00')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('3:30 PM', '2:12', 'Monday')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday') 