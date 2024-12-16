from cal_ui import *
from cal_abstraction import *
from lab8b import *
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT

if CHECK_AGAINST_FACIT:
    try:
        from lab8a import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *



def add_free_spans(appointments, start: Time, end: Time):
    '''Adds free spans to a list.'''
    if not appointments:
        # Inga fler appointments, lägg till den sista lediga perioden om den finns.
        if time_precedes(start, end):
            return [new_time_span(start, end)]
        return []

    appointment_start = ts_start(app_span(appointments[0]))
    appointment_end = ts_end(app_span(appointments[0]))

    if time_precedes_or_equals(start, appointment_start):
        # Om det finns utrymme mellan `start` och `appointment_start`, lägg till det.
        free_span = []
        if not time_equals(start, appointment_start):
            free_span = [new_time_span(start, appointment_start)]

        # Fortsätt från `appointment_end` för resten av listan.
        return free_span + add_free_spans(appointments[1:], appointment_end, end)

    elif time_precedes(appointment_start, start):
        # Om den nuvarande appointmenten överlappar med `start`, förskjut `start`.
        if not time_precedes(appointment_end, start):
            start = appointment_end

        # Fortsätt med nästa appointment från det nya `start`.
        return add_free_spans(appointments[1:], start, end)



def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    '''Returns the free spans of a day.'''
    if not is_booked_during(cal_day, new_time_span(start, end)):
        return new_time_span_seq([new_time_span(start, end)])
    
    return new_time_span_seq(add_free_spans(cal_day.appointments, start, end))

def show_free(name, day, month, start, end):
    '''Shows the free spans of a day in a calendar.'''
    if not calendar_exists(name):
        print("Not in calendar")
        return None
    else:
        day = new_day(day)
        month = new_month(month)
        start = new_time_from_string(start)
        end = new_time_from_string(end)
        cal_year = get_calendar(name)
        cal_month = cy_get_month(month, cal_year)
        cal_day = cm_get_day(cal_month, day)

        if time_precedes_or_equals(end, start):
            return new_time_span_seq()
        else:
            show_time_spans(free_spans(cal_day, start, end))


if __name__ == '__main__':
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    show_free("Jayne", 20, "sep", "08:00", "19:00")
    #Currently doesn't print anything since it has not been written yet
    