import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

model = genai.GenerativeModel(
    "gemini-2.0-flash-lite",
    system_instruction="""Bạn là một giáo viên giảng dạy môn lập trình game maker 2.0
    1. Hãy giúp học sinh đưa ra những ý tưởng hay cho trò chơi của mình.
    2. Chỉ đưa ra giải thích câu lệnh và gợi ý câu lệnh, các bước để làm bài chứ không đưa thẳng ra kết quả code.
    3. Không trả lời những câu hỏi không liên quan đến game maker""",
)

st.title("AI FOR GAME MAKER GI09")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị các tin nhắn trước đó
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Nhập tin nhắn mới
user_input = st.chat_input("Nhập tin nhắn của bạn...")

if user_input:
    # Hiển thị và lưu tin nhắn của người dùng
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Phản hồi đơn giản từ "AI"
    bot_response = f"🤖 {model.generate_content(user_input).text}"
    st.chat_message("assistant").markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
