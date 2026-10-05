🚀 AI-Powered Analytics Assistant

A full-stack data + AI system that converts natural language into SQL queries, executes them on PostgreSQL, and returns data, visualizations, and insights.

🔥 Features Natural language → SQL (LLM-powered) Secure query execution (SELECT-only) PostgreSQL analytics backend FastAPI production API Streamlit interactive dashboard Automatic chart generation AI-generated business insights 🧱 Tech Stack Python FastAPI PostgreSQL Streamlit Groq (Llama3) ⚙️ How It Works User asks a question LLM converts it to SQL SQL is validated (safe execution) Query runs on PostgreSQL Results returned + visualized LLM generates insight 📸 Screenshots

(Add your images here)

▶️ Run Locally git clone cd ai-analytics-assistant

python -m venv venv venv\Scripts\activate

pip install -r requirements.txt

Setup .env file
uvicorn app.main:app --reload streamlit run frontend.py 🧠 Example Queries Top 5 products by revenue Total revenue by country Top customers by spending Monthly revenue trend ⚠️ Limitations Depends on schema awareness LLM may generate imperfect SQL No authentication (yet) 🚀 Future Improvements Query caching Authentication Deployment (cloud) Better chart selection Semantic layer / embeddings
