from fastapi import APIRouter, Depends
from core.database import get_db, test_connection

router = APIRouter(prefix="/db", tags=["Database"])


@router.get("/test")
def test_db_connection():
    """
    데이터베이스 연결 테스트 엔드포인트

    Returns:
        dict: 연결 성공 여부 및 MySQL 버전 정보
    """
    try:
        result = test_connection()
        if result:
            return {
                "status": "success",
                "message": "Database connection successful"
            }
        else:
            return {
                "status": "failed",
                "message": "Database connection failed"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Connection error: {str(e)}"
        }


@router.get("/query-test")
def query_test(db=Depends(get_db)):
    """
    데이터베이스 쿼리 테스트 엔드포인트

    Returns:
        dict: MySQL 버전 및 현재 데이터베이스 정보
    """
    try:
        con, cur = db

        # MySQL 버전 조회
        cur.execute("SELECT VERSION() as version")
        version = cur.fetchone()

        # 현재 데이터베이스명 조회
        cur.execute("SELECT DATABASE() as database_name")
        db_name = cur.fetchone()

        # 현재 사용자 조회
        cur.execute("SELECT USER() as user")
        user = cur.fetchone()

        return {
            "status": "success",
            "data": {
                "mysql_version": version['version'],
                "database_name": db_name['database_name'],
                "user": user['user']
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Query error: {str(e)}"
        }


@router.get("/tables")
def show_tables(db=Depends(get_db)):
    """
    현재 데이터베이스의 테이블 목록 조회

    Returns:
        dict: 테이블 목록
    """
    try:
        con, cur = db
        cur.execute("SHOW TABLES")
        tables = cur.fetchall()

        return {
            "status": "success",
            "tables": tables
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error: {str(e)}"
        }