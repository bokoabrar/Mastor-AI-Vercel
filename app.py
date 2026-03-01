import streamlit as st
import google.generativeai as genai

# ১. এআই কনফিগারেশন (সরাসরি ভার্সন ফিক্স করা হয়েছে)
API_KEY = "AIzaSyAMr6ggmKoZLmqQ47WIaUiOEYW_PunYCQE"
genai.configure(api_key=API_KEY)

# ২. পেজ ডিজাইন
st.set_page_config(page_title="Mastor AI", page_icon="🎓")
st.title("🎓 Mastor AI")
st.write("আপনার পড়াশোনা ও ক্যারিয়ারের বিশ্বস্ত সহযোগী")
st.divider()

# ৩. চ্যাট হিস্ট্রি
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৪. ইনপুট ও এআই রেসপন্স
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # এখানে 'gemini-1.5-flash' ব্যবহার করা হয়েছে যা v1beta-তে নেই
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Tumi Mastor AI expert. Friendly Banglay uttor dao: {prompt}")
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.error("এআই কোনো উত্তর দিতে পারেনি।")
                
        except Exception as e:
            # এররটি পরিষ্কারভাবে দেখার জন্য
            st.error(f"Error: {str(e)}")
