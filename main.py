import streamlit as st

st.title("Hello World")
st.write("How are you doing?")

if st.button(label="Click Me"):
    st.write("You clicked me!")
else:
    st.write("You didn't click me!")
