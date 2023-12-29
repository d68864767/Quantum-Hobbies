import os

# Get the OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found in environment variables. Please set the key as 'OPENAI_API_KEY'.")
<FINAL_CODE>