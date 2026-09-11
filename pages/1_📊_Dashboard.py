import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊")

st.title("System Health & Analytics")
st.markdown("This dashboard visualizes operational metrics. In a production environment, this connects directly to an Oracle DB or REST API to pull real-time health checks.")

st.markdown("---")

# Generate mock operational data for the last 24 hours
# (Using today's date: Sept 11, 2026)
np.random.seed(42)
date_rng = pd.date_range(start='2026-09-11', periods=24, freq='h')

df = pd.DataFrame({
    'Time': date_rng,
    'API_Response_Time_ms': np.random.normal(loc=120, scale=15, size=24), # Simulated latency
    'Database_Queries': np.random.randint(500, 3000, size=24)             # Simulated load
}).set_index('Time')

# Create layout columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("API Latency (ms)")
    st.line_chart(df['API_Response_Time_ms'], color="#FF4B4B")

with col2:
    st.subheader("Database Query Volume")
    st.bar_chart(df['Database_Queries'], color="#0068C9")
    
st.info("💡 **Tech Stack Used:** Python, Pandas, Streamlit, NumPy")