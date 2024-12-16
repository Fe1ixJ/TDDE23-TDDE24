from cal_abstraction import *
from cal_output import show_ts
# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("Time_spans", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(Time_spans: List[TimeSpan] = None) -> TimeSpanSeq:
    """
    Skapar och returnerar en ny TimeSpanSeq med den angivna listan av TimeSpans, 
    som är sorterade i kronologisk ordning.
    """
    if Time_spans is None:
        Time_spans = []
    else:
        ensure_type(Time_spans, List[TimeSpan])
    return TimeSpanSeq(Time_spans)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """kollar om angiven TimeSpanSeq är tom"""
    ensure_type(tss, TimeSpanSeq)
    return not tss.Time_spans


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Funktion som kallas av användare för att lägga till en ny TimeSpan i TimeSpanSeq,
    som sedan returnerar en ny TimeSpanSeq med den nyligen tillagda TimeSpan:en
    """
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    def add_span(ts: TimeSpan, ts_list: List[TimeSpan]):
        """
        Returnerar en kopia av given TimeSpanSeq, där en ny TimeSpan har lagts till
        på rätt position.
        """
        if not ts_list or time_precedes(ts_start(ts), ts_start(ts_list[0])):
            return [ts] + ts_list
        else:
            return [ts_list[0]] + add_span(ts, ts_list[1:])
    
    return new_time_span_seq(add_span(ts, tss.Time_spans))


def tss_iter_spans(tss: TimeSpanSeq):
    """används för att få ut varje TimeSpan i TimeSpanSeq"""
    ensure_type(tss, TimeSpanSeq)
    for ts in tss.Time_spans:
        yield ts
            

def show_time_spans(tss):
    """printar varje TimeSpan i TimeSpanSeq"""
    for ts in tss_iter_spans(tss):
        show_ts(ts)
        print("")


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result

if __name__ == "__main__":
    time1 = new_time(new_hour(10), new_minute(15))
    time2 = new_time(new_hour(13), new_minute(30))
    time3 = new_time(new_hour(9), new_minute(30))
    time4 = new_time(new_hour(12), new_minute(30))

    new_span1 = new_time_span(time1, time2)
    new_span2 = new_time_span(time3, time4)

    new_seq = new_time_span_seq()
    new_seq = tss_plus_span(new_seq, new_span1)
    new_seq = tss_plus_span(new_seq, new_span2) 
    
    show_time_spans(new_seq)
    