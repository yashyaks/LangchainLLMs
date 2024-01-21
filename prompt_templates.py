#LLM prompt templates and Chain
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain_community.llms import HuggingFaceHub

huggingface_key = os.getenv('HUGGINGFACE_API_KEY')

llm = HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={"temperature": 0.1, "max_length": 128}
)

prompt_template = "Tell me the capital of {country}"
prompt = PromptTemplate(
    input_variables=["country"], 
    template=prompt_template
)

llmchain = LLMChain(llm=llm,prompt=prompt)
print(llmchain.run('India'))