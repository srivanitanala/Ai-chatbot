from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

messages = []

print("Chatbot started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print("Bot:", reply)
