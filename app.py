import streamlit as st
import google.generativeai as genai

# Setup ukurasa
st.set_page_config(page_title="Wilson & Gemini AI", page_icon="🤖")

st.title("🤖 Wilson & Gemini AI")
st.write("Karibu Wilson! Huu ni mfumo wako wa AI unakuwezesha kuuliza chochote.")

# Sehemu ya kuweka API Key (Tutaweka Streamlit Secrets baadaye)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model =
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Andika swali lako hapa..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
