import streamlit as st

st.title("My first Streamlit web Apps",  anchor=False)

st.header("Content 1", divider=True)
st.subheader("Content 1 Subheader")

st.text("Hello World")



st.markdown(":red[**Hello**] *world*")
st.markdown(":blue-background[:orange[**Hello**]] *world* :world_map:")