import os
from dotenv import load_dotenv
from parcle import Parcle

load_dotenv()


class ParcleMemory:

    def __init__(self):

        self.client = Parcle(
            api_key=os.getenv("PARCLE_API_KEY")
        )

        self.user_id = "devsarthi-ai"

        # Create user if it doesn't exist
        try:
            result = self.client.create_user(
                user_id=self.user_id
            )

            print("PARCLE USER:", result)

        except Exception as e:
            print("PARCLE USER EXISTS:", e)


    def save_memory(self, text):

        try:

            result = self.client.ingest_dialog(
                user_id=self.user_id,
                messages=[
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            )

            print("PARCLE MEMORY SAVED")

            return True

        except Exception as e:

            print("PARCLE SAVE ERROR:", e)

            return False


    def search_memory(self, query):

        try:

            result = self.client.search(
                user_id=self.user_id,
                query=query
            )

            print("PARCLE SEARCH RESULT:", result)

            return [str(result)]

        except Exception as e:

            print("PARCLE SEARCH ERROR:", e)

            return []