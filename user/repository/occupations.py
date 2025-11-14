from core.database import get_db_connection

def get_ratio():

    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "select country, count(*) from occupy_history group by country;"
    )

    return cur.fetchall()