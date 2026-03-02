import streamlit as st
from groq import Groq

# Groq API Key সেটআপ
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# পেজ কনফিগারেশন
st.set_page_config(page_title="Mastor AI", page_icon="🎓")
st.title("🎓 Mastor AI")
st.write("আপনার পড়াশোনা ও ক্যারিয়ারের বিশ্বস্ত সহযোগী (Powered by Groq)")
st.divider()

# চ্যাট হিস্ট্রি
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইনপুট ও এআই রেসপন্স
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Llama 3.3 মডেল ব্যবহার করা হচ্ছে যা সুপার ফাস্ট
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Mastor AI, an expert in Honors, Diploma, and Nursing admission in Bangladesh. Answer in friendly Bengali and use bullet points."},
                    {"role": "user", "content": prompt}
                ],
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error: {str(e)}")
