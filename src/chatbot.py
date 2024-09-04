from openai import OpenAI
import os

openai_client = OpenAI(api_key=os.getenv("JACO_OPENAI_API_KEY"))
openai_model = "gpt-4o-mini"

def main():
    query = "What is capital of France?"
    history = []    
    chatbot(query, history)

    query = "How about India?"
    chatbot(query, history)

def chatbot(query, history):
    # Add system message and previous history to messages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages.extend(history)
    
    # Add the current user query
    messages.append({"role": "user", "content": query})

    response = openai_client.chat.completions.create(
        model=openai_model,
        messages=messages,
    )

    # Get the assistant's response
    assistant_response = response.choices[0].message.content

    # Add the assistant's response to the history
    history.append({"role": "user", "content": query})
    history.append({"role": "assistant", "content": assistant_response})

    print(assistant_response)

if __name__ == "__main__":
    main()