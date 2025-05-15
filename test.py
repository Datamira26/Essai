import streamlit as st
st.title('Hello GoMycode')
st.header('streamlit app')
st.subheader('A.fisrt exemple')
st.text('text')
st.markdown('<h1> this is a mark down<!/h1>',unsafe_allow_html=True)
st.success("success")
st.info('information missing')
st.warning('Warning')
st.error('error')
exp=ZeroDivisionError("Trying to devide by zero")
st.exception(exp)
'''
from PIL import Image
img=Image.open(r"https://th.bing.com/th/id/OIP.OpswJwVFceXjSTwTY34dBAHaFj?cb=iwc2&rs=1&pid=ImgDetMain")
st.image(img, width=800, caption='essai')'''
if st.checkbox("show/hide"):
    st.text('showing the widget')
status= st.radio("select gender:", ("Male","Female"))
if (status=="Male"):
    st.success(" Selected choice: Male")
else:
    st.success(' Selected choice: Female')
hobby= st.selectbox("hobbies:",['Dancing','Reading','Sport'])
hobbies=st.multiselect("Hobbies :",['Dancing','Reading','Sport'])
st.write("You selected:", len(hobbies)," hobbies")
st.write("You selected:")
for i in hobbies:
    st.success(i)
level=st.slider("select the level",1,5)
st.text('select value : {}'.format(level))
st.button("Click me if you like the form")
if(st.button("About")):
    st.text("welcome to GoMycode")
name=st.text_input("Enter your name","Type here .....")
if(st.button('Submit')):
    result=name.title()
    result='you entred '+result
    st.success(result)
