import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\GitHub\CRAG-langchain\temporal-bebop-411009-6fd3a81d0dc7.json"

from google.auth import default

# Obtain default credentials
credentials, project_id = default()

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import ChatVertexAI

system = "You are a helpful assistant who translate English to Tamil"
human = "Translate this sentence from English to Tamil. I love programming."
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
 
chat = ChatVertexAI()
 
chain = prompt | chat
print(chain.invoke({}))