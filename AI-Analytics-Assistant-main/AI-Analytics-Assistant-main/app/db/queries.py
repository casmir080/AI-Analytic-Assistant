from app.db.connection import get_connection
from psycopg2.extras import RealDictCursor


def execute_query(query: str):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)

            if cursor.description:
                results = cursor.fetchall()
                return [dict(row) for row in results]

            return []

    finally:
        conn.close()