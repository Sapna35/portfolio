import streamlit as st

# Configure the page settings
st.set_page_config(page_title="Sapna Rani | Portfolio", page_icon="👋", layout="wide")

st.title("Sapna Rani")
st.subheader("Software Engineer & Data Analyst")
st.write("Welcome to my dynamic portfolio. This application is built entirely in Python.")

# --- RESUME DOWNLOAD SECTION ---
try:
    with open("assets/Sapna_Rani_Naukri_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 Download My Resume",
        data=PDFbyte,
        file_name="Sapna_Rani_Resume.pdf",
        mime="application/octet-stream"
    )
except FileNotFoundError:
    st.warning("Resume file not found. Please ensure 'Sapna_Rani_Naukri_Resume.pdf' is in the 'assets' folder.")

st.markdown("---")
st.subheader("Core Competencies")
st.write("""
- **Backend & APIs:** Python, Java, REST APIs
- **Data & Analytics:** SQL, Pandas, PyTorch
- **QA Automation:** Playwright, Cucumber
""")