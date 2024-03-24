from langchain_core.prompts import ChatPromptTemplate



class Prompt():
    def __init__(self) -> None:
        self.system = "You are a helpful assistant who assists students with helpful information "
        self.human = "Explain how photosynthesis works"
        self.prompt = ChatPromptTemplate.from_messages([("system", self.system), ("human", self.human)])
 