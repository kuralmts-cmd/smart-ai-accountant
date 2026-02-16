import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Sahifa dizayni (Dizayndagi kabi zamonaviy ko'rinish)
st.set_page_config(page_title="Smart AI Accountant", page_icon="🧾", layout="centered")

# Global CSS uslubi
st.markdown("""
    <style>
    .stButton>button {
        background-color: #00aaff;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .main { background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# 2. Gemini AI Sozlamasi
# Kural aka, o'zingizning API kalitingizni mana shu qo'shtirnoq ichiga qo'ying:
API_KEY = "SIZNING_NUSXALANGAN_KALITINGIZ" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Ilova sarlavhasi
st.title("🚀 Smart AI Accountant")
st.write("Scan any receipt, anywhere in the world.")

# 4. Fayl yuklash (Magic Scan)
uploaded_file = st.file_uploader("Rasmni tanlang...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Yuklangan chek', use_column_width=True)
    
    if st.button('✨ MAGIC SCAN'):
        with st.spinner('AI tahlil qilmoqda...'):
            # Prompt (AI ga buyruq)
            prompt = """
            Analyze this receipt. Extract:
            1. Store Name
            2. Date
            3. Items and Prices
            4. Total Amount and Currency
            Format the result as a very clean summary.
            """
            
            response = model.generate_content([prompt, image])
            
            st.markdown("### 📊 AQLLI NATIJA")
            st.write(response.text)
            st.success("Tahlil yakunlandi!")

st.write("---")
st.caption("Click & Get loyihasi uchun maxsus tayyorlandi.")
