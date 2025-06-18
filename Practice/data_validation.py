from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Annotated, Optional

load_dotenv()

# model = ChatGoogleGenerativeAI('gemini-1.5-flash')


class User(BaseModel):
    name: Annotated[str, Field(max_length=50, description="name of the user")]
    age: Annotated[int, Field(gt=12, lt=50, description="age of the user")]
    height: float
    email: EmailStr
    is_student: bool
    subject: List[str]
    address: Optional[Dict[str,str]] = Field(default="no address")


user = {
    "name": "saif",
    "age": 13,
    "height": 5.11,
    "email": "saif.rehman@x",
    "is_student": False,
    "subject": ['OOP', 'DSA', 'MCP', 'AIML'],
    "address": {"contact": "923495510088", "city": "Karachi"}}


print(User(**user))