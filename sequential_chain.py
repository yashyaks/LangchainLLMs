#Combining Multiple Chains Using simple Sequential Chain
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

from langchain.chains import SimpleSequentialChain

huggingface_key = os.getenv('HUGGINGFACE_API_KEY')

llm1 = HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={"temperature": 0.1, "max_length": 64}
)
llm2 = HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={"temperature": 0.9, "max_length": 128}
)

prompt_template1 = "Tell me the capital of {country}"
prompt1 = PromptTemplate(
    input_variables=["country"], 
    template=prompt_template1
)
prompt_template2 = "Tell me some amazing places to visit in {capital}"
prompt2 = PromptTemplate(
    input_variables=["capital"], 
    template=prompt_template2
)

llmchain1 = LLMChain(llm=llm1,prompt=prompt1)
llmchain2 = LLMChain(llm=llm2,prompt=prompt2)

chain = SimpleSequentialChain(chains=[llmchain1, llmchain2])
output = chain.run("India")
print(output)