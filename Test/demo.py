import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="#",
)
st.title("Welcome to Streamlit demo application")
st.write("Dipika Borse")
st.image("13a98c40261296c534a4868124aecf91.jpg")
value = st.slider('Select your age', 0, 100, 50)
st.write(f'Selected value: {value}')
if st.button('Click Me'):
    st.write(f'your age is :{value}')
st.sidebar.success("select a page above")