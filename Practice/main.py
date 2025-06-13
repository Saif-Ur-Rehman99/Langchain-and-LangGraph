from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

prompt = load_prompt("prompt.json")

st.header("Chat")
relation = st.selectbox("Select your relation:", ["Programmer", "Cricketer", "Doctor"])
tone = st.selectbox("Select the tone:", ["bad tempered", "formal", "funny"])
question = st.text_input("Enter your question:")

if st.button("Send"):
    chain = prompt | model
    response = chain.invoke({"relation": relation, "tone": tone, "question": question})
    st.write(response.content)
