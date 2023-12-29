import openai
from config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def quantum_hobbies(prompt):
    """
    This function takes a prompt as input and returns a completion generated by OpenAI's GPT-3 model.
    """
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Quantum physics is a hobby of mine. Can you generate a paragraph about it?"
    print(quantum_hobbies(prompt))