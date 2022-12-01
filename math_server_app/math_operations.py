from pydantic import BaseModel, validator, ValidationError
from typing import Optional
import pandas as pd
from abc import ABC, abstractmethod
from collections import Counter


class UserDataValidator(BaseModel):
    name: str
    age: int
    time_created: int
    gender: Optional[str]
    last_name: Optional[str]
    ip: Optional[str]
    city: Optional[str]
    premium: Optional[bool]
    birth_day: Optional[str]
    balance: Optional[float]

    @validator('name')
    def user_name_validator(cls, obj):
        if not obj:
            raise ValidationError
        return obj

    @validator('age')
    def age_validator(cls, obj):
        if obj <= 0:
            raise ValidationError
        return obj


class UserDataFilter(ABC):
    """Class implements methods to validate recieved data """
    def __init__(self, data: list, validator_class=UserDataValidator):
        self._validator_class = validator_class
        self._data = data

    def __call__(self, *args, **kwargs):
        validated_data = self._validate_data()
        if not validated_data:
            return {'Message': 'No records.'}
        return self._count_result(validated_data, *args)

    @abstractmethod
    def _count_result(self, data, *args):
        return

    def _validate_data(self):
        validated_data = []
        for rec in self._data:
            try:
                temp = self._validator_class.parse_obj(rec)
            except ValidationError as e:
                pass
            else:
                validated_data.append(dict(temp))

        return validated_data


class MedianCalculator(UserDataFilter):
    """Class for counting median by 'age' field of data"""
    def _count_result(self, data, *args):
        df = pd.DataFrame(data)
        return df['age'].median()


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


class UniqueNamesCalculator(UserDataFilter):
    """Class for counting unuque names of users"""
    def _count_result(self, data, *args):
        df = pd.DataFrame(data)
        return Counter(df['name'])