from dotenv import load_dotenv
from parcle import Parcle
import os

load_dotenv()

client = Parcle(
    api_key=os.getenv("PARCLE_API_KEY")
)

result = client.ingest_dialog(
    user_id="devsarthi-ai",
    messages=[
        {
            "role": "user",
            "content": "I am building DevSarthi AI using LangGraph and Parcle."
        }
    ]
)

print(result)