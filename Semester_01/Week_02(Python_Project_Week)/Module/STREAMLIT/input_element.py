import streamlit as st

st.title("Input your Information",anchor =False)
st.divider()

name = st.text_input("Enter your name", placeholder="Type your name")

print(type(name))

st.write("Your name is: ", name)

st.divider()

age = st.number_input("Enter your age", value = None, placeholder="Enter your age")

print(type(age))

st.write("Your age is : ", age)

password = st.text_input("Enter your password",type="password", placeholder="Enter your password")

print(type(password))

st.write("Your password is: ", password)

selected = st.selectbox("Chose your profession",
             ("Student", "Employe", "Businessman"),
             index = None,
             accept_new_options= True
            #  placeholder="Select"
             )

print(type(selected))

st.write("You selected: ", selected)

pressed = st.button("Enter to Confirm", type="primary")

if pressed :
    st.write(f"Yor name is {name} and your age is {age}")
