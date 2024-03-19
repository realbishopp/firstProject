import random

# Define responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing well, how about you?", "I'm fine, thank you."],
    "what's your name": ["I'm just a simple chatbot.", "I'm your friendly chatbot assistant!"],
    "default": ["Sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."],
}

def chatbot_response(user_input):
    # Convert input to lowercase for case insensitivity
    user_input = user_input.lower()
    
    # Check if input matches any predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no match is found, return a default response
    return random.choice(responses["default"])

# Main loop for interacting with the chatbot
print("Welcome to the Chatbot!")
print("You can start chatting or type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)