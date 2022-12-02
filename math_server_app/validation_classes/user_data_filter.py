from abc import ABC, abstractmethod

from pydantic import ValidationError

from validation_classes.user_validator import UserDataValidator


class UserDataFilter(ABC):
    """Class implements methods to validate received data """
    def __init__(self, validator_class=UserDataValidator):
        self._validator_class = validator_class


    def __call__(self, data: list, *args, **kwargs):
        validated_data = self._validate_data(data)
        if not validated_data:
            return {'Message': 'No records.'}
        return self._count_result(validated_data, *args)

    @abstractmethod
    def _count_result(self, data, *args):
        raise NotImplementedError("Must implement in child class")

    def _validate_data(self, data):
        validated_data = []
        for rec in data:
            try:
                temp = self._validator_class.parse_obj(rec)
            except ValidationError:
                pass
            else:
                validated_data.append(dict(temp))

        return validated_data
