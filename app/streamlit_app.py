import streamlit as st
import requests

st.title("My Simple FastAPI App")

# Tạo sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Chọn chức năng:", ["Home", "Health Check"])

if option == "Home":
    st.header("Welcome!")
    if st.button("Get Message"):
        response = requests.get("https://your-app-url/")  # Thay your-app-url bằng URL của bạn
        st.json(response.json())

elif option == "Health Check":
    st.header("Health Status")
    if st.button("Check Health"):
        response = requests.get("https://your-app-url/health")  # Thay your-app-url bằng URL của bạn
        st.json(response.json())
