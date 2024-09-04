from openai import OpenAI
import os

openai_client = OpenAI(api_key=os.getenv("JACO_OPENAI_API_KEY"))
openai_model = "gpt-4o-mini"

def main():
    query = "Hello, how are you?"
    history = []    
    chatbot(query, history)


def chatbot(query, history):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query},
    ]

    response = openai_client.chat.completions.create(
        model=openai_model,
        messages=messages,
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()