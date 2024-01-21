#using the hugging face integration
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import HuggingFaceHub

huggingface_key = os.getenv('HUGGINGFACE_API_KEY')

llm = HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={"temperature": 1, "max_length": 128}
)
# text = "can you tell the capital of antartica"
# output = llm.invoke(text)
# print(output)