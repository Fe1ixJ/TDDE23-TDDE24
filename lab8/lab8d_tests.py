# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    store_test_case(
        test_cases,
        2,
        start_str="10:00", 
        end_str="22:00", 
        booking_data=[],
        exp_result=["10:00-22:00"],
    ) # Testar funktionaliteten för då det inte finns någon bokning under angiven tid, expectar då hela tidsspannet (från start till end)
    store_test_case(
        test_cases,
        3,
        start_str="10:00",
        end_str="18:00",
        booking_data=["10:00-18:00"],
        exp_result=[],
    ) # Testar funktionaliteten för då det finns en bokning under hela angiven tid, expectar då att det inte finns några
    store_test_case(
        test_cases,
        4,
        start_str="10:00",
        end_str="18:00",
        booking_data=["10:00-10:24", "10:32-11:21", "12:04-17:32"],
        exp_result=["10:24-10:32", "11:21-12:04", "17:32-18:00"],
    ) # Testar funktionaliteten för minut precision, expectar då att det finns luckor mellan bokningarna
    store_test_case(
        test_cases,
        5,
        start_str="10:00",
        end_str="18:00",
        booking_data=["10:00-11:00", "10:30-15:00"],
        exp_result=["15:00-18:00"],
    ) # Testar Overlapping bokningar
    store_test_case(
        test_cases,
        6,
        start_str="10:00",
        end_str="18:00",
        booking_data=["09:00-15:00", "16:00-19:00"],
        exp_result=["15:00-16:00"],
    ) # Testing booking before and after search interval
    store_test_case(
        test_cases,
        7,
        start_str="10:00",
        end_str="18:00",
        booking_data=["10:00-10:29", "10:30-14:59", "15:00-16:29", "16:30-18:00"],
        exp_result=["10:29-10:30", "14:59-15:00", "16:29-16:30"],
    ) # Testar funktionaliteten när det är korta intervaller


    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
