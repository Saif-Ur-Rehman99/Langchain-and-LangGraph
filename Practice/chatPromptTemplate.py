from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
)

prompt = ChatPromptTemplate([
    ('system', 'you are a helpful chatbot for online website'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
with open('chat.txt') as file:
    chat_history.extend(file.readlines())


while True:
    user_query = input("You: ")
    if user_query == 'exit':
        break
    formatted_prompt = prompt.invoke(
        {
            'chat_history':chat_history,
            'query': user_query
        }
    )
    response = model.invoke(formatted_prompt)


    chat_history.append(HumanMessage(content=user_query))
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)


print("\nChat History\n", chat_history)





