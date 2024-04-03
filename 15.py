import cv2
import speech_recognition as sr
from bs4 import BeautifulSoup
import requests
import openai

# Set up OpenAI API and enter the API key below
openai.api_key = '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'

# Define function to query OpenAI's API for response
def ask_openai(question):
    """
    Queries OpenAI's API for a response to the given question.
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=question,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Define function to scrape a website for information
def scrape_website(url):
    """
    Scrapes the provided URL for relevant information.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find(class_='content').get_text()
        return content
    except Exception as e:
        return f"Error: {e}"

# Function to respond to common greetings
def respond_to_greeting(greeting):
    """
    Responds to common greetings.
    """
    if greeting.lower() in ["hello", "hi", "hey", "hola"]:
        return "Hello! How can I assist you today?"
    elif greeting.lower() in ["good morning", "good afternoon", "good evening"]:
        return f"{greeting.capitalize()}! What can I do for you?"
    else:
        return None

# Main loop for the chatbot
def chat():
    """
    Main loop for the chatbot.
    """
    recognizer = sr.Recognizer()

    print("Welcome to the Axil chatbot! How can I help you today?")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio)
                print("You:", user_input)

                if user_input.lower() == 'exit':
                    print("Goodbye! Have a nice day!!!")
                    break

                greeting_response = respond_to_greeting(user_input)
                if greeting_response:
                    print("Bot:", greeting_response)
                    continue

                elif user_input.lower().startswith('search'):
                    query = user_input.split(' ', 1)[1]
                    url = f"https://en.wikipedia.org/wiki/{query}"
                    response = scrape_website(url)
                    print(response)

                else:
                    response = ask_openai(user_input)
                    print("Bot:", response)

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said. Could you please repeat?")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Open camera
cap = cv2.VideoCapture(0)

# Set camera resolution to 1280x720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Set frame rate to 30 fps
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Chatbot", frame)

    # Call the chatbot function
    chat()

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
