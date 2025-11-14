from owner.model.owner import DayOfWeek
from user.model.store import StoreDetailedResponse, MenuResponse
from user.repository import store as repository

def get_store_detailed(store_id: str) -> StoreDetailedResponse:

    store_information = repository.get_store_information(store_id)
    store_name = store_information['name']
    address = store_information['address']
    phone_number = store_information['phone_number']

    operating_hours = {day: [] for day in DayOfWeek}

    for operating_hour in repository.get_operating_hours(store_id):
        day_enum = DayOfWeek(operating_hour['yoil'])
        operating_hours[day_enum].append(str(operating_hour['open_time']))
        operating_hours[day_enum].append(str(operating_hour['close_time']))

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

    ratio = {}
    total = 0
    for data in repository.get_ratio(store_id):
        count = int(data['count(*)'])
        country = data['country']
        total += count
        ratio[country] = count

    ratio = {country : round(count/total, 2) for country, count in ratio.items()}

    return StoreDetailedResponse(
        store_name= store_name,
        address= address,
        phone_number= phone_number,
        operating_hours= operating_hours,
        menus= menus,
        images= images,
        ratio= ratio
    )