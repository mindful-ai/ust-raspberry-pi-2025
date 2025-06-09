# Use of send()

def conversation():
    print("🤖 Bot: Hello! What's your name?")
    name = yield  # Pause and wait to receive the name

    print(f"🤖 Bot: Nice to meet you, {name}! How are you today?")
    mood = yield  # Wait to receive mood

    print(f"🤖 Bot: Glad to hear you're feeling {mood}. Have a great day!")
    

# Create generator
chat = conversation()

# Start the generator
next(chat)  # Advances to first yield

# Send name
chat.send("Alex")

# Send mood
try:
    chat.send("great")
except StopIteration:
    pass
