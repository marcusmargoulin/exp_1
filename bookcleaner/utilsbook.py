from __future__ import print_function
from __future__ import division

import pandas as pd

def get_date(date):
    return pd.to_datetime(date).date()