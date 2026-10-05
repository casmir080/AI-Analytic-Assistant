from app.services.llm_service import generate_sql, generate_insight


SCHEMA = """
Tables:

customers(customer_id, name, email, country, signup_date)
products(product_id, name, category, price)
orders(order_id, customer_id, product_id, quantity, order_date)

Relationships:
orders.customer_id → customers.customer_id
orders.product_id → products.product_id
"""


def build_prompt(question: str) -> str:
    return f"""
Convert the following question into a PostgreSQL SQL query.

Rules:
- Only use SELECT
- No explanations
- Use correct table joins
- Use aggregation if needed

Schema:
{SCHEMA}

Question:
{question}
"""


def rule_based_sql(question: str) -> str:
    q = question.lower()

    if "top" in q and "product" in q:
        return """
        SELECT p.name, SUM(o.quantity * p.price) AS revenue
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        GROUP BY p.name
        ORDER BY revenue DESC
        LIMIT 5;
        """

    if "total revenue" in q:
        return """
        SELECT SUM(o.quantity * p.price) AS total_revenue
        FROM orders o
        JOIN products p ON o.product_id = p.product_id;
        """

    if "orders per customer" in q:
        return """
        SELECT c.name, COUNT(o.order_id) AS total_orders
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.name
        ORDER BY total_orders DESC;
        """

    raise ValueError("No rule-based match for this question")


def get_sql_from_question(question: str) -> str:
    prompt = build_prompt(question)

    try:
        sql = generate_sql(prompt)

        sql = sql.replace("```sql", "").replace("```", "").strip()

        if not sql.lower().startswith("select"):
            raise ValueError("Invalid SQL generated")

        return sql

    except Exception as e:
        print("⚠️ LLM failed, switching to fallback:", e)
        return rule_based_sql(question)


def generate_data_insight(question: str, data: list) -> str:
    prompt = f"""
Question: {question}
Data:
{data}
Explain key insights in simple terms.
Focus on trends, highest values, and business meaning.
"""
    return generate_insight(prompt)