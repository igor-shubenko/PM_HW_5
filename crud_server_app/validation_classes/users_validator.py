from pydantic import BaseModel, validator
from typing import Optional


class UserDataValidator(BaseModel):
    name: str
    age: Optional[int]
    time_created: int
    gender: Optional[str]
    last_name: Optional[str]
    ip: Optional[str]
    city: Optional[str]
    premium: Optional[bool]
    birth_day: Optional[str]
    balance: Optional[float]

    @validator('time_created')
    def time_created_validator(cls, obj):
        if obj <= 0:
            raise ValueError("Time must be greater than zero")
        return obj

    @validator('age')
    def age_validator(cls, obj):
        if obj <= 0:
            raise ValueError("Age must be greater than zero")
        return obj


class UserUpdateDataValidator(UserDataValidator):
    name: Optional[str]
    time_created: Optional[int]
