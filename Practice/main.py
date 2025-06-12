from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

prompt = PromptTemplate(
    template="""You should act like my girlfriend.
    Rules:
    - You can only talk in Tunisian Arabic
    - You should be funny in your responses
    - Don't talk about math if someone asks you about it - just say "Not Again"
    Answer the question: {question}""",
    input_variables=["question"],
)

st.header("Chat")
question = st.text_input("Enter your question: ")

if st.button("Answer"):
    chain = prompt | model 
    response = chain.invoke({"question": question})
    st.write(response.content)
