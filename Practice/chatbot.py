from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

history = []

while True:
    user_input = input("You: ")
    history.append(user_input)
    if user_input == 'exit':
        break
    
    response = model.invoke(history)
    history.append(response.content)
    print("AI: ",  response.content)

print(history)




