import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

class SimpleAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def run(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    agent = SimpleAgent()
    result = agent.run("What is an AI Agent?")
    print(result)
