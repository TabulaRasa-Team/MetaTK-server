from core.database import get_db_connection
from owner.model.owner import Store, Coupon


def check_duplicate_bln(bln: str):
    con = get_db_connection()
    cur = con.cursor()

    cur.execute(
        "select * from store where bln = %s",
        (bln,)
    )

    return cur.fetchone()

def create_store(store_id: str, store_type_value: str, request: Store):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "insert into store(id, name, address, phone_number, store_type, bln, owner_name)" +
        "values(%s, %s, %s, %s, %s, %s, %s)",
        (store_id, request.company_name, request.address, request.phone_number, store_type_value, request.bln, request.owner_name)
    )
    con.commit()

def create_operating_hour(store_id: str, day: str, open_time: str, close_time: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "insert into operating_hour(store_id, yoil, open_time, close_time)" +
        "values(%s, %s, %s, %s)",
        (store_id, day, open_time, close_time)
    )

    con.commit()

def create_operating_hour_for_holiday(store_id: str, day: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "insert into operating_hour(store_id, yoil, open_time, close_time)" +
        "values(%s, %s, null, null)",
        (store_id, day)
    )

    con.commit()

def check_store_id(store_id: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select * from store where id = %s",
        (store_id,)
    )

    return cur.fetchall()

def create_coupon(coupon_id: str, request: Coupon, status: str, validity_period: int):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "INSERT INTO coupon(id, store_id, status, name, validity_period) VALUES(%s, %s, %s, %s, %s)",
        (coupon_id, str(request.store_id), status, request.name, validity_period)
    )

    con.commit()

def get_users_by_country(country: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "SELECT id FROM user WHERE country = %s",
        (country,)
    )

    return cur.fetchall()

def insert_coupon_history(user_id: str, coupon_id: str, expiration: str, status: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "INSERT INTO coupon_history(user_id, coupon_id, expiration, status) VALUES(%s, %s, %s, %s)",
        (user_id, coupon_id, expiration, status)
    )

    con.commit()

def insert_menu(store_id: str, menu_name: str, price: int, image: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    menu_id = str(__import__('uuid').uuid4())
    cur.execute(
        "INSERT INTO menu(id, store_id, name, price, image) VALUES(%s, %s, %s, %s, %s)",
        (menu_id, store_id, menu_name, price, image)
    )

    con.commit()

def insert_picture(store_id: str, image: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    picture_id = str(__import__('uuid').uuid4())
    cur.execute(
        "INSERT INTO picture(id, store_id, image) VALUES(%s, %s, %s)",
        (picture_id, store_id, image)
    )

    con.commit()