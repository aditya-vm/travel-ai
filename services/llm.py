from openai import OpenAI
from dotenv import load_dotenv

import os


load_dotenv()


class LLMClient:

    def __init__(self):

        self.client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url=("https://openrouter.ai/api/v1"))

    def generate(self, prompt: str) -> str:

        response = (
            self.client.chat.completions.create(
                model="qwen/qwen3-32b",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.7
            )
        )

        return (response.choices[0].message.content)