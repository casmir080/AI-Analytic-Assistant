from fastapi import FastAPI
from app.api.routes import router
from app.services.sql_generator import get_sql_from_question
from app.db.queries import execute_query
from app.core.security import is_safe_query

app = FastAPI(title="AI Analytics Assistant")

app.include_router(router)

@app.post("/ask")
def ask(question: str):
    try:
        sql = get_sql_from_question(question)

        if not is_safe_query(sql):
            return {"error": "Generated query was not safe."}

        data = execute_query(sql)

        return {"sql": sql, "data": data}

    except Exception as e:
        return {"error": str(e)}