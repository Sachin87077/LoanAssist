import streamlit as st
import requests

BACKEND_URL = st.sidebar.text_input(
    "Backend base URL", "http://127.0.0.1:8001"
)

st.set_page_config(page_title="LoanAssist", layout="wide")

st.title("💬 LoanAssist — Smart Loan Assistant")

# Session state
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Enter your message")

if st.button("Send") and user_input:
    resp = requests.post(
        f"{BACKEND_URL}/chat",
        json={"message": user_input}
    ).json()

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("LoanAssist", resp["reply"]))

for role, msg in st.session_state.chat:
    st.markdown(f"**{role}:** {msg}")
