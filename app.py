import streamlit as st
import google.generativeai as genai

# ১. এআই কনফিগারেশন
genai.configure(api_key="AIzaSyAMr6ggmKoZLmqQ47WIaUiOEYW_PunYCQE")

# ২. পেজ ডিজাইন ও টাইটেল পরিবর্তন
st.set_page_config(page_title="Mastor AI", page_icon="🎓")
st.title("🎓 Mastor AI")

# এখানে আপনি আপনার পছন্দমতো লেখা দিতে পারেন
st.write("আপনার পড়াশোনা ও ক্যারিয়ারের বিশ্বস্ত সহযোগী") 
st.divider()

# ৩. চ্যাট হিস্ট্রি
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৪. ইউজার ইনপুট ও এআই রেসপন্স
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # মডেলের নাম সঠিক রাখা হয়েছে যাতে আগের এরর না আসে
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"Tumi Mastor AI expert. Banglay uttor dao: {prompt}")
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("দুঃখিত, কোনো একটি সমস্যা হয়েছে।")
