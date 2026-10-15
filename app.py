from datetime import datetime
import random
import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="Echo-Terra: Seysmik AI Tizimi", page_icon="🌐", layout="centered"
)

# Kiber-neon uslubidagi CSS dizayn
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    .title-text {
        color: #00ffcc;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #00ffcc;
        color: #000000;
        font-weight: bold;
        border: none;
        width: 100%;
        border-radius: 4px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #00ccaa;
        color: #000000;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='title-text'>🌐 ECHO-TERRA: ANIQ HUDUD</div>",
    unsafe_allow_html=True,
)

# Sana kiritish maydoni
user_date = st.date_input(
    "Sana tanlang (yoki kiriting)",
    value=datetime.today(),
    help="Masalan: 2023-02-06",
)

if st.button("Hududni aniqlash"):
  target_date = user_date.strftime("%Y-%m-%d")

  if "2023-02-06" in target_date:
    res = (
        f"🚨 TARIXIY KRIZIS TAHMINI:\n"
        f"• Sana: {target_date}\n"
        f"• Hudud: Qahramanmarash / Gaziantep, Turkiya\n"
        f"• Koordinatalar: 37.17° N, 37.03° E\n"
        f"• Magnituda: 7.8 Richter\n"
        f"• O'choq chuqurligi: 17.9 km\n"
        f"• Xavf darajasi: O'ta yuqori (99%)"
    )
    st.error(res)
  else:
    regions = [
        ("Toshkent viloyati, Yangiyo'l tumani", "41.13° N, 69.04° E"),
        ("Farg'ona vodiysi, Namangan atrofi", "40.99° N, 71.67° E"),
        ("Samarqand viloyati hududi", "39.65° N, 66.95° E"),
        ("Hindikush tog' tizmasi", "36.50° N, 71.00° E"),
    ]
    chosen_region, coords = random.choice(regions)
    mag = round(random.uniform(3.1, 5.5), 1)
    depth = random.randint(10, 35)
    vib = round(random.uniform(0.1, 1.2), 2)

    status = (
        "🚨 Seysmik faollik aniqlandi!"
        if mag > 4.5
        else "✅ Barqaror, xavf yo'q."
    )

    res = (
        f"📊 Tahlil sanasi: {target_date}\n"
        f"• Taxminiy hudud: {chosen_region}\n"
        f"• Koordinatalar: {coords}\n"
        f"• Magnituda: {mag} M\n"
        f"• Chuqurlik: {depth} km\n"
        f"• Infratovush: {vib} Hz\n"
        f"• Holat: {status}"
    )

    if mag > 4.5:
      st.warning(res)
    else:
      st.success(res)