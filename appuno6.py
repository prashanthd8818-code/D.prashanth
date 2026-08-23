# create a simple chatbot using python that 
# can respond to basic greetings and answer 
# 5 basic questions also use exception handling


def chatbot():
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: You can ask me basic questions.")
    print("Chatbot: Type 'bye' to exit.")

    while True:
        try:
            user = input("You: ").lower().strip()

            # Exit
            if user == "bye":
                print("Chatbot: Goodbye! Have a nice day.")
                break

            # Greetings
            elif user in ["hello", "hi", "hey"]:
                print("Chatbot: Hello! How are you?")

            # Question 1
            elif "your name" in user:
                print("Chatbot: My name is Python Bot.")

            # Question 2
            elif "how are you" in user:
                print("Chatbot: I am fine. Thank you!")

            # Question 3
            elif "what is python" in user:
                print("Chatbot: Python is a popular programming language.")

            # Question 4
            elif "who created python" in user:
                print("Chatbot: Python was created by Guido van Rossum.")

            # Question 5
            elif "what is ai" in user:
                print("Chatbot: AI stands for Artificial Intelligence.")

            # Unknown question
            else:
                print("Chatbot: Sorry, I don't understand that question.")

        except Exception as e:
            print("Chatbot: Something went wrong.")
            print("Error:", e)


chatbot()