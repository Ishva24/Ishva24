import openai
import requests
from bs4 import BeautifulSoup

# Set up OpenAI API and enter it below
openai.api_key = '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'

# Define function to query OpenAI's API for response
def ask_openai(question):
    # Query OpenAI API for response
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=question,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Define function to scrape a website for information
def scrape_website(url):
    # Send GET request to the provided URL
    response = requests.get(url)

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information
    # For example, if you want to extract the text of a specific element with class 'content':
    content = soup.find(class_='content').get_text()
    return content

# Function to simulate processing delay
def simulate_processing_delay():
    for _ in range(10000):
        pass

# Function to respond to common greetings
def respond_to_greeting(greeting):
    if greeting.lower() in ["hello", "hi", "hey", "hola"]:
        return "Hello! How can I assist you today?"
    elif greeting.lower() in ["good morning", "good afternoon", "good evening"]:
        return f"{greeting.capitalize()}! What can I do for you?"
    else:
        return None

# Main loop for the chatbot
def chat():
    # Greet the user
    print("Welcome to the Axil chatbot! How can I help you today?")

    # Start conversation loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye! Have a nice day!!!")
            break

        # Check if the user input is a greeting
        greeting_response = respond_to_greeting(user_input)
        if greeting_response:
            print("Bot:", greeting_response)
            continue

        # Check if the user wants to search something
        elif user_input.lower().startswith('search'):
            # Extract query from user input
            query = user_input.split(' ', 1)[1]

            # Construct Wikipedia URL , You can replace it with any website url
            url = f"https://en.wikipedia.org/wiki/{query}"

            # Introduce artificial delay
            simulate_processing_delay()

            # Try to scrape the website for information
            try:
                response = scrape_website(url)
                print(response)
            except Exception as e:
                print("Error:", e)

        # If the user input doesn't match any specific command, ask OpenAI
        else:
            # Introduce artificial delay
            simulate_processing_delay()

            response = ask_openai(user_input)
            print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()