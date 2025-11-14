import uuid
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

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
    store_type: str
    operating_hours: dict[DayOfWeek, Optional[List[str]]]

class Coupon(BaseModel):
    store_id: uuid.UUID
    name: str

class Menu(BaseModel):
    name: str
    price: int

class MenuRequest(BaseModel):
    store_id: uuid.UUID
    menus: List[Menu]