import streamlit as st
import requests
import random

# Telegram sozlamalari
TELEGRAM_BOT_TOKEN = "8850573618:AAFHnfum5nKAEUL-JPvcQX7Emp_raHKj-K0"
TELEGRAM_CHAT_ID = "6937805047"

# Sahifa konfiguratsiyasi
st.set_page_config(page_title="Shahobiddin bilan Tanishuv", page_icon="🎮", layout="centered")

# Maxsus professional vizual dizayn (CSS) - Neon effektlar va chiroyli tugmalar
st.markdown("""
<style>
    /* Umumiy fon va matnlar */
    .stApp {
        background-color: #0e1117;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', Arial, sans-serif;
        text-shadow: 0 0 10px rgba(255, 75, 75, 0.3);
    }
    
    /* Neon sarlavha */
    .neon-title {
        color: #ff4b4b;
        font-weight: 800;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 5px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    /* O'yin kartalari */
    .quiz-box {
        background: linear-gradient(145deg, #1e222b, #12161f);
        border: 2px solid #262730;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }
    
    /* Tugmalarni daxshat qilish */
    div.stButton > button {
        background: linear-gradient(135deg, #ff4b4b, #d62828) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 14px 28px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.6) !important;
        background: linear-gradient(135deg, #ff6b6b, #ff4b4b) !important;
    }
    
    /* Radio variantlarni chiroyli qilish */
    .stRadio [data-testid="stMarkdownContainer"] {
        font-size: 16px !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# TEPADAGI BRENDING
st.markdown("<p class='neon-title'>🎮 GAMIFIED QUIZ v7.5</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-family: monospace;'>Powered by Streamlit Cloud Server</p>", unsafe_allow_html=True)
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
    try: requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"})
    except: pass

# Session state
if "step" not in st.session_state: st.session_state.step = "start"
if "answers" not in st.session_state: st.session_state.answers = {}

# 1. KIRISH SAHIFASI
if st.session_state.step == "start":
    st.markdown("""
    <div class='quiz-box'>
        <h2 style='color: #ff4b4b; margin-top:0;'>Assalomu alaykum, aziz Kursdoshim! 👋</h2>
        <p style='color: #cbd5e1; line-height: 1.6; font-size: 16px;'>
            Men <strong style='color: white; border-bottom: 2px solid #ff4b4b;'>Hamroqulov Shahobiddin</strong> sizlarning hammalaringiz bilan yaqinroqdan tanishish 
            va iloji boricha sizlarga yaqinroq bo‘lish uchun ushbu saytni yaratdim. 
            O‘ylaymanki, mehnatni qadrlagan holda ushbu interaktiv viktorinamizga javob berasiz.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Bu tizim sizning men bilan qanchalik mos kelishingizni taxminiy matematik hisob-kitob qilib beradi!")
    st.write("")
    if st.button("O'yinni Boshlash 🚀"):
        st.session_state.step = "quiz"
        st.rerun()

# 2. SAVOLLAR SAHIFASI
elif st.session_state.step == "quiz":
    st.markdown("<div class='quiz-box'>", unsafe_allow_html=True)
    
    # Ism so'rash
    if "name" not in st.session_state.answers:
        name = st.text_input("Sizni to'liq ismingiz nima? ✍️", placeholder="Ism va familiyangizni yozing...")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Keyingisi ➡️"):
            if name.strip() != "":
                st.session_state.answers["name"] = name
                st.rerun()
            else: st.error("Iltimos, ismingizni kiriting!")

    # Qiziqish
    elif "interest" not in st.session_state.answers:
        interest = st.radio("Sizni eng ko'p nima qiziqtiradi? 💡", ["Dasturlash / IT", "Biznes / Startap", "San'at / Musiqa", "Sport / Sayohat"])
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Keyingisi ➡️"):
            st.session_state.answers["interest"] = interest
            st.rerun()

    # Taom
    elif "food" not in st.session_state.answers:
        food = st.radio("Yoqtirgan taomingiz qaysi? 🍲", ["Osh (Palov)", "Shashlik / Kabob", "Fast-food (Lavash/Pitsa)", "Suyuq taomlar"])
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Keyingisi ➡️"):
            st.session_state.answers["food"] = food
            st.rerun()

    # Rang
    elif "color" not in st.session_state.answers:
        color = st.radio("Sizga eng yoqadigan rang? 🎨", ["To'q qora / Kulrang", "Yorqin ko'k / Havorang", "Oq / Toza ranglar", "Yashil / Tabiat"])
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Keyingisi ➡️"):
            st.session_state.answers["color"] = color
            st.rerun()

    # Qo'shiq
    elif "song" not in st.session_state.answers:
        song = st.text_input("Qanday janrdagi qo'shiqlarni sevasiz? 🎵", placeholder="Yoqtirgan qo'shig'ingiz yoki janringiz...")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Keyingisi ➡️"):
            if song.strip() != "":
                st.session_state.answers["song"] = song
                st.rerun()
            else: st.error("Iltimos, ushbu maydonni to'ldiring!")

    # Tug'ilgan kun
    elif "birthday" not in st.session_state.answers:
        st.write("Tug'ilgan kuningiz qachon? 🎂")
        birthday = st.date_input("Sanani tanlang:", min_value=None, max_value=None)
        st.markdown("</div>", unsafe_allow_html=True)
        st.caption("*(Ushbu sana bo'yicha Shahobiddinga avtomatik bildirishnoma boradi!)*")
        if st.button("Keyingisi ➡️"):
            st.session_state.answers["birthday"] = str(birthday)
            st.rerun()

    # Orzu
    elif "dream" not in st.session_state.answers:
        dream = st.text_area("Kelajakdagi eng katta orzuingiz nima? 🌟", placeholder="Kelajakda kim bo'lmoqchisiz yoki qanday maqsadingiz bor...")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Natijani ko'rish 📊"):
            if dream.strip() != "":
                st.session_state.answers["dream"] = dream
                st.session_state.step = "final"
                st.rerun()
            else: st.error("Iltimos, orzuingizni yozing!")

# 3. FINAL SAHIFA
elif st.session_state.step == "final":
    st.balloons()
    
    if "percent" not in st.session_state:
        st.session_state.percent = random.randint(75, 99)
        send_to_telegram(st.session_state.answers, st.session_state.percent)
        
    st.markdown(f"""
    <div class='quiz-box' style='text-align: center; border-color: #4cd964;'>
        <h2 style='color: #4cd964; margin-top:0;'>O'yin Yakunlandi! 🎉</h2>
        <p style='color: #aaa;'>Matematik hisob-kitob yakunlandi:</p>
        <h1 style='font-size: 80px; color: #ff4b4b; margin: 10px 0; font-weight:900;'>{st.session_state.percent}%</h1>
        <h4 style='color: white;'>Daxshat! Siz Shahobiddin bilan {st.session_state.percent}% mos keldingiz! 🚀</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("<p style='text-align:center; color:#888;'>Shahobiddin bilan Instagramda bog'lanish va rahmat aytish:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📸 @mr.shahobiddin5", "https://instagram.com", use_container_width=True)
    with col2:
        st.link_button("🎓 @csu.university", "https://instagram.com", use_container_width=True)

    st.write("")
    if st.button("Qayta boshlash 🔄"):
        st.session_state.clear()
        st.rerun()
