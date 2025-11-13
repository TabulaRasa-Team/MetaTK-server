from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel

class StoreType(Enum):
    FOOD = "food"
    CAFE = "cafe"
    DRINK = "drink"

class DayOfWeek(Enum):
    MON = "mon"
    TUE = "tue"
    WED = "wed"
    THU = "thu"
    FRI = "fri"
    SAT = "sat"
    SUN = "sun"

class Store(BaseModel):
    company_name: str
    bln: str
    owner_name: str
    address: str
    phone_number: str
    category: StoreType
    operating_hours: dict[DayOfWeek, List[str]]
