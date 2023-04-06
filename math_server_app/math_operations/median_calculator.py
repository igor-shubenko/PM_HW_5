import pandas as pd

from validation_classes.user_data_filter import UserDataFilter


class MedianCalculator(UserDataFilter):
    """Class for counting median by 'age' field of data"""
    def _count_result(self, data, *args):
        df = pd.DataFrame(data)
        return df['age'].median()