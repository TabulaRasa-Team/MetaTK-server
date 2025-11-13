from fastapi import HTTPException

from core.database import get_db_connection
from owner.model.owner import Store, DayOfWeek


def create_store(store_id: str, store_type_value: str, request: Store):

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select * from store where bln = %s",
        (request.bln,)
    )

    if cur.fetchone() is None:
        cur.execute(
            "insert into store(id, name, address, phone_number, store_type, bln, owner_name)" +
            "values(%s, %s, %s, %s, %s, %s, %s)",
            (store_id, request.company_name, request.address, request.phone_number, store_type_value, request.bln, request.owner_name)
        )
        con.commit()

        for day in DayOfWeek:
            cur.execute(
                "insert into operating_hour(store_id, yoil, open_time, close_time)" +
                "values(%s, %s, %s, %s)",
                (store_id, day.value, request.operating_hours[day][0], request.operating_hours[day][1])
            )
        con.commit()

        # test
        cur.execute("select * from store")
        print(cur.fetchall())
        cur.execute("select * from operating_hour")
        print(cur.fetchall())

        cur.close()
        con.close()