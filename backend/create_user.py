from dotenv import load_dotenv
from parcle import Parcle
import os

load_dotenv()

client = Parcle(
    api_key=os.getenv("PARCLE_API_KEY")
)

try:
    result = client.create_user(
        user_id="devsarthi-ai"
    )

    print("USER CREATED")
    print(result)

except Exception as e:
    print("ERROR")
    print(repr(e))