import streamlit as st
import google.generativeai as genai

# এআই কনফিগারেশন
API_KEY = "AIzaSyAMr6ggmKoZLmqQ47WIaUiOEYW_PunYCQE"
genai.configure(api_key=API_KEY)

# পেজ সেটআপ
st.set_page_config(page_title="Mastor AI", page_icon="🎓")
st.title("🎓 Mastor AI")
st.write("আপনার পড়াশোনা ও ক্যারিয়ারের বিশ্বস্ত সহযোগী")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # সঠিক মডেল কল করা হচ্ছে
            model = genai.GenerativeModel("gemini-1.5-flash")
            # এখানে 'stream=False' দিয়ে আমরা ভার্সন এররটি এড়াবো
            response = model.generate_content(f"Tumi Mastor AI expert. Friendly Banglay uttor dao: {prompt}")
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # এররটি যাতে পরিষ্কার দেখা যায়
            st.error(f"Error: {str(e)}")
