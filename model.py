import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/thlurte/lab/EKB-API/app/experiments/temporal-bebop-411009-6fd3a81d0dc7.json"

from google.auth import default

# Obtain default credentials
credentials, project_id = default()

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import ChatVertexAI