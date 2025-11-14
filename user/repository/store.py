from core.database import get_db_connection

def get_all_stores():

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "SELECT id, name, address, store_type FROM store"
    )

    return cur.fetchall()

def get_store_information(store_id: str):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select name, address, phone_number from store where id = %s",
        (store_id,)
    )

    return cur.fetchone()

def get_operating_hours(store_id: str):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select yoil, open_time, close_time from operating_hour where store_id = %s",
        (store_id,)
    )

    return cur.fetchall()

def get_menus(store_id: str):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select name, price, image from menu where store_id = %s",
        (store_id,)
    )

    return cur.fetchall()

def get_images(store_id: str):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select image from picture where store_id = %s",
        (store_id,)
    )

    return cur.fetchall()

def get_ratio(store_id: str):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select country, count(*) from occupy_history where store_id = %s group by country;",
        (store_id,)
    )

    return cur.fetchall()