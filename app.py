import streamlit as st
import requests
import random

# Telegram sozlamalari
TELEGRAM_BOT_TOKEN = "8850573618:AAFHnfum5nKAEUL-JPvcQX7Emp_raHKj-K0"
TELEGRAM_CHAT_ID = "6937805047"

# Sahifa sarlavhasi va dizayni
st.set_page_config(page_title="Shahobiddin bilan Tanishuv", page_icon="👋", layout="centered")

# Streamlit to'q rangli mavzusi bilan mos sarlavha
st.markdown("<h2 style='color: #ff4b4b;'>Streamlit Quiz App v7.0</h2>", unsafe_allow_html=True)
st.divider()

# Xabarni telegramga yuborish funksiyasi
def send_to_telegram(data, percent):
    message = (
        f"🌟 *YANGI ISHTIROKCHI REKORDI!* 🌟\n"
        f"👤 *Kursdosh:* {data['name']}\n"
        f"📊 *Matematik Moslik:* {percent}%\n\n"
        f"💡 *Qiziqishi:* {data['interest']}\n"
        f"🍲 *Yoqtirgan taomi:* {data['food']}\n"
        f"🎨 *Yoqtirgan rangi:* {data['color']}\n"
        f"🎵 *Qo'shiq/Janr:* {data['song']}\n"
        f"🎂 *Tug'ilgan kuni:* {data['birthday']}\n"
        f"🌟 *Katta orzusi:* {data['dream']}"
    )
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"})
    except:
        pass

# Session state (sahifalarni boshqarish uchun)
if "step" not in st.session_state:
    st.session_state.step = "start"
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 1. BOSHANG'ICH SAHIFA
if st.session_state.step == "start":
    st.subheader("Assalomu alaykum, aziz Kursdoshim! 👋")
    st.write(
        "Men **Hamroqulov Shahobiddin** sizlarning hammalaringiz bilan yaqinroqdan tanishish "
        "va iloji boricha sizlarga yaqinroq bo‘lish uchun ushbu saytni yaratdim. "
        "O‘ylaymanki, mehnatni qadrlagan holda ushbu viktorinamizga javob berasiz."
    )
    st.info("💡 Bu tizim sizning men bilan qanchalik mos kelishingizni taxminiy matematik hisob-kitob qilib beradi!")
    
    if st.button("O'yinni Boshlash 🚀", type="primary", use_container_width=True):
        st.session_state.step = "quiz"
        st.rerun()

# 2. VIKTORINA SAVOLLARI
elif st.session_state.step == "quiz":
    # Ism so'rash
    if "name" not in st.session_state.answers:
        name = st.text_input("Sizni to'liq ismingiz nima? ✍️", placeholder="Ism va familiyangiz...")
        if st.button("Keyingisi ➡️", type="primary"):
            if name.strip() != "":
                st.session_state.answers["name"] = name
                st.rerun()
            else:
                st.error("Iltimos, ismingizni kiriting!")

    # Qiziqish
    elif "interest" not in st.session_state.answers:
        interest = st.radio("Sizni eng ko'p nima qiziqtiradi? 💡", ["Dasturlash / IT", "Biznes / Startap", "San'at / Musiqa", "Sport / Sayohat"])
        if st.button("Keyingisi ➡️", type="primary"):
            st.session_state.answers["interest"] = interest
            st.rerun()

    # Taom
    elif "food" not in st.session_state.answers:
        food = st.radio("Yoqtirgan taomingiz qaysi? 🍲", ["Osh (Palov)", "Shashlik / Kabob", "Fast-food (Lavash/Pitsa)", "Suyuq taomlar"])
        if st.button("Keyingisi ➡️", type="primary"):
            st.session_state.answers["food"] = food
            st.rerun()

    # Rang
    elif "color" not in st.session_state.answers:
        color = st.radio("Sizga eng yoqadigan rang? 🎨", ["To'q qora / Kulrang", "Yorqin ko'k / Havorang", "Oq / Toza ranglar", "Yashil / Tabiat"])
        if st.button("Keyingisi ➡️", type="primary"):
            st.session_state.answers["color"] = color
            st.rerun()

    # Qo'shiq
    elif "song" not in st.session_state.answers:
        song = st.text_input("Qanday janrdagi qo'shiqlarni sevasiz? 🎵", placeholder="Yoqtirgan qo'shig'ingiz yoki janringiz...")
        if st.button("Keyingisi ➡️", type="primary"):
            if song.strip() != "":
                st.session_state.answers["song"] = song
                st.rerun()
            else:
                st.error("Iltimos, ushbu maydonni to'ldiring!")

    # Tug'ilgan kun
    elif "birthday" not in st.session_state.answers:
        st.write("Tug'ilgan kuningiz qachon? 🎂")
        birthday = st.date_input("Sanani tanlang:", min_value=None, max_value=None)
        if st.button("Keyingisi ➡️", type="primary"):
            st.session_state.answers["birthday"] = str(birthday)
            st.rerun()

    # Orzu
    elif "dream" not in st.session_state.answers:
        dream = st.text_area("Kelajakdagi eng katta orzuingiz nima? 🌟", placeholder="Kelajakdagi maqsadlaringiz haqida...")
        if st.button("Natijani ko'rish 📊", type="primary"):
            if dream.strip() != "":
                st.session_state.answers["dream"] = dream
                st.session_state.step = "final"
                st.rerun()
            else:
                st.error("Iltimos, orzuingizni yozing!")

# 3. FINAL SAHIFA
elif st.session_state.step == "final":
    st.balloons()
    st.success("O'yin Yakunlandi! 🎉")
    
    # Foiz hisoblash
    if "percent" not in st.session_state:
        st.session_state.percent = random.randint(75, 99)
        send_to_telegram(st.session_state.answers, st.session_state.percent)
        
    st.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{st.session_state.percent}%</h1>", unsafe_allow_html=True)
    st.subheader(f"Daxshat! Siz Shahobiddin bilan {st.session_state.percent}% mos keldingiz! 🚀")
    
    st.divider()
    st.write("Shahobiddin bilan Instagramda bog'lanish va rahmat aytish:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📸 @mr.shahobiddin5", "https://instagram.com", use_container_width=True)
    with col2:
        st.link_button("🎓 @csu.university", "https://instagram.com", use_container_width=True)

    if st.button("Qayta boshlash 🔄"):
        st.session_state.clear()
        st.rerun()
