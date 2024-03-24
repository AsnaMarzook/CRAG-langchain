from authentication import auth

from langchain_google_vertexai import ChatVertexAI


class Model():
    def __init__(self) -> None:
        self.chat = ChatVertexAI()
        self.auth = auth.Auth()
