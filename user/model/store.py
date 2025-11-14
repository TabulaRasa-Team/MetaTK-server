from typing import List

from pydantic import BaseModel

from owner.model.owner import DayOfWeek, Menu

class MenuResponse(Menu):
    image_url: str

class StoreDetailedResponse(BaseModel):
    store_name: str
    address: str
    phone_number: str
    operating_hours: dict[DayOfWeek, List[str]]
    menus: List[MenuResponse]
    images: List[str]
    ratio: dict[str, float]