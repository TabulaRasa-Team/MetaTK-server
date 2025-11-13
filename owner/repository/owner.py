from core.database import get_db_connection
from owner.model.owner import Store, DayOfWeek

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