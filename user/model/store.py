from typing import List, Optional

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

class StoreListItem(BaseModel):
    store_id: str
    store_name: str
    address: str
    store_type: str
    ratio: dict[str, float]

class StoreInfoResponse(BaseModel):
    store_name: str
    operating_hours: dict[DayOfWeek, Optional[List[str]]]
    ratio: dict[str, float]