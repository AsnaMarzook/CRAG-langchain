from prompt import prompt
from model import model

prompt = prompt.Prompt()
chat = model.Model()

chain = prompt.prompt | chat.chat
