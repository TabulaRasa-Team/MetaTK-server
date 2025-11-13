import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# .env 파일 로드
load_dotenv()

# 환경변수에서 데이터베이스 설정 가져오기
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME")


def get_db_connection():
    """
    MySQL 데이터베이스 연결 생성

    Returns:
        connection: mysql.connector connection 객체

    사용 예시:
        con = get_db_connection()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
        finally:
            cur.close()
            con.close()
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        raise e


def get_db():
    """
    FastAPI 의존성으로 사용할 데이터베이스 연결 및 커서 생성 함수

    Yields:
        tuple: (connection, cursor)

    사용 예시:
        @app.get("/users")
        def get_users(db = Depends(get_db)):
            con, cur = db
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            return users
    """
    con = get_db_connection()
    cur = con.cursor(dictionary=True)  # 딕셔너리 형태로 결과 반환
    try:
        yield con, cur
    finally:
        cur.close()
        con.close()


# 연결 테스트 함수
def test_connection():
    """
    데이터베이스 연결 테스트

    사용 예시:
        if __name__ == "__main__":
            test_connection()
    """
    try:
        con = get_db_connection()
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT VERSION() as version")
        version = cur.fetchone()
        print(f"Database connection successful!")
        print(f"MySQL Version: {version}")
        cur.close()
        con.close()
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
