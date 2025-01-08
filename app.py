import streamlit as st
import test
from PIL import Image

t = test.result()

foods = t.food()

st.markdown("<h1 style='text-align: center;'>Food Recommendation System</h1>", unsafe_allow_html=True)

st.write("-----------------")
food_choice = st.selectbox("เลือกเมนูอาหาร ", foods)
st.write("------------------")

c1, c2, c3 = st.columns(3)

m1, m2, m3 = t.query(food_choice)

with c1:
    st.subheader("Simple Content Based Filtering")
    st.write("แนะนำเมนูอาหาร โดยอ้างอิงจากอาหารที่มีความคล้ายคลึงกัน")
    st.write("------------------")
    for index, ele in enumerate(m1):
        st.write(index,ele.title())
    st.write("------------------")

with c2:
    st.subheader("Collaborative Based Filtering")
    st.write("แนะนำเมนูอาหาร โดยอ้างอิงจากผู้ใช้ที่มีความชอบคล้ายกัน")
    st.write("------------------")
    if m3 == None:
        st.write("**ข้อมูลการให้คะแนนของผู้ใช้น้อยเกินไป !!!**")
        st.write("ไม่สามารถแนะนำเมนูอาหารได้ ระบบจะรวบรวมข้อมูลเมื่อข้อมูลการให้คะแนนของลูกค้า มีการอัพเดต")
    else:
        for index, ele in enumerate(m3):
            st.write(index, ele.title())

    st.write("------------------")

with c3:
    st.subheader("Advanced Content Based Filtering")
    st.write("แนะนำเมนูอาหาร โดยอ้างอิงจากเมนูอาหารที่คล้ายกัน และคุณลักษณะของอาหารนั้นๆ (ประเภทอาหาร วัตถุดิบ ส่วนผสม)")
    st.write("------------------")
    for index, ele in enumerate(m2):
        st.write(index, ele.title())
    st.write("------------------")