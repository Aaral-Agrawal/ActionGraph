import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("GEMINI_API_KEY")

if key :
    print("key loaded : First 4 characters : ", key[:4])
else:
    print("key not loaded")