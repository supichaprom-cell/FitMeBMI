import streamlit as st
import joblib
import numpy as np

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="fitMeBMI",
    page_icon="💪",
    layout="centered"
)

# CSS สไตล์ Gen Z
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fceaff, #e0f7ff);
    }

    .stButton>button {
        background-color: #ff7eb9;
        color: white;
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #ff4fa3;
        color: white;
    }

    .result-box {
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        background: white;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# โหลดโมเดล
model = joblib.load("bmi_model.pkl")

# ส่วนหัว
st.markdown("""
<h1 style='text-align: center; color: #ff4fa3;'>
🏋️ fitMeBMI Checker
</h1>
<p style='text-align: center; font-size:18px;'>
กรอกข้อมูลของคุณ แล้วมาดูสุขภาพกันเลย ✨
</p>
""", unsafe_allow_html=True)

st.divider()

# รับข้อมูลผู้ใช้
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 อายุ (ปี)", 10, 100, 25)

with col2:
    height = st.number_input("📏 ส่วนสูง (cm)", 100, 220, 170)

weight = st.number_input("⚖️ น้ำหนัก (kg)", 30, 200, 65)

# ปุ่มทำนาย
if st.button("✨ ทำนาย BMI"):
    input_data = np.array([[age, height, weight]])
    prediction = model.predict(input_data)[0]
    bmi = round(prediction, 2)

    # แปลผล
    if bmi < 18.5:
        status = "น้ำหนักน้อย 🥺"
        color = "#6ec6ff"
    elif bmi < 23:
        status = "ปกติ สุขภาพดี 💚"
        color = "#66bb6a"
    elif bmi < 25:
        status = "น้ำหนักเกินนิดหน่อย 😅"
        color = "#ffa726"
    elif bmi < 30:
        status = "อ้วนระดับ 1 😬"
        color = "#ef5350"
    else:
        status = "อ้วนระดับ 2 🚨"
        color = "#d32f2f"

    # กล่องผลลัพธ์
    st.markdown(f"""
    <div class="result-box">
        <h2 style="color:{color};">BMI ของคุณ: {bmi}</h2>
        <h3 style="color:{color};">{status}</h3>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ตารางเกณฑ์
with st.expander("📊 ดูเกณฑ์การแปลผล BMI"):
    st.markdown("""
    **เกณฑ์ BMI สำหรับคนเอเชีย**
    
    - น้อยกว่า 18.5 → น้ำหนักน้อย  
    - 18.5 – 22.9 → ปกติ  
    - 23 – 24.9 → น้ำหนักเกิน  
    - 25 – 29.9 → อ้วนระดับ 1  
    - 30 ขึ้นไป → อ้วนระดับ 2  
    """)
