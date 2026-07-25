import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Form", page_icon="📝", layout="centered")

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"], .main {
            background: #000000 !important;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 980px;
        }
        .card {
            background: rgba(255,255,255,0.96);
            border-radius: 24px;
            padding: 1.4rem;
            margin-bottom: 1rem;
            box-shadow: 0 12px 35px rgba(0,0,0,0.16);
            border: 1px solid #e2e8f0;
        }
        .dark-card {
            background: linear-gradient(135deg, #111827, #1f2937);
            color: #f8fafc;
            border: 1px solid #374151;
        }
        .title {
            font-size: 1.8rem;
            font-weight: 800;
            margin-bottom: 0.3rem;
            color: #0f172a;
        }
        .dark-card .title {
            color: #f8fafc;
        }
        .subtitle {
            color: #64748b;
            margin-bottom: 1rem;
        }
        .dark-card .subtitle {
            color: #cbd5e1;
        }
        .section {
            background: #ffffff;
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid #e2e8f0;
        }
        .dark-card .section {
            background: rgba(255,255,255,0.05);
            border-color: #374151;
        }
        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {
            color: #f8fafc !important;
            background-color: #000000 !important;
            border: 1.5px solid #38bdf8 !important;
            border-radius: 12px !important;
            padding: 0.65rem 0.8rem !important;
            box-shadow: none !important;
        }
        div[data-testid="stTextInput"] > div,
        div[data-testid="stTextArea"] > div {
            background-color: transparent !important;
        }
        .dark-card div[data-testid="stTextInput"] input,
        .dark-card div[data-testid="stTextArea"] textarea {
            color: #f8fafc !important;
            background-color: #000000 !important;
            border-color: #38bdf8 !important;
        }
        .stButton > button {
            background: linear-gradient(135deg, #0ea5e9, #8b5cf6);
            color: white !important;
            border: none;
            border-radius: 999px;
            padding: 0.7rem 1.3rem;
            font-weight: 700;
            box-shadow: 0 10px 24px rgba(14,165,233,0.25);
        }
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 12px 28px rgba(14,165,233,0.35);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "saved_name" not in st.session_state:
    st.session_state.saved_name = ""
if "saved_father" not in st.session_state:
    st.session_state.saved_father = ""
if "saved_address" not in st.session_state:
    st.session_state.saved_address = ""

st.markdown(
    """
    <div class="card dark-card">
        <div class="title">Student Registration Form</div>
        <div class="subtitle">Fill your details section by section and save each part.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="card dark-card">
        <div class="title">Section 1</div>
        <div class="subtitle">Save your Name</div>
    </div>
    """,
    unsafe_allow_html=True,
)
name = st.text_input("Enter your Name:", placeholder="Type your Name here...", key="name_input")
save_name = st.button("Save Name", key="save_name")
if save_name:
    st.session_state.saved_name = name
    st.success("Name saved successfully")

st.markdown(
    """
    <div class="card dark-card">
        <div class="title">Section 2</div>
        <div class="subtitle">Save your Father's name</div>
    </div>
    """,
    unsafe_allow_html=True,
)
father_name = st.text_input("Enter your Father's name:", placeholder="Type your Father's name here...", key="father_input")
save_father = st.button("Save Father's Name", key="save_father")
if save_father:
    st.session_state.saved_father = father_name
    st.success("Father's name saved successfully")

st.markdown(
    """
    <div class="card dark-card">
        <div class="title">Section 3</div>
        <div class="subtitle">Save your Address</div>
    </div>
    """,
    unsafe_allow_html=True,
)
address = st.text_area("Enter your Address:", placeholder="Type your full Address here...", key="address_input")
save_address = st.button("Save Address", key="save_address")
if save_address:
    st.session_state.saved_address = address
    st.success("Address saved successfully")

st.markdown(
    """
    <div class="card dark-card">
        <div class="title">Class</div>
        <div class="subtitle">Choose your Class</div>
    </div>
    """,
    unsafe_allow_html=True,
)
classdata = st.selectbox("Enter your Class:", ["Class 1", "Class 2", "Class 3"], key="class_data")

submit_button = st.button("Submit All", key="submit_all")
if submit_button:
    data = {
        "Name": [st.session_state.saved_name],
        "Father's Name": [st.session_state.saved_father],
        "Address": [st.session_state.saved_address],
        "Class": [classdata],
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)