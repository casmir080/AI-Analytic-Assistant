from fastapi import APIRouter
from app.db.queries import execute_query
from app.core.security import is_safe_query
from app.services.sql_generator import get_sql_from_question, generate_data_insight

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/run-query")
def run_query(query: str):
    if not is_safe_query(query):
        return {"error": "Only SELECT queries are allowed."}

    try:
        result = execute_query(query)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@router.post("/ask")
def ask(question: str):
    try:
        sql = get_sql_from_question(question)

        if not is_safe_query(sql):
            return {"error": "Generated query is not safe.", "sql": sql}

        result = execute_query(sql)

        insight = generate_data_insight(question, result)

        return {
            "question": question,
            "sql": sql,
            "data": result,
            "insight": insight
        }

    except Exception as e:
        return {"error": str(e)}