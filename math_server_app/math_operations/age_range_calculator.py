from validation_classes.user_data_filter import UserDataFilter


class AgeRangeCalculator(UserDataFilter):
    """Class for filtering user by age range"""

    def _count_result(self, data, *args):
        age_from, age_to = args

        if age_from <= 0 or age_to <= 0:
            return {"Mistake": "Age must be above zero"}
        if age_from > age_to:
            return {"Mistake": "age_from must be less or equal age_to"}

        result = []
        for rec in data:
            if age_from <= rec['age'] <= age_to:
                result.append(rec)
        return result

