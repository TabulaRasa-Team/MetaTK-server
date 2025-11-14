from typing import List
from owner.model.owner import DayOfWeek
from user.model.store import StoreDetailedResponse, MenuResponse, StoreListItem, StoreInfoResponse
from user.repository import store as repository

def get_operating_hours(request):
    operating_hours = {day: [] for day in DayOfWeek}

    for operating_hour in request:
        day_enum = DayOfWeek(operating_hour['yoil'])
        operating_hours[day_enum].append(str(operating_hour['open_time']))
        operating_hours[day_enum].append(str(operating_hour['close_time']))

    return operating_hours

def get_ratio(request):
    ratio = {
        'shinla_ratio' : 0, 'goguryeo_ratio' : 0, 'baekjae_ratio' : 0
    }

    total = 0
    for data in request:
        count = int(data['count(*)'])
        country = data['country']
        total += count
        ratio[f"{country}_ratio"] = count

    if total == 0:
        return ratio

    ratio = {f"{country}_ratio": round(count / total * 100, 1) for country, count in ratio.items()}

    return ratio

def get_all_stores() -> List[StoreListItem]:
    stores = repository.get_all_stores()

    result = []
    for store in stores:
        ratio_data = repository.get_ratio(store['id'])
        ratio = get_ratio(ratio_data)

        result.append(StoreListItem(
            store_id=store['id'],
            store_name=store['name'],
            address=store['address'],
            store_type=store['store_type'],
            ratio=ratio
        ))

    return result

def get_store_info(store_id: str) -> StoreInfoResponse:
    store_information = repository.get_store_information(store_id)
    store_name = store_information['name']

    operating_hours_data = repository.get_operating_hours(store_id)
    operating_hours = get_operating_hours(operating_hours_data)

    # None으로 변환 (빈 리스트를 None으로)
    for day in DayOfWeek:
        if not operating_hours[day]:
            operating_hours[day] = None

    ratio_data = repository.get_ratio(store_id)
    ratio = get_ratio(ratio_data)

    return StoreInfoResponse(
        store_name=store_name,
        operating_hours=operating_hours,
        ratio=ratio
    )

def get_store_detailed(store_id: str) -> StoreDetailedResponse:

    store_information = repository.get_store_information(store_id)
    store_name = store_information['name']
    address = store_information['address']
    phone_number = store_information['phone_number']

    menus = []
    for menu in repository.get_menus(store_id):
        menus.append(MenuResponse(
            name = menu['name'],
            price = menu['price'],
            image_url = menu['image_url']
        ))

    images = []
    for image in repository.get_images(store_id):
        images.append(image['image_url'])

    return StoreDetailedResponse(
        store_name= store_name,
        address= address,
        phone_number= phone_number,
        operating_hours= get_operating_hours(repository.get_operating_hours(store_id)),
        menus= menus,
        images= images,
        ratio= get_ratio(repository.get_ratio(store_id))
    )