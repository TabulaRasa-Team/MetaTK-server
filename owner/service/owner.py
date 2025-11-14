import re
import uuid
from datetime import date

from core.error import DuplicateResourceException, InvalidValueException, IdNotFoundException
from owner.model.owner import Store, DayOfWeek, Coupon
from owner.repository import owner as repository
from owner.repository.owner import check_store_id

BLN_PATTERN = re.compile(r"^\d{3}-\d{2}-\d{5}$")

def create_store(request: Store) -> dict:

    if not BLN_PATTERN.fullmatch(request.bln):
        raise InvalidValueException(msg="BLN 형식이 잘못되었거나 유효하지 않습니다.")

    if repository.check_duplicate_bln(request.bln) is not None:
        raise DuplicateResourceException(msg="해당 BLN 으로 가게를 등록한 이력이 이미 존재합니다.")

    else:
        store_id = str(uuid.uuid4())
        store_type_value = request.category.value
        repository.create_store(store_id, store_type_value, request)

        for day in DayOfWeek:
            repository.create_operating_hour(store_id, day.value, request.operating_hours[day][0], request.operating_hours[day][1])

        return {
            "store_id" : store_id
        }

def create_coupon(request: Coupon) -> dict:

    if check_store_id(str(request.store_id)) is not []:
        raise IdNotFoundException(msg="해당 store_id의 가게를 찾을 수 없습니다.")

    repository.create_coupon(str(uuid.uuid4()), request, str(date.today()))

    return {
        "result" : "success"
    }