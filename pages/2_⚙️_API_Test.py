import streamlit as st
import requests

st.set_page_config(page_title="API Integration", page_icon="⚙️")

st.title("REST API Integration")
st.markdown("This page demonstrates live data fetching and form handling. In a real-world scenario, these connect to Java Spring Boot or Python microservices.")

st.markdown("---")

# 1. GET Request Section
st.subheader("Fetch Live Data (GET Request)")
st.write("Click below to fetch user data from a public JSON API.")

if st.button("Run GET Request"):
    with st.spinner("Calling API..."):
        try:
            # Making a live HTTP GET request
            response = requests.get("https://jsonplaceholder.typicode.com/users")
            
            # Check for successful response (HTTP 200)
            if response.status_code == 200:
                st.success(f"Success! HTTP Status Code: {response.status_code}")
                data = response.json()
                
                # Display the first 3 records cleanly
                st.json(data[:3]) 
            else:
                # Handle potential errors like 400, 401, 403, or 500
                st.error(f"Request failed with Status Code: {response.status_code}")
        except Exception as e:
            st.error(f"Connection Error: {e}")

st.markdown("---")

# 2. POST Request (Form) Section
st.subheader("Submit Data (Simulated POST Request)")
st.write("Test out data submission via an interactive form.")

with st.form("api_form"):
    user_name = st.text_input("Name:")
    user_role = st.selectbox("Role:", ["Data Analyst", "Backend Engineer", "QA Automation"])
    sql_exp = st.slider("Years of SQL Experience:", 0, 10, 2)
    
    # The submit button triggers the form
    submitted = st.form_submit_button("Send POST Payload")
    
    if submitted:
        payload = {
            "name": user_name, 
            "role": user_role, 
            "sql_experience_years": sql_exp
        }
        st.info("Constructed JSON Payload:")
        st.json(payload)
        st.success("Payload successfully generated and ready for backend transmission.")