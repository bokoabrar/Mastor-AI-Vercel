import streamlit as st
from groq import Groq

# ১. Groq API কনফিগারেশন (আপনার Key এখানে দিন)
GROQ_API_KEY = "gsk_y4M3B2l2EovFhH6pY68yWGdyb3FyeXbJ6N1kR5N2l2EovFhH6pY68y" 
client = Groq(api_key=GROQ_API_KEY)

# ২. পেজ সেটআপ ও ক্লিন ডিজাইন (Gemini/ChatGPT Style)
st.set_page_config(page_title="Mastor AI", page_icon="🎓", layout="centered")

# কাস্টম CSS (সবুজ গ্লো বা অতিরিক্ত রঙ সরিয়ে একদম ক্লিন করা হয়েছে)
st.markdown("""
    <style>
    /* মেইন ব্যাকগ্রাউন্ড কালো (ডার্ক মোড) */
    .stApp {
        background-color: #000000;
    }
    
    /* টাইটেল একদম ক্লিন সাদা করা হয়েছে (কোনো গ্লো নেই) */
    .clean-title {
        font-size: 40px;
        color: #FFFFFF;
        text-align: center;
        font-weight: bold;
        padding: 20px 0;
    }

    /* চ্যাট বাবল ডিজাইন (Gemini Style - ক্লিন এবং গ্রে) */
    .stChatMessage {
        border-radius: 10px !important;
        background-color: #1A1A1A !important;
        border: 1px solid #333 !important;
        margin-bottom: 8px !important;
    }

    /* টেক্সট কালার উজ্জ্বল সাদা এবং পড়তে সুবিধা এমন */
    .stMarkdown p {
        color: #E0E0E0 !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
    }

    /* অপ্রয়োজনীয় জিনিস লুকিয়ে একদম ক্লিন লুক দেওয়া হয়েছে */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ক্লিন টাইটেল প্রদর্শন
st.markdown('<div class="clean-title">Mastor AI</div>', unsafe_allow_html=True)

# ৩. মেমোরি সিস্টেম
if "messages" not in st.session_state:
    st.session_state.messages = []

# চ্যাট হিস্ট্রি স্ক্রিনে ধরে রাখা (Chat History Visibility)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৪. চ্যাট লজিক (Hello দিয়ে শুরু এবং মেমোরি)
if prompt := st.chat_input("যেকোনো প্রশ্ন করুন..."):
    # ইউজারের মেসেজ সেভ
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Groq API কল (মেমোরি সহ)
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are Mastor AI. Start with 'Hello'. Answer in friendly Bengali. Keep responses clean."},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ],
            )
            response_text = completion.choices[0].message.content
            st.markdown(response_text)
            
            # মেমোরিতে সেভ
            st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"দুঃখিত ভাই, একটু সমস্যা হয়েছে: {str(e)}")
