from collections import Counter

import pandas as pd

from validation_classes.user_data_filter import UserDataFilter


class UniqueNamesCalculator(UserDataFilter):
    """Class for counting unuque names of users"""
    def _count_result(self, data, *args):
        df = pd.DataFrame(data)
        return Counter(df['name'])