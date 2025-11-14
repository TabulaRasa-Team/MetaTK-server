from user.repository import occupations as repository
from user.service.store import get_ratio

FIXED_USER_ID = "96e8096e-c169-11f0-9219-ca5403729248"

def get_occupations():
    ratio_data = repository.get_ratio()
    print(ratio_data)
    return get_ratio(ratio_data)