from core.database import get_db_connection

def get_coupon_history(user_id: str, coupon_id: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        "SELECT user_id, coupon_id, expiration, status FROM coupon_history WHERE user_id = %s AND coupon_id = %s",
        (user_id, coupon_id)
    )

    return cur.fetchone()

def update_coupon_status(user_id: str, coupon_id: str, status: str):
    con = get_db_connection()
    cur = con.cursor()

    cur.execute(
        "UPDATE coupon_history SET status = %s WHERE user_id = %s AND coupon_id = %s",
        (status, user_id, coupon_id)
    )

    con.commit()

def get_my_coupons(user_id: str, sort: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    order_by_clause = {
        "recent": "ch.expiration DESC",
        "old": "ch.expiration ASC",
        "expiration": "ch.expiration ASC"
    }

    query = f"""
        SELECT
            c.id as coupon_id,
            c.name as coupon_name,
            s.name as store_name,
            ch.expiration,
            s.store_type
        FROM coupon_history ch
        JOIN coupon c ON ch.coupon_id = c.id
        JOIN store s ON c.store_id = s.id
        WHERE ch.user_id = %s AND ch.status = 'notUsed'
        ORDER BY {order_by_clause.get(sort, 'ch.expiration DESC')}
    """

    cur.execute(query, (user_id,))

    return cur.fetchall()

def get_coupon_detail(user_id: str, coupon_id: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute(
        """
        SELECT
            c.id as coupon_id,
            c.name as coupon_name,
            s.name as store_name,
            ch.expiration,
            s.store_type
        FROM coupon_history ch
        JOIN coupon c ON ch.coupon_id = c.id
        JOIN store s ON c.store_id = s.id
        WHERE ch.user_id = %s AND ch.coupon_id = %s AND ch.status = 'notUsed'
        """,
        (user_id, coupon_id)
    )

    return cur.fetchone()

def get_store_coupons(user_id: str, store_id: str, sort: str):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    order_by_clause = {
        "recent": "ch.expiration DESC",
        "old": "ch.expiration ASC",
        "expiration": "ch.expiration ASC"
    }

    query = f"""
        SELECT
            c.id as coupon_id,
            c.name as coupon_name,
            s.name as store_name,
            ch.expiration,
            s.store_type
        FROM coupon_history ch
        JOIN coupon c ON ch.coupon_id = c.id
        JOIN store s ON c.store_id = s.id
        WHERE ch.user_id = %s AND s.id = %s AND ch.status = 'notUsed'
        ORDER BY {order_by_clause.get(sort, 'ch.expiration DESC')}
    """

    cur.execute(query, (user_id, store_id))

    return cur.fetchall()