import streamlit as st

st.title("Input yor files",anchor=False)
st.divider()

# storage
st.image(r"D:\Mominur_images\mominur.jpg")

# Url
st.image("https://th.bing.com/th/id/OIP.F787S02J8v7JJGkviaCDNAHaEE?w=272&h=180&c=7&r=0&o=7&pid=1.7&rm=3")

images = st.file_uploader("Enter your image",
                         type=['jpg','jpeg','png'],
                         accept_multiple_files=True
                         )

print(type(images))

if images:
    if(len(images)>2):
        st.warning("You uploaded 3 photos")
    col = st.columns(len(images))

    # for i, img in enumerate(images):
    #     col[i].image(img)

    for i, img in enumerate(images):
        with col[i]:
            st.image(img)