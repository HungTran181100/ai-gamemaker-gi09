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
input_text = st.text_input("Nhập nội dung của bạn tại đây")
submit = st.button("Gửi")

response = None
if input_text and submit:
    response = model.generate_content(input_text)

mess = st.empty()
if response:
    mess.markdown(response.text)
