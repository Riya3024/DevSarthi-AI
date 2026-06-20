from dotenv import load_dotenv
from parcle import Parcle
import os

load_dotenv()

client = Parcle(
    api_key=os.getenv("PARCLE_API_KEY")
)

result = client.search(
    user_id="devsarthi-ai",
    query="What am I building?"
)

print(result)