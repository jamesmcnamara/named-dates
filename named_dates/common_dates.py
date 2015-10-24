"""
TODO: This is more for trying out the API at the moment.
I want to see how clean all this actually is to use, separate
from the unit tests.

Eventually this should be cleaned up when I feel the API is
clean enough.
"""
import datetime
from dateutil.easter import easter

from named_dates import register_named_date, make_named_date_set

# TODO: How to key these dates?
#  Allow everything before "Day", unless two matches?
#  Allow partial matching?
#  Seems error prone
#  For base dates, set a few different keys, and any user defined
#  keys are up to themselves to add aliases?
#  Add alias option to provide acronym (e.g. MLK)?
#    Do simple test to ensure dict entries point to same instance
#    of is_date function.
#  This made up my mind - should definitely error on bad names.
#    The question is whether to wrap the KeyError or not.
#  Allow entering days by name (e.g. "Monday")?
register_named_date("New Years Day", 1, 1)
register_named_date("Martin Luther King Day", 1, 0, nth=3)
register_named_date("Washington's Birthday", 2, 0, nth=3)
register_named_date("President's Day", 2, 0, nth=3)


def is_good_friday(date):
    # Defaults to western Easter.
    return date == easter(date.year) - datetime.timedelta(days=2)

register_named_date("Good Friday", custom_func=is_good_friday)
register_named_date("Memorial Day", 5, 0, nth=1, from_end=True)
register_named_date("Independence Day", 7, 4)
register_named_date("Labor Day", 9, 0, nth=1)
register_named_date("Thanksgiving Day", 11, 3, nth=4)
register_named_date("Christmas Day", 12, 25)

# TODO: Half days for Thanksgiving and Christmas?

