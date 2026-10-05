import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="AI Analytics Assistant", layout="wide")

st.title("AI Analytics Assistant")
st.caption("Ask business questions. Get SQL, data, charts, and insights.")

# Query history init
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar history
st.sidebar.title("Query History")
for q in st.session_state.history[-5:]:
    if st.sidebar.button(q):
        question = q

question = st.text_input("Ask a business question:")

if st.button("Run Query"):
    if question:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, params={"question": question})

        if response.status_code == 200:
            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                st.success("Query executed successfully")

                st.session_state.history.append(question)

                st.subheader("Generated SQL")
                st.code(data["sql"], language="sql")

                df = pd.DataFrame(data["data"])

                st.subheader("Results")

                if df.empty:
                    st.warning("No data returned.")
                else:
                    st.dataframe(df)

                    if len(df.columns) >= 2:
                        st.subheader("Chart")

                        x_col = df.columns[0]
                        y_col = df.columns[1]

                        fig, ax = plt.subplots()

                        if "date" in x_col.lower():
                            ax.plot(df[x_col], df[y_col])
                        else:
                            ax.bar(df[x_col], df[y_col])

                        ax.set_xlabel(x_col)
                        ax.set_ylabel(y_col)
                        plt.xticks(rotation=45, ha="right")
                        plt.tight_layout()

                        st.pyplot(fig)

                st.subheader("AI Insight")
                st.info(data.get("insight", "No insight available"))

        else:
            st.error(f"API request failed with status {response.status_code}")
    else:
        st.warning("Please enter a question.")