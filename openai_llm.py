#using the openai integration
import os
from langchain_openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(openai_api_key= openai_key,temperature=0.6)
text="What is the capital of India"
print(llm.invoke(text))