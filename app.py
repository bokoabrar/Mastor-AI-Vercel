import streamlit as st
import google.generativeai as genai

# আপনার নতুন এপিআই কি এখানে সেট করা হয়েছে
NEW_API_KEY = "AIzaSyAybe_rf1-33JZSTnlWtHQRHOc2MuM9bBk"
genai.configure(api_key=NEW_API_KEY)

# পেজ ডিজাইন
st.set_page_config(page_title="Mastor AI", page_icon="🎓")
st.title("🎓 Mastor AI")
st.write("আপনার পড়াশোনা ও ক্যারিয়ারের বিশ্বস্ত সহযোগী")
st.divider()

# চ্যাট হিস্ট্রি মেনটেইন করা
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট ও এআই উত্তর
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # সঠিক মডেল কল করা
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Tumi Mastor AI expert. Friendly Banglay point akare uttor dao: {prompt}")
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # এরর আসলে তা পরিষ্কার দেখা যাবে
            st.error(f"দুঃখিত, সমস্যাটি হলো: {str(e)}")
