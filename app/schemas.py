from datetime import datetime
from typing import List
from pydantic import BaseModel, validator


class city(BaseModel):
    name: str

class cat(BaseModel):
    favorite_fish: str

class dog(BaseModel):
    bark_decibels: float

    @validator("bark_decibels")
    def check_double(cls, v):
        if not isinstance(v, float):
            raise ValueError("bark_decibels must be a double")
        return v
    
class city_cat(BaseModel):
    pass