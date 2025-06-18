from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Annotated, Optional, Literal
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

class Review(BaseModel):
    summary: Annotated[str, Field(description="one line summary of the review")]
    sentiment: Annotated[Literal['POSITIVE', 'NEGATIVE'], Field(description="sentiment of the review")]
    pros: Annotated[Optional[List[str]], Field(description="2 pros of from the review")] = None
    cons: Annotated[Optional[List[str]], Field(description="2 cons of from the review")] = None

# model = ChatGoogleGenerativeAI('gemini-1.5-flash')
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text_generation",
    provider="hf-inference"
)

model = ChatHuggingFace(llm=llm)
parser = PydanticOutputParser(pydantic_object=Review)

prompt_template = PromptTemplate(
    template="""
    Check this review and process it according to the given data format:
    {format_instruction}
    {review}
    """,
    input_variables=['review'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

review = """The headphones deliver excellent sound quality with deep bass and crisp highs.
I love the long battery life and comfortable fit for all-day use.
However, the touch controls can be overly sensitive and sometimes frustrating to use."""


chain = prompt_template | model | parser
response = chain.invoke({"review": review})
print(response)


# prompt = prompt_template.invoke({"review": review})
# response = model.invoke(prompt)
# print(response)