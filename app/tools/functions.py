import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def callGpt(prompt):
    # Initialize OpenAI API with the key from the environment
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    # Process the prompt and return the result
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate chat model
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content']