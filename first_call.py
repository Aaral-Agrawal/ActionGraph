import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

#1 Load the api from .env file
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

#2 Create a client(our connection to gemini)
client = genai.Client(api_key=api_key)

#3 Which model to use
MODEL = "gemini-3.5-flash"

#4 the text we send (the "user prompt")
paragraph = """
In today's meeting , Priya said the API design doc is outdated and Alex 
agrred to update it by October 12 , The team also decided to postpone the
 mobile app launch by two weeks because of a performance issue. 
"""

#5 Send the request 
response = client.models.generate_content(
    model=MODEL,
    contents=f"Summarize this paragraph in one sentence:\n{paragraph}",
    config=types.GenerateContentConfig(
        temperature=0,
        system_instruction="You are a precise meeting assistant. Never add Facts not in the text.",
    ),
)

#6 Print the answer and the token usage
print(response.text)
print("---")
print("Tokens used:", response.usage_metadata)