import streamlit as st
st.title("เเอปพลิเคชั่นเเปลงปี พ.ศ. เป็น ค.ศ.")

bh_yrar=st.number_input("กรอกปี พ.ศ. ที่ต้องการเเปลง", value=2569)
ce_year=bhyear-543
st.header(f"ปี ค.ศ. คือ : {ce_y}")
