import os
from google.auth import default

# Obtain default credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"mehhhh........."

class Auth():
    def __init__(self) -> None:
        credentials, project_id = default()

