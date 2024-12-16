from cal_ui import *
from cal_abstraction import *

def remove(name, day, month, start):
    '''Removes an appointment from the specified calendar.'''
    if not calendar_exists(name):
        print("Not in calendar")
        return None
    else:
        day = new_day(day)
        month = new_month(month)
        start = new_time_from_string(start)
        cal_year = get_calendar(name)
        cal_month = cy_get_month(month, cal_year)
        cal_day = cm_get_day(cal_month, day)
        
        if is_booked_from(cal_day, start):
            new_year = minus_appointment(find_appointment(cal_day, start), cal_year, cal_month, cal_day)
            insert_calendar(name, new_year)

            print("Appointment removed")
        else:
            print("No appointment at that time")

def minus_appointment(appointment, cal_year, cal_month, cal_day):
    '''Removes an appointment and updates the calendar.'''
    old_cal_day = cal_day
    old_cal_month = cal_month

    new_cal_day = cd_minus_appointment(old_cal_day, appointment)
    new_cal_month = cm_plus_cd(old_cal_month, new_cal_day)
    new_cal_year = cy_plus_cm(cal_year, new_cal_month)

    return new_cal_year

def cd_minus_appointment(cal_day, appointment):
    '''Removes an appointment from a calendar day'''
    #
    def remove_appointment(app, appointments):
        '''Removes an appointment from the list.'''
        new_appointments = appointments.copy()
        new_appointments.remove(app)
        return new_appointments

    return new_calendar_day(cd_day(cal_day), remove_appointment(appointment, cal_day.appointments))  


def find_appointment(cal_day, start):
    '''Finds and returns an appointment in a calendar day.'''
    for appointment in cd_iter_appointments(cal_day):
        if time_equals(start, ts_start(app_span(appointment))):
            return appointment



if __name__ == "__main__":
    create("Test")
    book("Test", 20, "sep", "12:00", "13:00", "Rob train")
    book("Test", 20, "sep", "14:00", "14:01", "Rob train2")
    show("Test", 20, "sep")
    print("=========================")
    
    remove("Test", 20, "sep", "13:00")
    remove("Test", 20, "sep", "12:00")
    show("Test", 20, "sep")