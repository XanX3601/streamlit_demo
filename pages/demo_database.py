import streamlit as st
import psycopg

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query(
"""
SELECT
    customer_id,
    count(rental_id)
FROM
    rental
GROUP BY
    customer_id
"""
)

data = {'id': [row[0] for row in rows], 'rental_count': [row[1] * 1000 for row in rows]}

chart = st.bar_chart(data, x='id', y='rental_count')

