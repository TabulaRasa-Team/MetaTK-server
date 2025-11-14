import re
import uuid
from datetime import date, timedelta

from core.error import DuplicateResourceException, InvalidValueException, IdNotFoundException
from owner.model.owner import Store, DayOfWeek, Coupon, MenuRequest
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
        store_type_value = request.store_type
        repository.create_store(store_id, store_type_value, request)

        for day in DayOfWeek:
            if request.operating_hours[day] is None:
                repository.create_operating_hour_for_holiday(store_id, day.value)
                continue
            repository.create_operating_hour(store_id, day.value, request.operating_hours[day][0], request.operating_hours[day][1])

        # 메뉴 저장
        for menu in request.menus:
            repository.insert_menu(store_id, menu.name, menu.price, menu.image)

        # 이미지 저장
        for image in request.images:
            repository.insert_picture(store_id, image)

        return {
            "store_id" : store_id
        }

def create_coupon(request: Coupon) -> dict:

    if check_store_id(str(request.store_id)) is []:
        raise IdNotFoundException(msg="해당 store_id의 가게를 찾을 수 없습니다.")

    # 쿠폰 생성 (status: available, validity_period: 30일)
    coupon_id = str(uuid.uuid4())
    status = "available"
    validity_period = 30
    repository.create_coupon(coupon_id, request, status, validity_period)

    # country가 'sinla'인 사용자들 조회
    shinla_users = repository.get_users_by_country('shinla')

    # 각 사용자에게 쿠폰 발급 (만료일: 오늘로부터 한 달 후)
    expiration_date = date.today() + timedelta(days=30)
    for user in shinla_users:
        repository.insert_coupon_history(
            user_id=user['id'],
            coupon_id=coupon_id,
            expiration=str(expiration_date),
            status='notUsed'
        )

    return {
        "result" : "success"
    }