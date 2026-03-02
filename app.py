import streamlit as st
from groq import Groq

# ১. Groq এআই কনফিগারেশন
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# ২. প্রিমিয়াম ব্ল্যাক ইন্টারফেস ও গ্লোয়িং ডিজাইন
st.set_page_config(page_title="Mastor AI", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    /* মেইন ব্যাকগ্রাউন্ড একদম কুচকুচে কালো */
    .stApp {
        background-color: #000000;
    }
    
    /* Mastor AI নামের নিয়ন গ্লোয়িং ইফেক্ট */
    .glow-text {
        font-size: 45px;
        color: #fff;
        text-align: center;
        font-weight: bold;
        text-shadow: 0 0 10px #00FFA2, 0 0 20px #00FFA2, 0 0 30px #00FFA2;
        padding: 20px;
        margin-top: -30px;
    }

    /* চ্যাট বাবল ডিজাইন */
    .stChatMessage {
        border-radius: 15px;
        background-color: #121212 !important;
        border: 1px solid #222;
        margin-bottom: 10px;
        color: white !important;
    }

    /* স্ক্রিন থেকে অপ্রয়োজনীয় মেনু লুকানো */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* ইনপুট বক্সের ডিজাইন */
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# গ্লোয়িং টাইটেল প্রদর্শন
st.markdown('<div class="glow-text">Mastor AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>আপনার পড়াশোনা ও ক্যারিয়ারের স্মার্ট সহযোগী</p>", unsafe_allow_html=True)
st.divider()

# ৩. মেমোরি ও চ্যাট হিস্ট্রি (যাতে আগের কথা মনে থাকে)
if "messages" not in st.session_state:
    st.session_state.messages = []

# আগের সব চ্যাট স্ক্রিনে দেখানো (History)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৪. ইউজার ইনপুট ও Groq এর মাধ্যমে উত্তর
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    # ইউজারের মেসেজ মেমোরিতে সেভ করা
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Groq Llama-3 মডেল (সুপার ফাস্ট)
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Mastor AI, a helpful educational assistant for Honors, Diploma, and Nursing students in Bangladesh. Always reply in friendly Bengali."},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ],
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            
            # এআই এর উত্তর মেমোরিতে সেভ করা
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"দুঃখিত ভাই, একটু সমস্যা হয়েছে: {str(e)}")
