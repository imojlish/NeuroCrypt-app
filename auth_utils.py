
import streamlit as st

# Dummy credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "password"
}

def login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

def is_authenticated():
    return st.session_state.get("authenticated", False)
