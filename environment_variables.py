import os
from dotenv import load_dotenv

class EnvironmentVariables():
    def __init__(self):
        load_dotenv()
        self.ip_stack_api_token = os.getenv('IP_STACK_API_TOKEN')
        self.api_stack_base_url = os.getenv('IP_STACK_BASE_URL')
