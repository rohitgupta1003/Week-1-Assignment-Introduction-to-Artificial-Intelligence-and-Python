# Week 1 - Task 5
# Mini AI Project: Simple Rule-Based Chatbot


def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hello! Welcome."
    elif "how are you" in text:
        return "I'm fine, thank you! How about you?"
    elif "your name" in text:
        return "I am a simple rule-based chatbot made for the AI internship assignment."
    elif "what can you do" in text:
        return "I can chat about basic things like greetings and simple questions."
    elif "help" in text:
        return "Sure, I can help! Try asking me how I am, or just say hello."
    elif "thank" in text:
        return "You're welcome!"
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Can you rephrase?"


def main():
    print("Bot: Hi! I'm a rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
